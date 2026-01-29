from dataclasses import dataclass
from datetime import datetime

from .folder_library_folder_item_description import FolderLibraryFolderItemDescription
from .library_folder_contents_index_result_folder_contents_item_type_enum import (
    LibraryFolderContentsIndexResultFolderContentsItemTypeEnum,
)

__all__ = ["FolderLibraryFolderItem"]


@dataclass
class FolderLibraryFolderItem:
    """
    FolderLibraryFolderItem dataclass

    Args:
        can_manage (bool)        :
        can_modify (bool)        :
        create_time (datetime)   : The time and date this item was created.
        deleted (bool)           :
        id_ (str)                : Maps from 'id'
        name (str)               :
        type_ (LibraryFolderContentsIndexResultFolderContentsItemTypeEnum)
                                 : Maps from 'type'
        update_time (datetime)   : The last time and date this item was updated.
        description (FolderLibraryFolderItemDescription | None)
                                 : A detailed description of the library folder.
    """

    can_manage: bool
    can_modify: bool
    create_time: datetime  # The time and date this item was created.
    deleted: bool
    id_: str  # Maps from 'id'
    name: str
    type_: LibraryFolderContentsIndexResultFolderContentsItemTypeEnum  # Maps from 'type'
    update_time: datetime  # The last time and date this item was updated.
    description: FolderLibraryFolderItemDescription | None = ""  # A detailed description of the library folder.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "can_manage": "can_manage",
            "can_modify": "can_modify",
            "create_time": "create_time",
            "deleted": "deleted",
            "description": "description",
            "id": "id_",
            "name": "name",
            "type": "type_",
            "update_time": "update_time",
        }
        key_transform_with_dump = {
            "can_manage": "can_manage",
            "can_modify": "can_modify",
            "create_time": "create_time",
            "deleted": "deleted",
            "description": "description",
            "id_": "id",
            "name": "name",
            "type_": "type",
            "update_time": "update_time",
        }
