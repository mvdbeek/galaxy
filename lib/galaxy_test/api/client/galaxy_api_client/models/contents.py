from typing import TypeAlias

from .contents_object import ContentsObject

__all__ = ["Contents"]

Contents: TypeAlias = list[ContentsObject] | None
"""Alias for The items matching the search query. Only the items fitting in the current page limit will be returned."""
