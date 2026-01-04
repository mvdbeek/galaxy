from typing import TypeAlias

from .anonymous_array_item_84 import AnonymousArrayItem84

__all__ = ["ModifyIds"]

ModifyIds: TypeAlias = list[AnonymousArrayItem84] | str | None
"""Alias for A list of role encoded IDs defining roles that should have modify permission on the dataset."""
