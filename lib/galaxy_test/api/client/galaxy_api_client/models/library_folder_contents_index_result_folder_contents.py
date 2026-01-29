from typing import TypeAlias

from .library_folder_contents_index_result_folder_contents_item import (
    LibraryFolderContentsIndexResultFolderContentsItem,
)

__all__ = ["LibraryFolderContentsIndexResultFolderContents"]

LibraryFolderContentsIndexResultFolderContents: TypeAlias = list[LibraryFolderContentsIndexResultFolderContentsItem]
