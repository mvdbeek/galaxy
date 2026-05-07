"""Build and query a local SQLite index of biocontainers.

The index is populated from two public sources:

* biocontainers.pro GA4GH TRS API
  (``https://api.biocontainers.pro/ga4gh/trs/v2/tools``) — single-package
  containers with their concrete tags/builds.
* The BioContainers ``multi-package-containers`` repository
  (``combinations/hash.tsv``) — every multi-package combination that has
  been built. The mulled-v2 hash is computed deterministically from the
  package list, and the published tag is resolved from quay.io.

Used by the MCP ``find_biocontainer`` tool to resolve a list of software
requirements (name + optional version) into a quay.io biocontainer image
identifier. When the index lacks an entry the lookup falls back to a live
quay.io query via ``targets_to_mulled_name``.
"""

import argparse
import json
import logging
import os
import sqlite3
import sys
import time
from concurrent.futures import (
    as_completed,
    ThreadPoolExecutor,
)
from typing import (
    Any,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
)

from galaxy.util import requests
from .util import (
    build_target,
    mulled_tags_for,
    MULLED_SOCKET_TIMEOUT,
    v2_image_name,
    version_sorted,
)

log = logging.getLogger(__name__)

SCHEMA_VERSION = "1"
DEFAULT_NAMESPACE = "biocontainers"
BIOCONTAINERS_PRO_API = "https://api.biocontainers.pro/ga4gh/trs/v2/tools"
MULTI_PACKAGE_HASH_TSV_URL = (
    "https://raw.githubusercontent.com/BioContainers/multi-package-containers/master/combinations/hash.tsv"
)
DEFAULT_TOOLS_PAGE_LIMIT = 1000
DEFAULT_BUILD_WORKERS = 16


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS single_packages (
    name              TEXT NOT NULL,
    version           TEXT NOT NULL,
    build             TEXT NOT NULL DEFAULT '',
    image_identifier  TEXT NOT NULL,
    image_type        TEXT NOT NULL,
    PRIMARY KEY (name, version, build, image_type)
);
CREATE INDEX IF NOT EXISTS idx_single_name_version ON single_packages(name, version);
CREATE INDEX IF NOT EXISTS idx_single_name ON single_packages(name);

CREATE TABLE IF NOT EXISTS mulled_containers (
    package_hash      TEXT NOT NULL,
    version_hash      TEXT NOT NULL DEFAULT '',
    image_identifier  TEXT NOT NULL,
    PRIMARY KEY (package_hash, version_hash)
);

CREATE TABLE IF NOT EXISTS mulled_packages (
    package_hash      TEXT NOT NULL,
    version_hash      TEXT NOT NULL DEFAULT '',
    package_name      TEXT NOT NULL,
    package_version   TEXT
);
CREATE INDEX IF NOT EXISTS idx_mulled_pkg_name ON mulled_packages(package_name);
CREATE INDEX IF NOT EXISTS idx_mulled_hash ON mulled_packages(package_hash, version_hash);

CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT
);
"""


def connect(db_path: str) -> sqlite3.Connection:
    """Open the SQLite index, creating tables on first use."""
    parent = os.path.dirname(os.path.abspath(db_path))
    if parent and not os.path.isdir(parent):
        os.makedirs(parent, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA_SQL)
    conn.commit()
    return conn


def _set_meta(conn: sqlite3.Connection, key: str, value: str) -> None:
    conn.execute("INSERT OR REPLACE INTO meta(key, value) VALUES (?, ?)", (key, value))


def _http_get_json(url: str, session: requests.Session, retries: int = 3) -> Any:
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=MULLED_SOCKET_TIMEOUT)
            if resp.status_code in (429, 500, 502, 503, 504):
                time.sleep(2**attempt)
                continue
            resp.raise_for_status()
            if resp.status_code == 204 or not resp.content:
                return None
            return resp.json()
        except requests.exceptions.RequestException as e:
            if attempt == retries - 1:
                log.warning("GET %s failed after %d attempts: %s", url, retries, e)
                return None
            time.sleep(2**attempt)
    return None


def _iter_biocontainers_pro_tools(
    session: requests.Session, page_limit: int = DEFAULT_TOOLS_PAGE_LIMIT
) -> Iterable[Dict[str, Any]]:
    """Yield tool records from biocontainers.pro, paginating via the ``next_page`` query parameter."""
    next_page: Optional[str] = None
    while True:
        params = {"limit": page_limit}
        if next_page:
            params["offset"] = next_page
        resp = session.get(BIOCONTAINERS_PRO_API, params=params, timeout=MULLED_SOCKET_TIMEOUT)
        resp.raise_for_status()
        # The TRS API exposes pagination via a ``next_page`` response header.
        page = resp.json()
        if not page:
            break
        yield from page
        next_page = resp.headers.get("next_page")
        if not next_page:
            break


def _ingest_version_images(
    conn: sqlite3.Connection,
    tool_name: str,
    version_data: Dict[str, Any],
) -> int:
    """Insert image rows for a single TRS version response. Returns rows inserted."""
    images = version_data.get("images") or []
    meta_version = version_data.get("meta_version") or version_data.get("name")
    if not meta_version:
        return 0
    inserted = 0
    rows: List[Tuple[str, str, str, str, str]] = []
    for image in images:
        image_name = image.get("image_name")
        image_type = image.get("image_type")
        if not image_name or image_type not in ("Docker", "Singularity"):
            continue
        # Image names look like quay.io/biocontainers/samtools:1.23.1--ha83d96e_0
        # For Singularity image names look like "samtools:1.23.1--ha83d96e_0"
        tag = image_name.rsplit(":", 1)[-1] if ":" in image_name else ""
        build = ""
        if "--" in tag:
            _, build = tag.rsplit("--", 1)
        rows.append((tool_name, str(meta_version), build, image_name, image_type))
    if rows:
        conn.executemany(
            """INSERT OR REPLACE INTO single_packages
               (name, version, build, image_identifier, image_type) VALUES (?, ?, ?, ?, ?)""",
            rows,
        )
        inserted = len(rows)
    return inserted


def build_single_packages(
    conn: sqlite3.Connection,
    *,
    workers: int = DEFAULT_BUILD_WORKERS,
    limit: Optional[int] = None,
    session: Optional[requests.Session] = None,
) -> int:
    """Populate ``single_packages`` from biocontainers.pro. Returns rows inserted."""
    if session is None:
        session = requests.Session()
    log.info("Fetching tool list from %s", BIOCONTAINERS_PRO_API)
    inserted = 0
    pending: List[Tuple[str, str]] = []  # (tool_name, version_url)
    seen_tools = 0
    for tool in _iter_biocontainers_pro_tools(session):
        seen_tools += 1
        tool_name = tool.get("name")
        if not tool_name:
            continue
        for version in tool.get("versions") or []:
            url = version.get("url")
            if url:
                pending.append((tool_name, url))
        if limit is not None and seen_tools >= limit:
            break
    log.info("Fetching image lists for %d versions across %d tools", len(pending), seen_tools)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_http_get_json, url, session): (tool_name, url) for tool_name, url in pending}
        batch_count = 0
        for fut in as_completed(futures):
            tool_name, _ = futures[fut]
            data = fut.result()
            if not data:
                continue
            inserted += _ingest_version_images(conn, tool_name, data)
            batch_count += 1
            if batch_count % 200 == 0:
                conn.commit()
    conn.commit()
    _set_meta(conn, "last_built_single_packages_at", str(int(time.time())))
    log.info("Inserted %d single-package image rows", inserted)
    return inserted


def _parse_targets_field(targets_field: str) -> List[Tuple[str, Optional[str]]]:
    """Parse a ``pkg=ver,pkg=ver,...`` cell from hash.tsv."""
    result: List[Tuple[str, Optional[str]]] = []
    for raw in targets_field.split(","):
        raw = raw.strip()
        if not raw:
            continue
        if "=" in raw:
            name, _, version = raw.partition("=")
            result.append((name.strip(), version.strip() or None))
        else:
            result.append((raw, None))
    return result


def _split_v2_image_name(image_name: str) -> Tuple[str, Optional[str]]:
    """Split a ``v2_image_name`` result into ``(package_hash, version_hash)``.

    For multi-package targets ``v2_image_name`` returns either
    ``mulled-v2-<package_hash>`` (no versions) or
    ``mulled-v2-<package_hash>:<version_hash>``.
    """
    if ":" in image_name:
        repo, tag = image_name.split(":", 1)
        return repo.replace("mulled-v2-", "", 1), tag
    return image_name.replace("mulled-v2-", "", 1), None


def build_mulled_containers(
    conn: sqlite3.Connection,
    *,
    limit: Optional[int] = None,
    session: Optional[requests.Session] = None,
    resolve_tags: bool = True,
) -> int:
    """Populate ``mulled_containers`` and ``mulled_packages`` from hash.tsv. Returns combinations inserted."""
    if session is None:
        session = requests.Session()
    log.info("Fetching %s", MULTI_PACKAGE_HASH_TSV_URL)
    resp = session.get(MULTI_PACKAGE_HASH_TSV_URL, timeout=MULLED_SOCKET_TIMEOUT)
    resp.raise_for_status()
    inserted = 0
    for line_no, raw_line in enumerate(resp.text.splitlines()):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        targets_field = line.split("\t", 1)[0]
        parsed = _parse_targets_field(targets_field)
        if len(parsed) < 2:
            continue
        targets = [build_target(name, version=version) for name, version in parsed]
        base_image_name = v2_image_name(targets)
        package_hash, version_hash = _split_v2_image_name(base_image_name)

        image_identifier: Optional[str] = None
        if resolve_tags:
            try:
                tags = mulled_tags_for(DEFAULT_NAMESPACE, f"mulled-v2-{package_hash}", session=session)
                if version_hash:
                    tags = [t for t in tags if t.startswith(version_hash)]
                if tags:
                    image_identifier = (
                        f"quay.io/{DEFAULT_NAMESPACE}/mulled-v2-{package_hash}:{version_sorted(tags)[0]}"
                    )
            except requests.exceptions.RequestException as e:
                log.warning("Tag lookup failed for %s line %d: %s", package_hash, line_no, e)

        if image_identifier is None:
            # No published tag yet; record the deterministic name without a tag so callers
            # at least learn the canonical mulled image name.
            image_identifier = f"quay.io/{DEFAULT_NAMESPACE}/mulled-v2-{package_hash}"
            if version_hash:
                image_identifier = f"{image_identifier}:{version_hash}"

        conn.execute(
            "INSERT OR REPLACE INTO mulled_containers (package_hash, version_hash, image_identifier) VALUES (?, ?, ?)",
            (package_hash, version_hash or "", image_identifier),
        )
        conn.execute(
            "DELETE FROM mulled_packages WHERE package_hash = ? AND version_hash = ?",
            (package_hash, version_hash or ""),
        )
        conn.executemany(
            "INSERT INTO mulled_packages (package_hash, version_hash, package_name, package_version) VALUES (?, ?, ?, ?)",
            [(package_hash, version_hash or "", name, version) for name, version in parsed],
        )
        inserted += 1
        if inserted % 200 == 0:
            conn.commit()
        if limit is not None and inserted >= limit:
            break
    conn.commit()
    _set_meta(conn, "last_built_mulled_containers_at", str(int(time.time())))
    log.info("Inserted %d multi-package mulled combinations", inserted)
    return inserted


def build_index(
    db_path: str,
    *,
    sources: Optional[List[str]] = None,
    limit: Optional[int] = None,
    workers: int = DEFAULT_BUILD_WORKERS,
) -> Dict[str, int]:
    """Build (or refresh) the SQLite index. Returns a count summary."""
    sources = sources or ["biocontainers_pro", "multi_package_containers"]
    conn = connect(db_path)
    try:
        _set_meta(conn, "schema_version", SCHEMA_VERSION)
        result: Dict[str, int] = {}
        if "biocontainers_pro" in sources:
            result["single_packages"] = build_single_packages(conn, limit=limit, workers=workers)
        if "multi_package_containers" in sources:
            result["mulled_containers"] = build_mulled_containers(conn, limit=limit)
        return result
    finally:
        conn.close()


def _normalize_software(software: List[Dict[str, Any]]) -> List[Tuple[str, Optional[str]]]:
    out: List[Tuple[str, Optional[str]]] = []
    for entry in software:
        if not isinstance(entry, dict):
            raise ValueError(f"software entries must be dicts, got: {entry!r}")
        name = entry.get("name")
        if not name:
            raise ValueError(f"software entry missing 'name': {entry!r}")
        version = entry.get("version") or None
        out.append((str(name), str(version) if version is not None else None))
    return out


def _packages_for_mulled(
    conn: sqlite3.Connection, package_hash: str, version_hash: Optional[str]
) -> List[Dict[str, Any]]:
    rows = conn.execute(
        "SELECT package_name, package_version FROM mulled_packages WHERE package_hash = ? AND version_hash = ?",
        (package_hash, version_hash or ""),
    ).fetchall()
    return [{"name": r["package_name"], "version": r["package_version"], "build": None} for r in rows]


def _lookup_single(conn: sqlite3.Connection, name: str, version: Optional[str]) -> Optional[Dict[str, Any]]:
    if version is not None:
        row = conn.execute(
            """SELECT name, version, build, image_identifier, image_type FROM single_packages
               WHERE name = ? AND version = ? AND image_type = 'Docker' ORDER BY build DESC LIMIT 1""",
            (name, version),
        ).fetchone()
    else:
        # Pick the newest version using version_sorted on the candidate tags.
        rows = conn.execute(
            """SELECT name, version, build, image_identifier, image_type FROM single_packages
               WHERE name = ? AND image_type = 'Docker'""",
            (name,),
        ).fetchall()
        if not rows:
            return None
        tags = [f"{r['version']}--{r['build']}" if r["build"] else r["version"] for r in rows]
        sorted_tags = version_sorted(tags)
        if not sorted_tags:
            return None
        best = sorted_tags[0]
        for r in rows:
            candidate = f"{r['version']}--{r['build']}" if r["build"] else r["version"]
            if candidate == best:
                row = r
                break
        else:
            return None
    if row is None:
        return None
    return {
        "image": row["image_identifier"],
        "image_type": row["image_type"],
        "registry": "quay.io",
        "packages": [{"name": row["name"], "version": row["version"], "build": row["build"] or None}],
        "source": "db",
    }


def _lookup_mulled(
    conn: sqlite3.Connection, software: List[Tuple[str, Optional[str]]]
) -> Optional[Dict[str, Any]]:
    targets = [build_target(name, version=version) for name, version in software]
    base_image_name = v2_image_name(targets)
    package_hash, version_hash = _split_v2_image_name(base_image_name)
    row = conn.execute(
        "SELECT image_identifier FROM mulled_containers WHERE package_hash = ? AND version_hash = ?",
        (package_hash, version_hash or ""),
    ).fetchone()
    if row is None:
        return None
    return {
        "image": row["image_identifier"],
        "image_type": "Docker",
        "registry": "quay.io",
        "packages": _packages_for_mulled(conn, package_hash, version_hash),
        "source": "db",
    }


def _live_lookup(software: List[Tuple[str, Optional[str]]]) -> Optional[Dict[str, Any]]:
    # Imported here to avoid a circular-import-on-import-time cost; this path is the
    # exception rather than the rule.
    from galaxy.tool_util.deps.container_resolvers.mulled import targets_to_mulled_name

    targets = [build_target(name, version=version) for name, version in software]
    name = targets_to_mulled_name(targets, hash_func="v2", namespace=DEFAULT_NAMESPACE)
    if not name:
        return None
    return {
        "image": f"quay.io/{DEFAULT_NAMESPACE}/{name}",
        "image_type": "Docker",
        "registry": "quay.io",
        "packages": [{"name": n, "version": v, "build": None} for n, v in software],
        "source": "live",
    }


def find_biocontainer(
    software: List[Dict[str, Any]],
    db_path: Optional[str] = None,
    allow_live_fallback: bool = True,
) -> Dict[str, Any]:
    """Resolve a list of software requirements to a biocontainer image.

    ``software`` is a list like ``[{"name": "samtools", "version": "1.21"}, ...]``;
    ``version`` is optional. Returns a dict with ``image``, ``image_type``,
    ``registry``, ``packages``, and a ``source`` of ``"db"``, ``"live"``, or
    ``"not_found"``.
    """
    parsed = _normalize_software(software)
    if not parsed:
        raise ValueError("software list must contain at least one entry")

    result: Optional[Dict[str, Any]] = None
    if db_path and os.path.exists(db_path):
        conn = connect(db_path)
        try:
            if len(parsed) == 1:
                name, version = parsed[0]
                result = _lookup_single(conn, name, version)
            else:
                result = _lookup_mulled(conn, parsed)
        finally:
            conn.close()

    if result is None and allow_live_fallback:
        result = _live_lookup(parsed)

    if result is None:
        return {
            "image": None,
            "image_type": None,
            "registry": None,
            "packages": [{"name": n, "version": v, "build": None} for n, v in parsed],
            "source": "not_found",
        }
    return result


def _parse_lookup_args(args: List[str]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for arg in args:
        if "=" in arg:
            name, _, version = arg.partition("=")
            out.append({"name": name, "version": version or None})
        else:
            out.append({"name": arg, "version": None})
    return out


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument(
        "--db-path",
        default=os.environ.get("GALAXY_BIOCONTAINER_DB", "biocontainer_index.sqlite"),
        help="Path to the SQLite index file (default: biocontainer_index.sqlite)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_build = sub.add_parser("build", help="Build or refresh the index")
    p_build.add_argument(
        "--source",
        default="biocontainers_pro,multi_package_containers",
        help="Comma-separated list of sources to ingest",
    )
    p_build.add_argument("--limit", type=int, default=None, help="Cap rows per source for testing")
    p_build.add_argument("--workers", type=int, default=DEFAULT_BUILD_WORKERS, help="Parallel HTTP fetchers")

    p_lookup = sub.add_parser("lookup", help="Look up a biocontainer image")
    p_lookup.add_argument("software", nargs="+", help="Software specs as name or name=version")
    p_lookup.add_argument("--no-live", action="store_true", help="Disable live quay.io fallback")

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    if args.command == "build":
        sources = [s.strip() for s in args.source.split(",") if s.strip()]
        summary = build_index(args.db_path, sources=sources, limit=args.limit, workers=args.workers)
        print(json.dumps(summary, indent=2))
        return 0
    if args.command == "lookup":
        result = find_biocontainer(
            _parse_lookup_args(args.software),
            db_path=args.db_path,
            allow_live_fallback=not args.no_live,
        )
        print(json.dumps(result, indent=2))
        return 0 if result.get("source") != "not_found" else 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
