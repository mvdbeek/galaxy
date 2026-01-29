from typing import TypeAlias

from .dataset_source_transform import DatasetSourceTransform

__all__ = ["Transform"]

Transform: TypeAlias = list[DatasetSourceTransform] | None
"""Alias for The transformations applied to the dataset source."""
