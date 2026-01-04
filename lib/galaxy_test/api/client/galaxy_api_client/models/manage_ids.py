from typing import TypeAlias

from .anonymous_array_item_82 import AnonymousArrayItem82

__all__ = ["ManageIds"]

ManageIds: TypeAlias = list[AnonymousArrayItem82] | str | None
"""Alias for A list of role encoded IDs defining roles that should have manage permission on the dataset."""
