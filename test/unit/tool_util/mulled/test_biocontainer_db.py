import os
import sqlite3

import pytest

from galaxy.tool_util.deps.mulled import biocontainer_db


def _seed_single(conn: sqlite3.Connection, rows):
    conn.executemany(
        "INSERT INTO single_packages (name, version, build, image_identifier, image_type) VALUES (?, ?, ?, ?, ?)",
        rows,
    )
    conn.commit()


def _seed_mulled(conn: sqlite3.Connection, package_hash, version_hash, image, packages):
    conn.execute(
        "INSERT INTO mulled_containers (package_hash, version_hash, image_identifier) VALUES (?, ?, ?)",
        (package_hash, version_hash or "", image),
    )
    conn.executemany(
        "INSERT INTO mulled_packages (package_hash, version_hash, package_name, package_version) VALUES (?, ?, ?, ?)",
        [(package_hash, version_hash or "", n, v) for n, v in packages],
    )
    conn.commit()


@pytest.fixture
def db_path(tmp_path):
    path = str(tmp_path / "bc.sqlite")
    conn = biocontainer_db.connect(path)
    try:
        _seed_single(
            conn,
            [
                ("samtools", "1.21", "h96c455f_1", "quay.io/biocontainers/samtools:1.21--h96c455f_1", "Docker"),
                ("samtools", "1.20", "h50ea8bc_0", "quay.io/biocontainers/samtools:1.20--h50ea8bc_0", "Docker"),
                ("samtools", "1.21", "h96c455f_1", "samtools:1.21--h96c455f_1", "Singularity"),
            ],
        )
    finally:
        conn.close()
    return path


def test_lookup_single_with_version(db_path):
    result = biocontainer_db.find_biocontainer(
        [{"name": "samtools", "version": "1.21"}], db_path=db_path, allow_live_fallback=False
    )
    assert result["source"] == "db"
    assert result["image"] == "quay.io/biocontainers/samtools:1.21--h96c455f_1"
    assert result["image_type"] == "Docker"
    assert result["packages"] == [{"name": "samtools", "version": "1.21", "build": "h96c455f_1"}]


def test_lookup_single_without_version_returns_newest(db_path):
    result = biocontainer_db.find_biocontainer(
        [{"name": "samtools"}], db_path=db_path, allow_live_fallback=False
    )
    assert result["source"] == "db"
    # version_sorted should pick 1.21 over 1.20
    assert result["image"] == "quay.io/biocontainers/samtools:1.21--h96c455f_1"


def test_lookup_miss_without_fallback(db_path):
    result = biocontainer_db.find_biocontainer(
        [{"name": "no-such-tool", "version": "9.9"}], db_path=db_path, allow_live_fallback=False
    )
    assert result["source"] == "not_found"
    assert result["image"] is None


def test_lookup_mulled_uses_v2_hash(tmp_path):
    db_path = str(tmp_path / "bc.sqlite")
    conn = biocontainer_db.connect(db_path)
    try:
        # Compute the same hash as the lookup will.
        from galaxy.tool_util.deps.mulled.util import build_target, v2_image_name

        targets = [build_target("bwa", version="0.7.17"), build_target("samtools", version="1.10")]
        package_hash, version_hash = biocontainer_db._split_v2_image_name(v2_image_name(targets))
        _seed_mulled(
            conn,
            package_hash,
            version_hash,
            f"quay.io/biocontainers/mulled-v2-{package_hash}:{version_hash}-0",
            [("bwa", "0.7.17"), ("samtools", "1.10")],
        )
    finally:
        conn.close()

    result = biocontainer_db.find_biocontainer(
        [
            {"name": "bwa", "version": "0.7.17"},
            {"name": "samtools", "version": "1.10"},
        ],
        db_path=db_path,
        allow_live_fallback=False,
    )
    assert result["source"] == "db"
    assert result["image"].startswith("quay.io/biocontainers/mulled-v2-")
    assert {p["name"] for p in result["packages"]} == {"bwa", "samtools"}


def test_normalize_software_validates():
    with pytest.raises(ValueError):
        biocontainer_db.find_biocontainer([], db_path=None, allow_live_fallback=False)
    with pytest.raises(ValueError):
        biocontainer_db.find_biocontainer([{"version": "1.0"}], db_path=None, allow_live_fallback=False)


def test_db_missing_falls_back_to_not_found_without_live(tmp_path):
    missing = str(tmp_path / "does-not-exist.sqlite")
    assert not os.path.exists(missing)
    result = biocontainer_db.find_biocontainer(
        [{"name": "samtools", "version": "1.21"}], db_path=missing, allow_live_fallback=False
    )
    assert result["source"] == "not_found"


def test_parse_targets_field():
    parsed = biocontainer_db._parse_targets_field("bwa=0.7.17,samtools=1.10, picard")
    assert parsed == [("bwa", "0.7.17"), ("samtools", "1.10"), ("picard", None)]


def test_split_v2_image_name():
    assert biocontainer_db._split_v2_image_name("mulled-v2-abc123") == ("abc123", None)
    assert biocontainer_db._split_v2_image_name("mulled-v2-abc123:def456") == ("abc123", "def456")


def test_build_mulled_containers_from_tsv(monkeypatch, tmp_path):
    """Build the mulled table from a fake hash.tsv response, with no live tag resolution."""
    db_path = str(tmp_path / "bc.sqlite")
    fake_tsv = (
        "#targets\tbase_image\timage_build\n"
        "bwa=0.7.17,samtools=1.10\tbusybox-bash:0.1\t0\n"
        "picard=2.23.3,bowtie=1.1.1\tbusybox-bash:0.1\t1\n"
    )

    class _FakeResponse:
        text = fake_tsv

        def raise_for_status(self):
            pass

    class _FakeSession:
        def get(self, url, **kwargs):
            return _FakeResponse()

    conn = biocontainer_db.connect(db_path)
    try:
        inserted = biocontainer_db.build_mulled_containers(
            conn, session=_FakeSession(), resolve_tags=False
        )
        assert inserted == 2
        rows = conn.execute("SELECT image_identifier FROM mulled_containers").fetchall()
        assert len(rows) == 2
        assert all(r["image_identifier"].startswith("quay.io/biocontainers/mulled-v2-") for r in rows)
        pkg_rows = conn.execute("SELECT package_name FROM mulled_packages ORDER BY package_name").fetchall()
        assert [r["package_name"] for r in pkg_rows] == ["bowtie", "bwa", "picard", "samtools"]
    finally:
        conn.close()


def test_cli_lookup_returns_db_result(db_path, capsys):
    rc = biocontainer_db.main(["--db-path", db_path, "lookup", "samtools=1.21", "--no-live"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "quay.io/biocontainers/samtools:1.21" in out
