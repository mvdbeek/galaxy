"""
Service layer for Tool Source Store API.

This module provides the business logic for tool source storage
operations, tool index management, and cache statistics.
"""

import logging
from typing import (
    List,
    Optional,
)

from galaxy.exceptions import ObjectNotFound
from galaxy.managers.context import ProvidesAppContext
from galaxy.tool_source_store import (
    StoredToolSource,
    ToolSourceStore,
)
from galaxy.tool_source_store.index import (
    ToolIndex,
    ToolIndexEntry,
)
from galaxy.tool_source_store.models import (
    CacheStatsResponse,
    ToolIndexEntryResponse,
    ToolIndexStatsResponse,
    ToolSourceDetailResponse,
    ToolSourceListResponse,
    ToolSourceResponse,
    ToolSourceStatsResponse,
)

log = logging.getLogger(__name__)


class ToolSourcesService:
    """Service for tool source storage operations."""

    def _get_store(self, trans: ProvidesAppContext) -> ToolSourceStore:
        """Get the tool source store from the app."""
        if hasattr(trans.app, "tool_source_store"):
            return trans.app.tool_source_store
        raise ObjectNotFound("Tool source store not configured")

    def _get_index(self, trans: ProvidesAppContext) -> Optional[ToolIndex]:
        """Get the tool index."""
        store = self._get_store(trans)
        return store.load_index()

    def _get_lazy_toolbox(self, trans: ProvidesAppContext):
        """Get the lazy toolbox if available."""
        if hasattr(trans.app, "lazy_toolbox"):
            return trans.app.lazy_toolbox
        return None

    # Tool Source operations

    def list_tool_sources(
        self,
        trans: ProvidesAppContext,
        tool_id: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> ToolSourceListResponse:
        """List stored tool sources."""
        store = self._get_store(trans)

        items = []
        total = 0

        if tool_id:
            sources = store.get_by_tool_id(tool_id)
            total = len(sources)
            for source in sources[offset : offset + limit]:
                items.append(self._source_to_response(source))
        else:
            # List all with pagination
            all_hashes = list(store.list_all())
            total = len(all_hashes)
            for hash_value in all_hashes[offset : offset + limit]:
                source = store.get(hash_value)
                if source:
                    items.append(self._source_to_response(source))

        return ToolSourceListResponse(total_count=total, items=items)

    def get_tool_source(
        self, trans: ProvidesAppContext, hash: str
    ) -> ToolSourceDetailResponse:
        """Get a tool source by hash."""
        store = self._get_store(trans)
        source = store.get(hash)
        if not source:
            raise ObjectNotFound(f"Tool source not found: {hash}")
        return self._source_to_detail_response(source)

    def get_tool_sources_by_id(
        self,
        trans: ProvidesAppContext,
        tool_id: str,
        version: Optional[str] = None,
    ) -> List[ToolSourceResponse]:
        """Get tool sources by tool ID."""
        store = self._get_store(trans)
        sources = store.get_by_tool_id(tool_id, version)
        return [self._source_to_response(s) for s in sources]

    def get_stats(self, trans: ProvidesAppContext) -> ToolSourceStatsResponse:
        """Get storage statistics."""
        store = self._get_store(trans)
        stats = store.get_stats()
        return ToolSourceStatsResponse(
            backend=stats.get("backend", "unknown"),
            count=stats.get("count", 0),
            size_bytes=stats.get("size_bytes"),
        )

    def _source_to_response(self, source: StoredToolSource) -> ToolSourceResponse:
        """Convert StoredToolSource to API response."""
        return ToolSourceResponse(
            hash=source.hash,
            tool_source_class=source.tool_source_class,
            tool_id=source.tool_id,
            tool_version=source.tool_version,
            tool_dir=source.tool_dir,
            stored_at=source.stored_at,
        )

    def _source_to_detail_response(
        self, source: StoredToolSource
    ) -> ToolSourceDetailResponse:
        """Convert StoredToolSource to detailed API response."""
        return ToolSourceDetailResponse(
            hash=source.hash,
            tool_source_class=source.tool_source_class,
            tool_id=source.tool_id,
            tool_version=source.tool_version,
            tool_dir=source.tool_dir,
            stored_at=source.stored_at,
            raw_source=source.raw_source,
            metadata=source.metadata,
        )

    # Tool Index operations

    def list_index_entries(
        self,
        trans: ProvidesAppContext,
        section_id: Optional[str] = None,
        include_hidden: bool = False,
        limit: int = 1000,
    ) -> List[ToolIndexEntryResponse]:
        """List tool index entries."""
        index = self._get_index(trans)
        if not index:
            return []

        entries = index.list_all(section_id=section_id, include_hidden=include_hidden)
        return [self._entry_to_response(e) for e in entries[:limit]]

    def get_index_entry(
        self, trans: ProvidesAppContext, tool_id: str
    ) -> ToolIndexEntryResponse:
        """Get a specific tool index entry."""
        index = self._get_index(trans)
        if not index:
            raise ObjectNotFound("Tool index not available")

        entry = index.get(tool_id)
        if not entry:
            raise ObjectNotFound(f"Tool not found in index: {tool_id}")

        return self._entry_to_response(entry)

    def get_index_stats(self, trans: ProvidesAppContext) -> ToolIndexStatsResponse:
        """Get tool index statistics."""
        index = self._get_index(trans)
        if not index:
            return ToolIndexStatsResponse(
                index_size=0,
                memory_estimate_bytes=0,
                version="",
                built_at=None,
            )

        return ToolIndexStatsResponse(
            index_size=len(index.entries),
            memory_estimate_bytes=index.memory_size_estimate(),
            version=index.version,
            built_at=index.built_at,
        )

    def search_index(
        self, trans: ProvidesAppContext, query: str, limit: int = 50
    ) -> List[ToolIndexEntryResponse]:
        """Search tool index."""
        index = self._get_index(trans)
        if not index:
            return []

        entries = index.search(query, limit=limit)
        return [self._entry_to_response(e) for e in entries]

    def _entry_to_response(self, entry: ToolIndexEntry) -> ToolIndexEntryResponse:
        """Convert ToolIndexEntry to API response."""
        return ToolIndexEntryResponse(
            id=entry.id,
            uuid=entry.uuid,
            version=entry.version,
            name=entry.name,
            description=entry.description,
            panel_section_id=entry.panel_section_id,
            panel_section_name=entry.panel_section_name,
            labels=entry.labels,
            edam_operations=entry.edam_operations,
            edam_topics=entry.edam_topics,
            hidden=entry.hidden,
            test_count=entry.test_count,
        )

    # Cache operations

    def get_cache_stats(self, trans: ProvidesAppContext) -> CacheStatsResponse:
        """Get cache statistics."""
        lazy_toolbox = self._get_lazy_toolbox(trans)
        if lazy_toolbox:
            stats = lazy_toolbox.cache_stats()
            return CacheStatsResponse(
                tool_cache_size=stats.get("tool_cache_size", 0),
                tool_cache_maxsize=stats.get("tool_cache_maxsize", 0),
                index_size=stats.get("index_size", 0),
                index_memory_estimate=stats.get("index_memory_estimate", 0),
            )
        return CacheStatsResponse(
            tool_cache_size=0,
            tool_cache_maxsize=0,
            index_size=0,
            index_memory_estimate=0,
        )

    def clear_tool_cache(self, trans: ProvidesAppContext) -> None:
        """Clear the Tool object cache."""
        lazy_toolbox = self._get_lazy_toolbox(trans)
        if lazy_toolbox:
            lazy_toolbox.clear_cache()
