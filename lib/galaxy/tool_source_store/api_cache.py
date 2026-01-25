"""
API Cache for Tool Source Store.

This module provides pre-computed, gzip-compressed caching for common
API responses to minimize CPU and memory usage for batch endpoints.
"""

import gzip
import json
import logging
from datetime import (
    datetime,
    timedelta,
)
from typing import (
    Any,
    Optional,
)

from .index import ToolIndex

log = logging.getLogger(__name__)


class ToolAPICache:
    """
    Cache for pre-computed API responses.

    Stores gzip-compressed JSON for common API queries to avoid
    recomputing responses on every request.
    """

    CACHE_KEYS = {
        # /api/tools variants
        "tools_list": "/api/tools",
        "tools_list_detailed": "/api/tools?detailed=true",
        "tool_panel": "/api/tools?in_panel=true",
        # Other batch endpoints
        "tests_summary": "/api/tools/tests_summary",
        "all_requirements": "/api/tools/all_requirements",
        "panel_views": "/api/tool_panels",
        "dependency_toolbox": "/api/dependency_resolvers/toolbox",
    }

    def __init__(self, ttl_seconds: int = 300):
        """
        Initialize the API cache.

        Args:
            ttl_seconds: Time-to-live for cached responses in seconds.
        """
        self._ttl = timedelta(seconds=ttl_seconds)
        self._cache: dict[str, tuple[bytes, datetime]] = {}

    def get_tools_list(self, detailed: bool = False) -> Optional[bytes]:
        """
        Get cached tools list response (gzip compressed).

        Args:
            detailed: Whether to get the detailed version.

        Returns:
            Gzip-compressed JSON bytes, or None if not cached.
        """
        key = "tools_list_detailed" if detailed else "tools_list"
        return self._get_cached(key)

    def get_tests_summary(self) -> Optional[bytes]:
        """Get cached tests summary response."""
        return self._get_cached("tests_summary")

    def get_all_requirements(self) -> Optional[bytes]:
        """Get cached all requirements response."""
        return self._get_cached("all_requirements")

    def get_panel_views(self) -> Optional[bytes]:
        """Get cached panel views response."""
        return self._get_cached("panel_views")

    def get_dependency_toolbox(self) -> Optional[bytes]:
        """Get cached dependency toolbox response."""
        return self._get_cached("dependency_toolbox")

    def _get_cached(self, key: str) -> Optional[bytes]:
        """Get a cached response by key."""
        if key in self._cache:
            data, expires_at = self._cache[key]
            if datetime.utcnow() < expires_at:
                return data
            del self._cache[key]
        return None

    def _set_cached(self, key: str, data: Any, expires_at: datetime) -> None:
        """Set a cached response."""
        compressed = gzip.compress(json.dumps(data).encode())
        self._cache[key] = (compressed, expires_at)

    def refresh(self, index: ToolIndex) -> None:
        """
        Refresh all cached API responses from index.

        Args:
            index: The tool index to generate responses from.
        """
        now = datetime.utcnow()
        expires_at = now + self._ttl

        log.debug("Refreshing tool API cache...")

        # Tools list (basic)
        tools_list = [
            entry.to_api_dict() for entry in index.entries.values() if not entry.hidden
        ]
        self._set_cached("tools_list", tools_list, expires_at)

        # Tools list (detailed)
        tools_detailed = [
            entry.to_api_dict(detail=True)
            for entry in index.entries.values()
            if not entry.hidden
        ]
        self._set_cached("tools_list_detailed", tools_detailed, expires_at)

        # Tests summary
        tests_summary = index.get_tests_summary()
        self._set_cached("tests_summary", tests_summary, expires_at)

        # All requirements
        all_reqs = index.get_all_requirements()
        self._set_cached("all_requirements", all_reqs, expires_at)

        # Panel views
        panel_views = index.get_panel_views()
        self._set_cached("panel_views", panel_views, expires_at)

        # Dependency toolbox (by requirements)
        dep_summary = index.get_requirements_summary(index_by="requirements")
        self._set_cached("dependency_toolbox", dep_summary, expires_at)

        log.debug(f"Tool API cache refreshed with {len(self._cache)} entries")

    def refresh_sanitize_allowlist(
        self, index: ToolIndex, allowed_ids: set[str]
    ) -> bytes:
        """
        Refresh and return sanitize allowlist.

        This is computed on-demand because it depends on runtime configuration.

        Args:
            index: The tool index.
            allowed_ids: Set of allowed tool IDs.

        Returns:
            Gzip-compressed JSON response.
        """
        allowlist = index.get_sanitize_allowlist(allowed_ids)
        return gzip.compress(json.dumps(allowlist).encode())

    def invalidate(self) -> None:
        """Invalidate all cached responses."""
        self._cache.clear()

    def invalidate_key(self, key: str) -> None:
        """Invalidate a specific cached response."""
        if key in self._cache:
            del self._cache[key]

    def get_stats(self) -> dict[str, Any]:
        """Get cache statistics."""
        now = datetime.utcnow()
        stats = {
            "cached_keys": list(self._cache.keys()),
            "total_size_bytes": sum(len(data) for data, _ in self._cache.values()),
            "ttl_seconds": self._ttl.total_seconds(),
        }

        # Check which keys are still valid
        valid_keys = []
        expired_keys = []
        for key, (_, expires_at) in self._cache.items():
            if now < expires_at:
                valid_keys.append(key)
            else:
                expired_keys.append(key)

        stats["valid_keys"] = valid_keys
        stats["expired_keys"] = expired_keys

        return stats
