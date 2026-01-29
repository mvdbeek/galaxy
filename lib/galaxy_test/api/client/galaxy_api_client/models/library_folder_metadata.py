from dataclasses import dataclass

from .full_path import FullPath

__all__ = ["LibraryFolderMetadata"]


@dataclass
class LibraryFolderMetadata:
    """
    LibraryFolderMetadata dataclass.

    Args:
        can_add_library_item (bool)
                                 :
        can_modify_folder (bool) :
        folder_description (str) :
        folder_name (str)        :
        full_path (FullPath)     :
        parent_library_id (str)  :
        total_rows (int)         :
    """

    can_add_library_item: bool
    can_modify_folder: bool
    folder_description: str
    folder_name: str
    full_path: FullPath
    parent_library_id: str
    total_rows: int
