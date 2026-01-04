from typing import Any, TypeAlias

__all__ = ["HistoryDatasets"]

HistoryDatasets: TypeAlias = dict[str, Any] | None
"""Alias for History datasets associated with the invocation."""
