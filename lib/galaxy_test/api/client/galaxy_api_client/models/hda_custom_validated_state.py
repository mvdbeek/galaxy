from typing import TypeAlias

from .dataset_validated_state import DatasetValidatedState

__all__ = ["HdaCustomValidatedState"]

HdaCustomValidatedState: TypeAlias = DatasetValidatedState | None
"""Alias for The state of the datatype validation for this dataset."""
