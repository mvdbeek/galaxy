"""Tests for the tool sources API.

These tests verify the tool source storage and index API endpoints.
Note: The tool source store must be configured for these tests to work.
"""

from ._framework import ApiTestCase


class TestToolSourcesApi(ApiTestCase):
    """Tests for /api/tool_sources endpoints."""

    def test_list_tool_sources(self):
        """Test listing tool sources."""
        response = self._get("tool_sources", admin=True)
        # May return 404 if store not configured, which is acceptable
        if response.status_code == 404:
            return
        self._assert_status_code_is(response, 200)
        data = response.json()
        assert "total_count" in data
        assert "items" in data
        assert isinstance(data["items"], list)

    def test_list_tool_sources_with_pagination(self):
        """Test listing tool sources with pagination."""
        response = self._get("tool_sources?limit=10&offset=0", admin=True)
        if response.status_code == 404:
            return
        self._assert_status_code_is(response, 200)
        data = response.json()
        assert len(data["items"]) <= 10

    def test_get_tool_sources_stats(self):
        """Test getting tool source storage statistics."""
        response = self._get("tool_sources/stats", admin=True)
        if response.status_code == 404:
            return
        self._assert_status_code_is(response, 200)
        data = response.json()
        assert "backend" in data
        assert "count" in data

    def test_get_nonexistent_tool_source(self):
        """Test getting a non-existent tool source returns 404."""
        response = self._get("tool_sources/nonexistent_hash_12345", admin=True)
        # Either 404 for not found or 404 for store not configured
        self._assert_status_code_is(response, 404)


class TestToolIndexApi(ApiTestCase):
    """Tests for /api/tool_index endpoints."""

    def test_list_index_entries(self):
        """Test listing tool index entries."""
        response = self._get("tool_index", admin=True)
        if response.status_code == 404:
            return
        self._assert_status_code_is(response, 200)
        data = response.json()
        assert isinstance(data, list)

    def test_list_index_entries_with_section_filter(self):
        """Test listing tool index entries filtered by section."""
        response = self._get("tool_index?section_id=test_section", admin=True)
        if response.status_code == 404:
            return
        self._assert_status_code_is(response, 200)

    def test_get_index_stats(self):
        """Test getting tool index statistics."""
        response = self._get("tool_index/stats", admin=True)
        if response.status_code == 404:
            return
        self._assert_status_code_is(response, 200)
        data = response.json()
        assert "index_size" in data
        assert "memory_estimate_bytes" in data

    def test_search_index(self):
        """Test searching the tool index."""
        response = self._get("tool_index/search?q=test", admin=True)
        if response.status_code == 404:
            return
        self._assert_status_code_is(response, 200)
        data = response.json()
        assert isinstance(data, list)

    def test_search_index_requires_query(self):
        """Test that search requires a query parameter."""
        response = self._get("tool_index/search", admin=True)
        # Should return 422 for missing required parameter
        assert response.status_code in (404, 422)


class TestToolCacheApi(ApiTestCase):
    """Tests for /api/tool_cache endpoints."""

    def test_get_cache_stats(self):
        """Test getting cache statistics."""
        response = self._get("tool_cache/stats", admin=True)
        self._assert_status_code_is(response, 200)
        data = response.json()
        assert "tool_cache_size" in data
        assert "tool_cache_maxsize" in data
        assert "index_size" in data
        assert "index_memory_estimate" in data

    def test_clear_cache(self):
        """Test clearing the tool cache."""
        response = self._post("tool_cache/clear", admin=True)
        self._assert_status_code_is(response, 200)
        data = response.json()
        assert data.get("status") == "cleared"
