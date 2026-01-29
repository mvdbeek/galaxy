from typing import TypeAlias

from .history_contents_result_item import HistoryContentsResultItem

__all__ = ["HistoryContentsResult"]

HistoryContentsResult: TypeAlias = list[HistoryContentsResultItem]
"""Alias for List of history content items.
Can contain different views and kinds of items."""
