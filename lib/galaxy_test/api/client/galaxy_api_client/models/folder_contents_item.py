from typing import TypeAlias

from .file_library_folder_item import FileLibraryFolderItem
from .folder_library_folder_item import FolderLibraryFolderItem

__all__ = ["FolderContentsItem"]

FolderContentsItem: TypeAlias = FileLibraryFolderItem | FolderLibraryFolderItem
