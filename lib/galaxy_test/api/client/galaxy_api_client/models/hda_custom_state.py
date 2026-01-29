from typing import TypeAlias

from .dataset_state import DatasetState

__all__ = ["HdaCustomState"]

HdaCustomState: TypeAlias = DatasetState | None
"""Alias for The current state of this dataset."""
