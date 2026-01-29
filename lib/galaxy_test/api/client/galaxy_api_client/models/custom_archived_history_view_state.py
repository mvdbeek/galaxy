from typing import TypeAlias

from .dataset_state import DatasetState

__all__ = ["CustomArchivedHistoryViewState"]

CustomArchivedHistoryViewState: TypeAlias = DatasetState | None
"""Alias for The current state of the History based on the states of the datasets it contains."""
