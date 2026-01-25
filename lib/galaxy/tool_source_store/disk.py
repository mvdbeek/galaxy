"""
Disk backend for Tool Source Store.

This module provides a file-based implementation of the ToolSourceStore
that stores tool sources in a sharded directory structure.
"""

import gzip
import json
import logging
import os
import shutil
from collections.abc import Iterator
from datetime import datetime
from pathlib import Path
from typing import (
    Optional,
)

from . import (
    StoredToolSource,
    ToolSourceStore,
)
from .index import (
    ToolIndex,
    ToolIndexEntry,
)

log = logging.getLogger(__name__)


class DiskToolSourceStore(ToolSourceStore):
    """
    File-based tool source store.

    Directory structure:
    {base_path}/
        sources/
            {hash[:2]}/
                {hash[2:4]}/
                    {hash}.json
        index/
            tool_id/
                {tool_id}.json  # List of hashes
            version/
                {tool_id}/
                    {version}.json  # List of hashes
            _index.json  # Full ToolIndex
    """

    def __init__(self, base_path: str, compression: Optional[str] = None):
        """
        Initialize the disk tool source store.

        Args:
            base_path: Base directory for storing tool sources.
            compression: Optional compression type (none, gzip, lz4).
        """
        self._base_path = Path(base_path)
        self._sources_path = self._base_path / "sources"
        self._index_path = self._base_path / "index"
        self._compression = compression

        # Create directories
        self._sources_path.mkdir(parents=True, exist_ok=True)
        self._index_path.mkdir(parents=True, exist_ok=True)
        (self._index_path / "tool_id").mkdir(exist_ok=True)
        (self._index_path / "version").mkdir(exist_ok=True)

        self._cached_index: Optional[ToolIndex] = None

    def _source_path(self, hash: str) -> Path:
        """Get the path for a tool source file."""
        return self._sources_path / hash[:2] / hash[2:4] / f"{hash}.json"

    def _read_json(self, path: Path) -> Optional[dict]:
        """Read a JSON file, handling compression if enabled."""
        if not path.exists():
            return None

        try:
            if self._compression == "gzip":
                with gzip.open(path, "rt", encoding="utf-8") as f:
                    return json.load(f)
            else:
                with open(path, encoding="utf-8") as f:
                    return json.load(f)
        except Exception as e:
            log.error(f"Error reading {path}: {e}")
            return None

    def _write_json(self, path: Path, data: dict) -> None:
        """Write a JSON file, handling compression if enabled."""
        path.parent.mkdir(parents=True, exist_ok=True)

        if self._compression == "gzip":
            with gzip.open(path, "wt", encoding="utf-8") as f:
                json.dump(data, f)
        else:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f)

    def store(self, tool_source: StoredToolSource) -> str:
        """Store a tool source on disk."""
        path = self._source_path(tool_source.hash)

        if path.exists():
            return tool_source.hash

        data = {
            "hash": tool_source.hash,
            "tool_source_class": tool_source.tool_source_class,
            "raw_source": tool_source.raw_source,
            "tool_id": tool_source.tool_id,
            "tool_version": tool_source.tool_version,
            "tool_dir": tool_source.tool_dir,
            "stored_at": (tool_source.stored_at.isoformat() if tool_source.stored_at else None),
            "metadata": tool_source.metadata,
        }

        self._write_json(path, data)
        self._update_indexes(tool_source)

        return tool_source.hash

    def _update_indexes(self, tool_source: StoredToolSource) -> None:
        """Update the tool_id and version indexes."""
        if not tool_source.tool_id:
            return

        # Update tool_id index
        tool_id_path = self._index_path / "tool_id" / f"{tool_source.tool_id}.json"
        hashes = self._read_json(tool_id_path) or {"hashes": []}
        if tool_source.hash not in hashes["hashes"]:
            hashes["hashes"].append(tool_source.hash)
            self._write_json(tool_id_path, hashes)

        # Update version index
        if tool_source.tool_version:
            version_dir = self._index_path / "version" / tool_source.tool_id
            version_dir.mkdir(parents=True, exist_ok=True)
            version_path = version_dir / f"{tool_source.tool_version}.json"
            version_hashes = self._read_json(version_path) or {"hashes": []}
            if tool_source.hash not in version_hashes["hashes"]:
                version_hashes["hashes"].append(tool_source.hash)
                self._write_json(version_path, version_hashes)

    def get(self, hash: str) -> Optional[StoredToolSource]:
        """Retrieve a tool source by hash."""
        path = self._source_path(hash)
        data = self._read_json(path)

        if not data:
            return None

        return self._data_to_stored(data)

    def _data_to_stored(self, data: dict) -> StoredToolSource:
        """Convert file data to StoredToolSource."""
        stored_at = data.get("stored_at")
        if stored_at and isinstance(stored_at, str):
            stored_at = datetime.fromisoformat(stored_at)

        return StoredToolSource(
            hash=data["hash"],
            tool_source_class=data.get("tool_source_class", "XmlToolSource"),
            raw_source=data.get("raw_source", ""),
            tool_id=data.get("tool_id"),
            tool_version=data.get("tool_version"),
            tool_dir=data.get("tool_dir"),
            stored_at=stored_at,
            metadata=data.get("metadata", {}),
        )

    def exists(self, hash: str) -> bool:
        """Check if a tool source exists."""
        return self._source_path(hash).exists()

    def delete(self, hash: str) -> bool:
        """Delete a tool source by hash."""
        path = self._source_path(hash)

        if not path.exists():
            return False

        # Get the source first to remove from indexes
        data = self._read_json(path)

        # Delete the file
        path.unlink()

        # Clean up empty parent directories
        try:
            path.parent.rmdir()
            path.parent.parent.rmdir()
        except OSError:
            pass  # Directory not empty

        # Remove from indexes
        if data:
            self._remove_from_indexes(data)

        return True

    def _remove_from_indexes(self, data: dict) -> None:
        """Remove a tool source from indexes."""
        tool_id = data.get("tool_id")
        if not tool_id:
            return

        hash_value = data["hash"]

        # Remove from tool_id index
        tool_id_path = self._index_path / "tool_id" / f"{tool_id}.json"
        hashes = self._read_json(tool_id_path)
        if hashes and hash_value in hashes.get("hashes", []):
            hashes["hashes"].remove(hash_value)
            if hashes["hashes"]:
                self._write_json(tool_id_path, hashes)
            else:
                tool_id_path.unlink(missing_ok=True)

        # Remove from version index
        version = data.get("tool_version")
        if version:
            version_path = self._index_path / "version" / tool_id / f"{version}.json"
            version_hashes = self._read_json(version_path)
            if version_hashes and hash_value in version_hashes.get("hashes", []):
                version_hashes["hashes"].remove(hash_value)
                if version_hashes["hashes"]:
                    self._write_json(version_path, version_hashes)
                else:
                    version_path.unlink(missing_ok=True)

    def list_all(self) -> Iterator[str]:
        """List all stored tool source hashes."""
        for _root, _dirs, files in os.walk(self._sources_path):
            for file in files:
                if file.endswith(".json"):
                    yield file[:-5]  # Remove .json extension

    def get_by_tool_id(self, tool_id: str, version: Optional[str] = None) -> list[StoredToolSource]:
        """Get tool sources by tool ID and optional version."""
        if version:
            path = self._index_path / "version" / tool_id / f"{version}.json"
        else:
            path = self._index_path / "tool_id" / f"{tool_id}.json"

        data = self._read_json(path)
        if not data:
            return []

        sources = []
        for hash_value in data.get("hashes", []):
            source = self.get(hash_value)
            if source:
                sources.append(source)

        return sources

    def count(self) -> int:
        """Return the total number of stored tool sources."""
        count = 0
        for _ in self.list_all():
            count += 1
        return count

    def get_stats(self) -> dict:
        """Return storage statistics."""
        count = self.count()

        # Calculate total size
        total_size = 0
        for root, _dirs, files in os.walk(self._sources_path):
            for file in files:
                total_size += os.path.getsize(os.path.join(root, file))

        return {
            "count": count,
            "backend": "disk",
            "size_bytes": total_size,
            "path": str(self._base_path),
        }

    # Index operations

    def store_index(self, index: ToolIndex) -> None:
        """Store the complete tool index."""
        index_path = self._index_path / "_index.json"
        self._write_json(index_path, index.to_dict())
        self._cached_index = index

    def load_index(self) -> Optional[ToolIndex]:
        """Load the tool index."""
        if self._cached_index is not None:
            return self._cached_index

        index_path = self._index_path / "_index.json"
        data = self._read_json(index_path)

        if not data:
            return None

        self._cached_index = ToolIndex.from_dict(data)
        return self._cached_index

    def update_index_entry(self, entry: ToolIndexEntry) -> None:
        """Update a single index entry."""
        index = self.load_index()
        if index is None:
            index = ToolIndex()

        index.entries[entry.id] = entry
        index.invalidate_caches()

        # Update section mapping
        if entry.panel_section_id:
            if entry.panel_section_id not in index.by_section:
                index.by_section[entry.panel_section_id] = []
            if entry.id not in index.by_section[entry.panel_section_id]:
                index.by_section[entry.panel_section_id].append(entry.id)

        self.store_index(index)

    def invalidate_index_cache(self) -> None:
        """Invalidate the cached index."""
        self._cached_index = None

    def clear_all(self) -> None:
        """Clear all stored data (for testing)."""
        if self._sources_path.exists():
            shutil.rmtree(self._sources_path)
        if self._index_path.exists():
            shutil.rmtree(self._index_path)

        # Recreate directories
        self._sources_path.mkdir(parents=True, exist_ok=True)
        self._index_path.mkdir(parents=True, exist_ok=True)
        (self._index_path / "tool_id").mkdir(exist_ok=True)
        (self._index_path / "version").mkdir(exist_ok=True)

        self._cached_index = None
