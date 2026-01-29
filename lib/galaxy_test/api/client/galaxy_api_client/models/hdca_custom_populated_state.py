from typing import TypeAlias

from .dataset_collection_populated_state import DatasetCollectionPopulatedState

__all__ = ["HdcaCustomPopulatedState"]

HdcaCustomPopulatedState: TypeAlias = DatasetCollectionPopulatedState | None
"""Alias for Indicates the general state of the elements in the dataset collection:- 'new': new dataset collection, unpopulated elements.- 'ok': collection elements populated (HDAs may or may not have errors).- 'failed': some problem populating, won't be populated."""
