from typing import TypeAlias

from .dce_summary_2 import DceSummary2

__all__ = ["DatasetCollectionContentElements"]

DatasetCollectionContentElements: TypeAlias = list[DceSummary2]
"""Alias for Represents a collection of elements contained in the dataset collection."""
