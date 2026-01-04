from typing import TypeAlias

from .anonymous_array_item_74 import AnonymousArrayItem74

__all__ = ["LibraryAddIn"]

LibraryAddIn: TypeAlias = list[AnonymousArrayItem74] | str | None
"""Alias for A list of role encoded IDs defining roles that should have manage permission on the library."""
