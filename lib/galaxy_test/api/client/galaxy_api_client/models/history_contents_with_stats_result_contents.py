from typing import TypeAlias

from .history_contents_with_stats_result_contents_item import HistoryContentsWithStatsResultContentsItem

__all__ = ["HistoryContentsWithStatsResultContents"]

HistoryContentsWithStatsResultContents: TypeAlias = list[HistoryContentsWithStatsResultContentsItem]
"""Alias for The items matching the search query. Only the items fitting in the current page limit will be returned."""
