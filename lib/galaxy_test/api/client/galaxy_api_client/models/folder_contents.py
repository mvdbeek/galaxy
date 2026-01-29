from typing import TypeAlias

from .folder_contents_item import FolderContentsItem

__all__ = ["FolderContents"]

FolderContents: TypeAlias = list[FolderContentsItem]
