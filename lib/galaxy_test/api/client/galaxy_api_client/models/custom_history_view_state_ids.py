from typing import Any, TypeAlias

__all__ = ["CustomHistoryViewStateIds"]

CustomHistoryViewStateIds: TypeAlias = dict[str, Any] | None
"""Alias for A dictionary keyed to possible dataset states and valued with lists containing the ids of each HDA in that state."""
