from typing import TypeAlias

from .contents_object import ContentsObject

__all__ = ["ContentsObjectContents"]

ContentsObjectContents: TypeAlias = list[ContentsObject] | None
"""Alias for If this ContentsObject describes a nested bundle and the caller specified "?expand=true" on the request, then this contents array must be present and describe the objects within the nested bundle."""
