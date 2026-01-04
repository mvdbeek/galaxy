from typing import Any, TypeAlias

__all__ = ["HistoryDatasetCollections"]

HistoryDatasetCollections: TypeAlias = dict[str, Any] | None
"""Alias for History dataset collections associated with the invocation."""
