from typing import Any, TypeAlias

__all__ = ["CustomArchivedHistoryViewStateIds"]

CustomArchivedHistoryViewStateIds: TypeAlias = dict[str, Any] | None
"""Alias for A dictionary keyed to possible dataset states and valued with lists containing the ids of each HDA in that state."""
