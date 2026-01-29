from typing import TypeAlias

__all__ = ["DatasetSourceTransform"]

DatasetSourceTransform: TypeAlias = list["DatasetSourceTransform"] | None
"""Alias for The transformations applied to the dataset source."""
