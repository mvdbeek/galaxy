from typing import TypeAlias

from .full_path_item import FullPathItem

__all__ = ["FullPath"]

FullPath: TypeAlias = list[FullPathItem]
