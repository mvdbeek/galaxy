"""
Redis backend for Tool Source Store.

This module provides a Redis-backed implementation of the ToolSourceStore
for high-performance tool source caching and storage.
"""

import json
import logging
from collections.abc import Iterator
from datetime import datetime
from typing import (
    cast,
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


class RedisToolSourceStore(ToolSourceStore):
    """
    Redis-backed tool source store.

    Key structure:
    - tool_source:{hash} -> JSON blob of StoredToolSource
    - tool_source:index:tool_id:{tool_id} -> Set of hashes
    - tool_source:index:version:{tool_id}:{version} -> Set of hashes
    - tool_source:all -> Set of all hashes
    - tool_index:data -> JSON blob of ToolIndex
    - tool_index:entry:{tool_id} -> JSON of ToolIndexEntry
    - tool_index:all -> Set of all tool_ids
    - tool_index:section:{section_id} -> Set of tool_ids in section
    - tool_index:meta -> JSON with version, built_at
    """

    PREFIX = "tool_source"
    INDEX_PREFIX = "tool_index"

    def __init__(self, redis_url: str, ttl: Optional[int] = None):
        """
        Initialize the Redis tool source store.

        Args:
            redis_url: Redis connection URL.
            ttl: Optional TTL in seconds for stored entries.
        """
        try:
            # Optional dependency: only required when the redis backend is selected.
            from redis import Redis
        except ImportError:
            raise ImportError("redis package is required for RedisToolSourceStore")

        self._redis = Redis.from_url(redis_url, decode_responses=True)
        self._ttl = ttl
        self._cached_index: Optional[ToolIndex] = None

    def store(self, tool_source: StoredToolSource) -> str:
        """Store a tool source in Redis."""
        key = f"{self.PREFIX}:{tool_source.hash}"

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

        pipe = self._redis.pipeline()

        if self._ttl:
            pipe.setex(key, self._ttl, json.dumps(data))
        else:
            pipe.set(key, json.dumps(data))

        # Add to all hashes set
        pipe.sadd(f"{self.PREFIX}:all", tool_source.hash)

        # Index by tool_id
        if tool_source.tool_id:
            pipe.sadd(f"{self.PREFIX}:index:tool_id:{tool_source.tool_id}", tool_source.hash)
            if tool_source.tool_version:
                pipe.sadd(
                    f"{self.PREFIX}:index:version:{tool_source.tool_id}:{tool_source.tool_version}",
                    tool_source.hash,
                )

        pipe.execute()
        return tool_source.hash

    def get(self, hash: str) -> Optional[StoredToolSource]:
        """Retrieve a tool source by hash."""
        key = f"{self.PREFIX}:{hash}"
        data = cast(Optional[str], self._redis.get(key))

        if not data:
            return None

        return self._data_to_stored(json.loads(data))

    def _data_to_stored(self, data: dict) -> StoredToolSource:
        """Convert Redis data to StoredToolSource."""
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
        return cast(int, self._redis.exists(f"{self.PREFIX}:{hash}")) > 0

    def delete(self, hash: str) -> bool:
        """Delete a tool source by hash."""
        key = f"{self.PREFIX}:{hash}"

        # Get the source first to remove from indexes
        data = cast(Optional[str], self._redis.get(key))
        if not data:
            return False

        source_data = json.loads(data)

        pipe = self._redis.pipeline()
        pipe.delete(key)
        pipe.srem(f"{self.PREFIX}:all", hash)

        tool_id = source_data.get("tool_id")
        if tool_id:
            pipe.srem(f"{self.PREFIX}:index:tool_id:{tool_id}", hash)
            version = source_data.get("tool_version")
            if version:
                pipe.srem(f"{self.PREFIX}:index:version:{tool_id}:{version}", hash)

        pipe.execute()
        return True

    def list_all(self) -> Iterator[str]:
        """List all stored tool source hashes."""
        hashes = cast(set, self._redis.smembers(f"{self.PREFIX}:all"))
        yield from hashes

    def get_by_tool_id(self, tool_id: str, version: Optional[str] = None) -> list[StoredToolSource]:
        """Get tool sources by tool ID and optional version."""
        if version:
            key = f"{self.PREFIX}:index:version:{tool_id}:{version}"
        else:
            key = f"{self.PREFIX}:index:tool_id:{tool_id}"

        hashes = cast(set, self._redis.smembers(key))
        sources = []

        for hash_value in hashes:
            source = self.get(hash_value)
            if source:
                sources.append(source)

        return sources

    def count(self) -> int:
        """Return the total number of stored tool sources."""
        return cast(int, self._redis.scard(f"{self.PREFIX}:all")) or 0

    def get_stats(self) -> dict:
        """Return storage statistics."""
        return {
            "count": self.count(),
            "backend": "redis",
        }

    # Index operations

    def store_index(self, index: ToolIndex) -> None:
        """Store the complete tool index."""
        pipe = self._redis.pipeline()

        # Store the full index as JSON
        index_data = index.to_dict()
        pipe.set(f"{self.INDEX_PREFIX}:data", json.dumps(index_data))

        # Store individual entries for quick access
        for tool_id, entry in index.entries.items():
            pipe.set(f"{self.INDEX_PREFIX}:entry:{tool_id}", json.dumps(entry.to_dict()))
            pipe.sadd(f"{self.INDEX_PREFIX}:all", tool_id)

            if entry.panel_section_id:
                pipe.sadd(f"{self.INDEX_PREFIX}:section:{entry.panel_section_id}", tool_id)

        # Store metadata
        meta = {
            "version": index.version,
            "built_at": index.built_at.isoformat() if index.built_at else None,
        }
        pipe.set(f"{self.INDEX_PREFIX}:meta", json.dumps(meta))

        pipe.execute()
        self._cached_index = index

    def load_index(self) -> Optional[ToolIndex]:
        """Load the tool index."""
        if self._cached_index is not None:
            return self._cached_index

        # Try to load the full index first
        data = cast(Optional[str], self._redis.get(f"{self.INDEX_PREFIX}:data"))
        if data:
            self._cached_index = ToolIndex.from_dict(json.loads(data))
            return self._cached_index

        # Fall back to building from individual entries
        tool_ids = cast(set, self._redis.smembers(f"{self.INDEX_PREFIX}:all"))
        if not tool_ids:
            return None

        entries = {}
        for tool_id in tool_ids:
            entry_data = cast(Optional[str], self._redis.get(f"{self.INDEX_PREFIX}:entry:{tool_id}"))
            if entry_data:
                entries[tool_id] = ToolIndexEntry.from_dict(json.loads(entry_data))

        # Build section mapping
        by_section = {}
        for key in self._redis.scan_iter(f"{self.INDEX_PREFIX}:section:*"):
            section_id = key.split(":")[-1]
            by_section[section_id] = list(cast(set, self._redis.smembers(key)))

        # Get metadata
        meta_data = cast(Optional[str], self._redis.get(f"{self.INDEX_PREFIX}:meta"))
        meta = json.loads(meta_data) if meta_data else {}

        built_at = meta.get("built_at")
        if built_at and isinstance(built_at, str):
            built_at = datetime.fromisoformat(built_at)

        self._cached_index = ToolIndex(
            entries=entries,
            by_section=by_section,
            version=meta.get("version", ""),
            built_at=built_at,
        )
        return self._cached_index

    def update_index_entry(self, entry: ToolIndexEntry) -> None:
        """Update a single index entry."""
        pipe = self._redis.pipeline()

        pipe.set(f"{self.INDEX_PREFIX}:entry:{entry.id}", json.dumps(entry.to_dict()))
        pipe.sadd(f"{self.INDEX_PREFIX}:all", entry.id)

        if entry.panel_section_id:
            pipe.sadd(f"{self.INDEX_PREFIX}:section:{entry.panel_section_id}", entry.id)

        pipe.execute()

        # Invalidate cached index
        self._cached_index = None

    def invalidate_index_cache(self) -> None:
        """Invalidate the cached index."""
        self._cached_index = None

    def clear_all(self) -> None:
        """Clear all stored data (for testing)."""
        # Get all keys matching our prefixes
        for prefix in [self.PREFIX, self.INDEX_PREFIX]:
            for key in self._redis.scan_iter(f"{prefix}:*"):
                self._redis.delete(key)
        self._cached_index = None
