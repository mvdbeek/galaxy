from typing import TypeAlias

from .anonymous_array_item_78 import AnonymousArrayItem78

__all__ = ["LibraryModifyIn"]

LibraryModifyIn: TypeAlias = list[AnonymousArrayItem78] | str | None
"""Alias for A list of role encoded IDs defining roles that should be able to add items to the library."""
