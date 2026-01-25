"""
API endpoints for Tool Source Store management.

This module provides REST API endpoints for managing stored tool sources,
retrieving tool index information, and accessing cache statistics.
"""

import logging
from typing import (
    Optional,
)

from fastapi import Query

from galaxy.managers.context import ProvidesAppContext
from galaxy.tool_source_store.models import (
    CacheStatsResponse,
    ClearCacheResponse,
    ToolIndexEntryListResponse,
    ToolIndexEntryResponse,
    ToolIndexStatsResponse,
    ToolSourceDetailResponse,
    ToolSourceListResponse,
    ToolSourceResponse,
    ToolSourceStatsResponse,
)
from galaxy.webapps.galaxy.api import (
    depends,
    DependsOnTrans,
    Router,
)
from galaxy.webapps.galaxy.services.tool_sources import ToolSourcesService

log = logging.getLogger(__name__)

router = Router(tags=["tool_sources"])


@router.cbv
class ToolSourcesAPI:
    """API for tool source storage management."""

    service: ToolSourcesService = depends(ToolSourcesService)

    @router.get(
        "/api/tool_sources",
        summary="List stored tool sources",
        response_model=ToolSourceListResponse,
        require_admin=True,
    )
    def list_tool_sources(
        self,
        trans: ProvidesAppContext = DependsOnTrans,
        tool_id: Optional[str] = Query(None, description="Filter by tool ID"),
        limit: int = Query(100, ge=1, le=1000, description="Maximum results"),
        offset: int = Query(0, ge=0, description="Offset for pagination"),
    ) -> ToolSourceListResponse:
        """List all stored tool sources with optional filtering."""
        return self.service.list_tool_sources(trans, tool_id=tool_id, limit=limit, offset=offset)

    @router.get(
        "/api/tool_sources/stats",
        summary="Get tool source storage statistics",
        response_model=ToolSourceStatsResponse,
        require_admin=True,
    )
    def get_stats(
        self,
        trans: ProvidesAppContext = DependsOnTrans,
    ) -> ToolSourceStatsResponse:
        """Get statistics about the tool source store."""
        return self.service.get_stats(trans)

    @router.get(
        "/api/tool_sources/by_tool/{tool_id}",
        summary="Get tool sources by tool ID",
        response_model=list[ToolSourceResponse],
        require_admin=True,
    )
    def get_tool_sources_by_id(
        self,
        tool_id: str,
        trans: ProvidesAppContext = DependsOnTrans,
        version: Optional[str] = Query(None, description="Filter by version"),
    ) -> list[ToolSourceResponse]:
        """Retrieve all tool sources for a given tool ID."""
        return self.service.get_tool_sources_by_id(trans, tool_id, version)

    @router.get(
        "/api/tool_sources/{hash}",
        summary="Get a specific tool source by hash",
        response_model=ToolSourceDetailResponse,
        require_admin=True,
    )
    def get_tool_source(
        self,
        hash: str,
        trans: ProvidesAppContext = DependsOnTrans,
    ) -> ToolSourceDetailResponse:
        """Retrieve a tool source by its content hash."""
        return self.service.get_tool_source(trans, hash)


@router.cbv
class ToolIndexAPI:
    """API for tool index management."""

    service: ToolSourcesService = depends(ToolSourcesService)

    @router.get(
        "/api/tool_index",
        summary="List tool index entries",
        response_model=ToolIndexEntryListResponse,
    )
    def list_index_entries(
        self,
        trans: ProvidesAppContext = DependsOnTrans,
        section_id: Optional[str] = Query(None, description="Filter by section"),
        include_hidden: bool = Query(False, description="Include hidden tools"),
        limit: int = Query(1000, ge=1, le=10000, description="Maximum results"),
    ) -> ToolIndexEntryListResponse:
        """List all tool index entries."""
        return self.service.list_index_entries(trans, section_id=section_id, include_hidden=include_hidden, limit=limit)

    @router.get(
        "/api/tool_index/stats",
        summary="Get tool index statistics",
        response_model=ToolIndexStatsResponse,
        require_admin=True,
    )
    def get_index_stats(
        self,
        trans: ProvidesAppContext = DependsOnTrans,
    ) -> ToolIndexStatsResponse:
        """Get statistics about the tool index."""
        return self.service.get_index_stats(trans)

    # Static-suffix routes must precede `/{tool_id}` to avoid path shadowing.
    @router.get(
        "/api/tool_index/search",
        summary="Search tool index",
        response_model=list[ToolIndexEntryResponse],
    )
    def search_index(
        self,
        trans: ProvidesAppContext = DependsOnTrans,
        q: str = Query(..., description="Search query"),
        limit: int = Query(50, ge=1, le=500, description="Maximum results"),
    ) -> list[ToolIndexEntryResponse]:
        """Search tool index by text."""
        return self.service.search_index(trans, q, limit)

    @router.get(
        "/api/tool_index/{tool_id}",
        summary="Get tool index entry by ID",
        response_model=ToolIndexEntryResponse,
    )
    def get_index_entry(
        self,
        tool_id: str,
        trans: ProvidesAppContext = DependsOnTrans,
    ) -> ToolIndexEntryResponse:
        """Get a specific tool index entry."""
        return self.service.get_index_entry(trans, tool_id)


@router.cbv
class ToolCacheAPI:
    """API for tool cache management."""

    service: ToolSourcesService = depends(ToolSourcesService)

    @router.get(
        "/api/tool_cache/stats",
        summary="Get cache statistics",
        response_model=CacheStatsResponse,
        require_admin=True,
    )
    def get_cache_stats(
        self,
        trans: ProvidesAppContext = DependsOnTrans,
    ) -> CacheStatsResponse:
        """Get statistics about the tool cache."""
        return self.service.get_cache_stats(trans)

    @router.post(
        "/api/tool_cache/clear",
        summary="Clear tool object cache",
        response_model=ClearCacheResponse,
        require_admin=True,
    )
    def clear_cache(
        self,
        trans: ProvidesAppContext = DependsOnTrans,
    ) -> ClearCacheResponse:
        """Clear the Tool object LRU cache."""
        self.service.clear_tool_cache(trans)
        return ClearCacheResponse(status="cleared")
