from typing import TypeAlias

from .anonymous_array_item_80 import AnonymousArrayItem80

__all__ = ["AddIds"]

AddIds: TypeAlias = list[AnonymousArrayItem80] | str | None
"""Alias for A list of role encoded IDs defining roles that should be able to add items to the library."""
