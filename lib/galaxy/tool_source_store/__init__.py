"""
Tool Source Store - Pluggable storage backends for Galaxy tool sources.

This module provides a configurable, pluggable tool source storage system
that enables storing and retrieving tool sources from multiple backends
(database, Redis, disk).
"""

from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime
from collections.abc import Iterator
from typing import (
    TYPE_CHECKING,
    Optional,
)

if TYPE_CHECKING:
    from galaxy.config import GalaxyAppConfiguration

    from .index import ToolIndex


@dataclass
class StoredToolSource:
    """Representation of a stored tool source."""

    hash: str  # Content hash (SHA256)
    tool_source_class: str  # XmlToolSource, YamlToolSource, etc.
    raw_source: str  # Serialized tool source string
    tool_id: Optional[str] = None  # Tool ID if known
    tool_version: Optional[str] = None  # Tool version if known
    tool_dir: Optional[str] = None  # Original tool directory
    stored_at: Optional[datetime] = None
    metadata: Optional[dict] = field(default_factory=dict)


class ToolSourceStore(ABC):
    """Abstract base class for tool source storage backends."""

    @abstractmethod
    def store(self, tool_source: StoredToolSource) -> str:
        """
        Store a tool source.

        Args:
            tool_source: The tool source to store.

        Returns:
            The storage key (hash).
        """

    @abstractmethod
    def get(self, hash: str) -> Optional[StoredToolSource]:
        """
        Retrieve a tool source by hash.

        Args:
            hash: The content hash of the tool source.

        Returns:
            The stored tool source, or None if not found.
        """

    @abstractmethod
    def exists(self, hash: str) -> bool:
        """
        Check if a tool source exists.

        Args:
            hash: The content hash to check.

        Returns:
            True if the tool source exists.
        """

    @abstractmethod
    def delete(self, hash: str) -> bool:
        """
        Delete a tool source by hash.

        Args:
            hash: The content hash of the tool source to delete.

        Returns:
            True if deleted, False if not found.
        """

    @abstractmethod
    def list_all(self) -> Iterator[str]:
        """
        List all stored tool source hashes.

        Yields:
            Content hashes of all stored tool sources.
        """

    @abstractmethod
    def get_by_tool_id(
        self, tool_id: str, version: Optional[str] = None
    ) -> list[StoredToolSource]:
        """
        Get tool sources by tool ID and optional version.

        Args:
            tool_id: The tool ID to search for.
            version: Optional version filter.

        Returns:
            List of matching tool sources.
        """

    @abstractmethod
    def count(self) -> int:
        """Return the total number of stored tool sources."""

    def get_stats(self) -> dict:
        """Return storage statistics."""
        return {"count": self.count()}

    # Index operations

    @abstractmethod
    def store_index(self, index: "ToolIndex") -> None:
        """
        Store the complete tool index.

        Args:
            index: The tool index to store.
        """

    @abstractmethod
    def load_index(self) -> Optional["ToolIndex"]:
        """
        Load the tool index.

        Returns:
            The tool index, or None if not found.
        """

    @abstractmethod
    def update_index_entry(self, entry: "ToolIndexEntry") -> None:
        """
        Update a single index entry.

        Args:
            entry: The index entry to update.
        """


class ConfigurationError(Exception):
    """Raised when there's a configuration error."""


def build_tool_source_store(config: "GalaxyAppConfiguration") -> ToolSourceStore:
    """
    Build a tool source store based on configuration.

    Args:
        config: Galaxy application configuration.

    Returns:
        Configured ToolSourceStore instance.

    Raises:
        ConfigurationError: If the backend is unknown or misconfigured.
    """
    backend = getattr(config, "tool_source_store", "database")

    if backend == "database":
        from .database import DatabaseToolSourceStore

        return DatabaseToolSourceStore(config)

    elif backend == "redis":
        from .redis import RedisToolSourceStore

        redis_url = getattr(config, "tool_source_redis_url", None)
        if not redis_url:
            raise ConfigurationError("tool_source_redis_url required for redis backend")
        ttl = getattr(config, "tool_source_redis_ttl", None)
        return RedisToolSourceStore(redis_url, ttl=ttl)

    elif backend == "disk":
        from .disk import DiskToolSourceStore

        disk_path = getattr(config, "tool_source_disk_path", None)
        if not disk_path:
            raise ConfigurationError("tool_source_disk_path required for disk backend")
        return DiskToolSourceStore(disk_path)

    else:
        raise ConfigurationError(f"Unknown tool source store backend: {backend}")


# Re-export key classes
from .index import (  # noqa: E402
    ToolIndex,
    ToolIndexEntry,
)

__all__ = [
    "StoredToolSource",
    "ToolSourceStore",
    "ToolIndex",
    "ToolIndexEntry",
    "build_tool_source_store",
    "ConfigurationError",
]
