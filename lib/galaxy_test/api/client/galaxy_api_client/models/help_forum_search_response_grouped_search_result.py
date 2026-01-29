from typing import TypeAlias

from .help_forum_grouped_search_result import HelpForumGroupedSearchResult

__all__ = ["HelpForumSearchResponseGroupedSearchResult"]

HelpForumSearchResponseGroupedSearchResult: TypeAlias = HelpForumGroupedSearchResult | None
"""Alias for The grouped search result."""
