from typing import Any, TypeAlias

__all__ = ["CustomArchivedHistoryViewStateDetails"]

CustomArchivedHistoryViewStateDetails: TypeAlias = dict[str, Any] | None
"""Alias for A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states."""
