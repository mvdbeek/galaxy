from typing import TypeAlias

from .library_folder_metadata_full_path_item import LibraryFolderMetadataFullPathItem

__all__ = ["LibraryFolderMetadataFullPath"]

LibraryFolderMetadataFullPath: TypeAlias = list[LibraryFolderMetadataFullPathItem]
