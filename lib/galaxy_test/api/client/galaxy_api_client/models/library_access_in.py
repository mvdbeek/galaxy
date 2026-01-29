from typing import TypeAlias

from .anonymous_array_item_72 import AnonymousArrayItem72

__all__ = ["LibraryAccessIn"]

LibraryAccessIn: TypeAlias = list[AnonymousArrayItem72] | str | None
"""Alias for A list of role encoded IDs defining roles that should have access permission on the library."""
