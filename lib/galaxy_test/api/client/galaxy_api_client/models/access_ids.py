from typing import TypeAlias

from .anonymous_array_item_86 import AnonymousArrayItem86

__all__ = ["AccessIds"]

AccessIds: TypeAlias = list[AnonymousArrayItem86] | str | None
"""Alias for A list of role encoded IDs defining roles that should have access permission on the dataset."""
