from typing import TypeAlias

from .anonymous_array_item_76 import AnonymousArrayItem76

__all__ = ["LibraryManageIn"]

LibraryManageIn: TypeAlias = list[AnonymousArrayItem76] | str | None
"""Alias for A list of role encoded IDs defining roles that should have modify permission on the library."""
