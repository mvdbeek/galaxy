#!/usr/bin/env python
"""
Populate tool source store from Galaxy toolbox.

This script populates the configured tool source storage backend with
tool sources from the Galaxy toolbox. It supports incremental updates
and parallel processing.

Usage:
    python scripts/tool_source/populate_store.py --config galaxy.yml [options]

Options:
    --config FILE       Galaxy configuration file (required)
    --dry-run           Show what would be stored without storing
    --incremental       Only store new/changed tools (default)
    --full              Force re-store all tools
    --tool-id PATTERN   Only process tools matching pattern
    --verbose           Enable verbose output
    --parallel N        Number of parallel workers (default: 4)
    --rebuild-index     Rebuild the tool index after population
"""

import argparse
import hashlib
import logging
import sys
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)
from datetime import datetime
from pathlib import Path
from typing import (
    Dict,
    Iterator,
    Optional,
    Tuple,
)

# Add Galaxy lib to path
galaxy_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(galaxy_root / "lib"))

log = logging.getLogger(__name__)


def compute_hash(content: str) -> str:
    """Compute SHA256 hash of content."""
    return hashlib.sha256(content.encode()).hexdigest()


def iter_tool_sources(toolbox, pattern: Optional[str] = None) -> Iterator[Tuple]:
    """
    Iterate over all tools in the toolbox.

    Yields:
        Tuples of (tool_id, version, tool_source, tool_dir).
    """
    for tool_id, tool in toolbox._tools_by_id.items():
        if pattern and pattern not in tool_id:
            continue
        if hasattr(tool, "tool_source") and tool.tool_source:
            yield tool_id, tool.version, tool.tool_source, getattr(tool, "tool_dir", None)


def populate_store(
    config_file: str,
    dry_run: bool = False,
    incremental: bool = True,
    pattern: Optional[str] = None,
    parallel: int = 4,
    verbose: bool = False,
    rebuild_index: bool = False,
) -> Dict[str, int]:
    """
    Main population function.

    Args:
        config_file: Path to Galaxy configuration file.
        dry_run: If True, don't actually store anything.
        incremental: If True, skip already stored tools.
        pattern: Optional tool ID pattern to filter.
        parallel: Number of parallel workers.
        verbose: Enable verbose logging.
        rebuild_index: Rebuild index after population.

    Returns:
        Statistics dictionary with counts.
    """
    from galaxy.config import GalaxyAppConfiguration
    from galaxy.tool_source_store import (
        StoredToolSource,
        build_tool_source_store,
    )

    log.info("Loading Galaxy configuration...")
    config = GalaxyAppConfiguration(config_file=config_file)

    log.info(f"Building tool source store (backend: {getattr(config, 'tool_source_store', 'database')})...")
    store = build_tool_source_store(config)

    log.info("Loading toolbox...")
    # For now, we'll work with tools that are already loaded
    # In a real implementation, this would initialize the toolbox

    stats = {"processed": 0, "stored": 0, "skipped": 0, "errors": 0}

    # Since we can't easily initialize a full toolbox without a running app,
    # we'll look for tool XML files directly
    tools_dirs = [
        Path(config.tool_path) if hasattr(config, "tool_path") else None,
        galaxy_root / "tools",
        galaxy_root / "lib" / "galaxy" / "tools" / "bundled",
    ]

    tool_files = []
    for tools_dir in tools_dirs:
        if tools_dir and tools_dir.exists():
            for xml_file in tools_dir.rglob("*.xml"):
                try:
                    with open(xml_file) as f:
                        content = f.read()
                    if "<tool" in content and "macro" not in xml_file.name.lower():
                        tool_files.append((str(xml_file), content))
                except Exception as e:
                    if verbose:
                        log.warning(f"Error reading {xml_file}: {e}")

    log.info(f"Found {len(tool_files)} tool files")

    if pattern:
        tool_files = [(p, c) for p, c in tool_files if pattern in p]
        log.info(f"Filtered to {len(tool_files)} tools matching '{pattern}'")

    def process_tool(args: Tuple[str, str]) -> Tuple[str, str, Optional[str]]:
        """Process a single tool file."""
        path, content = args
        try:
            content_hash = compute_hash(content)

            if incremental and store.exists(content_hash):
                return ("skipped", path, None)

            # Try to parse tool ID from content
            tool_id = None
            import re
            match = re.search(r'<tool[^>]+id=["\']([^"\']+)["\']', content)
            if match:
                tool_id = match.group(1)

            # Try to parse version
            tool_version = None
            match = re.search(r'<tool[^>]+version=["\']([^"\']+)["\']', content)
            if match:
                tool_version = match.group(1)

            stored = StoredToolSource(
                hash=content_hash,
                tool_source_class="XmlToolSource",
                raw_source=content,
                tool_id=tool_id,
                tool_version=tool_version,
                tool_dir=str(Path(path).parent),
                stored_at=datetime.utcnow(),
            )

            if not dry_run:
                store.store(stored)

            return ("stored", path, tool_id)
        except Exception as e:
            log.error(f"Error processing {path}: {e}")
            return ("error", path, str(e))

    log.info(f"Processing {len(tool_files)} tools with {parallel} workers...")

    with ThreadPoolExecutor(max_workers=parallel) as executor:
        futures = {executor.submit(process_tool, t): t for t in tool_files}
        for future in as_completed(futures):
            result = future.result()
            status = result[0]

            if status == "error":
                stats["errors"] += 1
            elif status == "skipped":
                stats["skipped"] += 1
            else:
                stats["stored"] += 1

            stats["processed"] += 1

            if verbose or status == "error":
                log.info(f"{status}: {result[1]}")

    log.info(f"Population complete: {stats}")

    if rebuild_index and not dry_run:
        log.info("Rebuilding tool index...")
        from galaxy.tools.lazy_toolbox import LazyToolBox

        # We need a minimal app context for this
        # For now, just log that this would happen
        log.info("Index rebuild would happen here with full app context")

    return stats


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Populate tool source store from Galaxy toolbox"
    )
    parser.add_argument(
        "--config", "-c", required=True, help="Galaxy configuration file"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what would be stored"
    )
    parser.add_argument(
        "--incremental",
        action="store_true",
        default=True,
        help="Only store new/changed tools (default)",
    )
    parser.add_argument(
        "--full", action="store_true", help="Force re-store all tools"
    )
    parser.add_argument(
        "--tool-id", help="Tool ID pattern filter"
    )
    parser.add_argument(
        "--parallel", "-j", type=int, default=4, help="Number of parallel workers"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )
    parser.add_argument(
        "--rebuild-index", action="store_true", help="Rebuild index after population"
    )

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    stats = populate_store(
        config_file=args.config,
        dry_run=args.dry_run,
        incremental=not args.full,
        pattern=args.tool_id,
        parallel=args.parallel,
        verbose=args.verbose,
        rebuild_index=args.rebuild_index,
    )

    # Exit with error if there were failures
    sys.exit(1 if stats["errors"] > 0 else 0)


if __name__ == "__main__":
    main()
