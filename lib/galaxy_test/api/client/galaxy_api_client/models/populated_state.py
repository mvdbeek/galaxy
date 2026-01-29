from typing import TypeAlias

__all__ = ["PopulatedState"]

PopulatedState: TypeAlias = str | None
"""Alias for Indicates the general state of the elements in the dataset collection:- 'new': new dataset collection, unpopulated elements.- 'ok': collection elements populated (HDAs may or may not have errors).- 'failed': some problem populating, won't be populated."""
