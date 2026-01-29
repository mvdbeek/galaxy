from dataclasses import dataclass

from .library_folder_metadata_full_path import LibraryFolderMetadataFullPath

__all__ = ["LibraryFolderMetadata"]


@dataclass
class LibraryFolderMetadata:
    """
    LibraryFolderMetadata dataclass

    Args:
        can_add_library_item (bool)
                                 :
        can_modify_folder (bool) :
        folder_description (str) :
        folder_name (str)        :
        full_path (LibraryFolderMetadataFullPath)
                                 :
        parent_library_id (str)  :
        total_rows (int)         :
    """

    can_add_library_item: bool
    can_modify_folder: bool
    folder_description: str
    folder_name: str
    full_path: LibraryFolderMetadataFullPath
    parent_library_id: str
    total_rows: int

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "can_add_library_item": "can_add_library_item",
            "can_modify_folder": "can_modify_folder",
            "folder_description": "folder_description",
            "folder_name": "folder_name",
            "full_path": "full_path",
            "parent_library_id": "parent_library_id",
            "total_rows": "total_rows",
        }
        key_transform_with_dump = {
            "can_add_library_item": "can_add_library_item",
            "can_modify_folder": "can_modify_folder",
            "folder_description": "folder_description",
            "folder_name": "folder_name",
            "full_path": "full_path",
            "parent_library_id": "parent_library_id",
            "total_rows": "total_rows",
        }
