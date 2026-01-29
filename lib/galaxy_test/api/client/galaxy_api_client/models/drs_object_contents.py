from typing import TypeAlias

from .contents_object import ContentsObject

__all__ = ["DrsObjectContents"]

DrsObjectContents: TypeAlias = list[ContentsObject] | None
"""Alias for If not set, this `DrsObject` is a single blob.
If set, this `DrsObject` is a bundle containing the listed `ContentsObject` s (some of which may be further nested)."""
