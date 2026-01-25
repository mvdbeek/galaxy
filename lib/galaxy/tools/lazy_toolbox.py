"""
Lazy ToolBox - On-demand tool loading with LRU caching.

This module provides a LazyToolBox that keeps only a lightweight index
in memory and loads full Tool objects on-demand with LRU eviction.
"""

import hashlib
import logging
import threading
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Optional,
)

from cachetools import LRUCache

from galaxy.tool_source_store import (
    StoredToolSource,
    ToolSourceStore,
)
from galaxy.tool_source_store.api_cache import ToolAPICache
from galaxy.tool_source_store.index import (
    ToolIndex,
    ToolIndexEntry,
)

if TYPE_CHECKING:
    from galaxy.app import StructuredApp
    from galaxy.tools import Tool

log = logging.getLogger(__name__)


class LazyToolBox:
    """
    ToolBox that loads tools on-demand from the tool source store.

    Keeps a lightweight index in memory for API responses,
    but only loads full Tool objects when needed for execution
    or form building.
    """

    def __init__(
        self,
        app: "StructuredApp",
        tool_source_store: ToolSourceStore,
        cache_size: int = 500,
        api_cache_ttl: int = 300,
    ):
        """
        Initialize the lazy toolbox.

        Args:
            app: Galaxy application instance.
            tool_source_store: The tool source store to load from.
            cache_size: Maximum number of Tool objects to cache.
            api_cache_ttl: TTL for API cache in seconds.
        """
        self._app = app
        self._store = tool_source_store
        self._index: Optional[ToolIndex] = None
        self._tool_cache: LRUCache = LRUCache(maxsize=cache_size)
        self._cache_lock = threading.RLock()
        self._api_cache = ToolAPICache(ttl_seconds=api_cache_ttl)

        # Load index on startup
        self._load_index()

    def _load_index(self) -> None:
        """Load the tool index from store."""
        log.debug("Loading tool index from store...")
        self._index = self._store.load_index()
        if self._index is None:
            log.info("No tool index found, will build on first population")
            self._index = ToolIndex()
        else:
            log.info(f"Loaded tool index with {len(self._index.entries)} entries")
            # Refresh API cache
            self._api_cache.refresh(self._index)

    def rebuild_index(self) -> ToolIndex:
        """
        Rebuild index from all stored tool sources.

        Returns:
            The rebuilt index.
        """
        log.info("Rebuilding tool index from stored sources...")
        entries: Dict[str, ToolIndexEntry] = {}
        by_section: Dict[str, List[str]] = {}

        for source_hash in self._store.list_all():
            stored = self._store.get(source_hash)
            if stored:
                try:
                    entry = self._build_index_entry(stored)
                    entries[entry.id] = entry
                    if entry.panel_section_id:
                        if entry.panel_section_id not in by_section:
                            by_section[entry.panel_section_id] = []
                        by_section[entry.panel_section_id].append(entry.id)
                except Exception as e:
                    log.error(f"Error building index entry for {source_hash}: {e}")

        self._index = ToolIndex(
            entries=entries,
            by_section=by_section,
            version=hashlib.md5(str(sorted(entries.keys())).encode()).hexdigest()[:8],
            built_at=datetime.utcnow(),
        )
        self._store.store_index(self._index)
        self._api_cache.refresh(self._index)

        log.info(f"Rebuilt tool index with {len(entries)} entries")
        return self._index

    def _build_index_entry(self, stored: StoredToolSource) -> ToolIndexEntry:
        """
        Build index entry from stored source (without full Tool creation).

        This uses lightweight parsing to extract only metadata.
        """
        from galaxy.tool_util.parser import get_tool_source

        tool_source = get_tool_source(
            raw_tool_source=stored.raw_source,
            tool_source_class=stored.tool_source_class,
        )

        # Extract requirements
        requirements = []
        try:
            for req in tool_source.parse_requirements():
                requirements.append(
                    {
                        "name": req.name,
                        "version": req.version,
                        "type": req.type,
                    }
                )
        except Exception:
            pass

        # Extract container requirements
        container_requirements = []
        try:
            for container in tool_source.parse_containers():
                container_requirements.append(
                    {
                        "type": container.type,
                        "identifier": container.identifier,
                    }
                )
        except Exception:
            pass

        # Count tests
        test_count = 0
        try:
            tests = tool_source.parse_tests_to_dict()
            test_count = len(tests.get("tests", []))
        except Exception:
            pass

        # Parse tool shed info
        tool_shed = None
        repository_name = None
        repository_owner = None
        changeset_revision = None
        is_local = True

        try:
            # Check if this came from a tool shed
            if stored.tool_dir:
                # Look for shed metadata in tool_dir path
                if "shed_tools" in stored.tool_dir:
                    is_local = False
        except Exception:
            pass

        return ToolIndexEntry(
            id=tool_source.parse_id() or stored.tool_id or "",
            uuid=str(tool_source.parse_uuid()) if tool_source.parse_uuid() else None,
            version=tool_source.parse_version(),
            name=tool_source.parse_name() or "",
            description=tool_source.parse_description() or "",
            labels=list(tool_source.parse_xrefs()) if hasattr(tool_source, 'parse_xrefs') else [],
            edam_operations=list(tool_source.parse_edam_operations()) if hasattr(tool_source, 'parse_edam_operations') else [],
            edam_topics=list(tool_source.parse_edam_topics()) if hasattr(tool_source, 'parse_edam_topics') else [],
            source_hash=stored.hash,
            source_class=stored.tool_source_class,
            hidden=tool_source.parse_hidden() if hasattr(tool_source, 'parse_hidden') else False,
            test_count=test_count,
            requirements=requirements,
            container_requirements=container_requirements,
            tool_shed=tool_shed,
            repository_name=repository_name,
            repository_owner=repository_owner,
            changeset_revision=changeset_revision,
            is_local=is_local,
            indexed_at=datetime.utcnow(),
        )

    # === API Methods (use index, no Tool loading) ===

    def list_tools(
        self,
        section_id: Optional[str] = None,
        include_hidden: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        List all tools - used by /api/tools.

        Returns lightweight dicts from index, no Tool loading.
        """
        if self._index is None:
            return []
        entries = self._index.list_all(section_id, include_hidden)
        return [entry.to_api_dict() for entry in entries]

    def search_tools(self, query: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Search tools by text - fast, uses index only."""
        if self._index is None:
            return []
        entries = self._index.search(query, limit)
        return [entry.to_api_dict() for entry in entries]

    def get_tool_info(self, tool_id: str) -> Optional[Dict[str, Any]]:
        """Get tool info - uses index, no Tool loading."""
        if self._index is None:
            return None
        entry = self._index.get(tool_id)
        return entry.to_api_dict(detail=True) if entry else None

    def get_tests_summary(self) -> Dict[str, Dict[str, Dict]]:
        """Get tests summary - uses index."""
        if self._index is None:
            return {}
        return self._index.get_tests_summary()

    def get_all_requirements(self) -> List[Dict[str, Any]]:
        """Get all requirements - uses index."""
        if self._index is None:
            return []
        return self._index.get_all_requirements()

    def get_panel_views(self) -> Dict[str, Dict]:
        """Get panel views - uses index."""
        if self._index is None:
            return {}
        return self._index.get_panel_views()

    def get_requirements_summary(
        self, index_by: str = "requirements"
    ) -> List[Dict[str, Any]]:
        """Get requirements summary for dependency endpoints."""
        if self._index is None:
            return []
        return self._index.get_requirements_summary(index_by)

    # === Tool Loading Methods (load from store on-demand) ===

    def get_tool(
        self, tool_id: str, version: Optional[str] = None
    ) -> Optional["Tool"]:
        """
        Get a full Tool object - loads from store if not cached.

        Used for tool execution, form building, etc.

        Args:
            tool_id: The tool ID.
            version: Optional version (None = latest).

        Returns:
            The Tool object, or None if not found.
        """
        cache_key = f"{tool_id}:{version or 'latest'}"

        with self._cache_lock:
            if cache_key in self._tool_cache:
                return self._tool_cache[cache_key]

        # Get source hash from index
        if self._index is None:
            return None

        entry = self._index.get(tool_id)
        if not entry:
            return None

        # Load source from store
        stored = self._store.get(entry.source_hash)
        if not stored:
            log.warning(
                f"Tool source not found for {tool_id} (hash: {entry.source_hash})"
            )
            return None

        # Create Tool object
        try:
            tool = self._create_tool_from_source(stored)
        except Exception as e:
            log.error(f"Error creating tool {tool_id}: {e}")
            return None

        with self._cache_lock:
            self._tool_cache[cache_key] = tool

        return tool

    def _create_tool_from_source(self, stored: StoredToolSource) -> "Tool":
        """Create a Tool object from stored source."""
        from galaxy.tool_util.parser import get_tool_source
        from galaxy.tools import create_tool_from_source

        tool_source = get_tool_source(
            raw_tool_source=stored.raw_source,
            tool_source_class=stored.tool_source_class,
        )

        return create_tool_from_source(
            self._app,
            tool_source,
            tool_dir=stored.tool_dir,
        )

    # === Index Management ===

    @property
    def index(self) -> Optional[ToolIndex]:
        """Get the tool index."""
        return self._index

    def add_tool_source(
        self, stored: StoredToolSource, update_index: bool = True
    ) -> str:
        """
        Add a tool source to the store.

        Args:
            stored: The tool source to store.
            update_index: Whether to update the index.

        Returns:
            The storage hash.
        """
        hash_value = self._store.store(stored)

        if update_index:
            try:
                entry = self._build_index_entry(stored)
                self._store.update_index_entry(entry)
                if self._index:
                    self._index.entries[entry.id] = entry
                    self._index.invalidate_caches()
                    self._api_cache.refresh(self._index)
            except Exception as e:
                log.error(f"Error updating index for {stored.tool_id}: {e}")

        return hash_value

    # === Cache Management ===

    @property
    def api_cache(self) -> ToolAPICache:
        """Get the API cache."""
        return self._api_cache

    def cache_stats(self) -> Dict[str, Any]:
        """Return cache statistics."""
        return {
            "tool_cache_size": len(self._tool_cache),
            "tool_cache_maxsize": self._tool_cache.maxsize,
            "index_size": len(self._index.entries) if self._index else 0,
            "index_memory_estimate": (
                self._index.memory_size_estimate() if self._index else 0
            ),
            "api_cache": self._api_cache.get_stats(),
        }

    def clear_cache(self) -> None:
        """Clear the tool object cache."""
        with self._cache_lock:
            self._tool_cache.clear()

    def evict_tool(self, tool_id: str) -> None:
        """Evict a specific tool from cache."""
        with self._cache_lock:
            keys_to_remove = [
                k for k in self._tool_cache if k.startswith(f"{tool_id}:")
            ]
            for key in keys_to_remove:
                del self._tool_cache[key]

    def refresh_api_cache(self) -> None:
        """Refresh the API cache."""
        if self._index:
            self._api_cache.refresh(self._index)
