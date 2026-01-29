from dataclasses import dataclass
from datetime import datetime

from .dataset_state import DatasetState
from .file_library_folder_item_message import FileLibraryFolderItemMessage
from .library_folder_contents_index_result_folder_contents_item_type_enum import (
    LibraryFolderContentsIndexResultFolderContentsItemTypeEnum,
)

__all__ = ["FileLibraryFolderItem"]


@dataclass
class FileLibraryFolderItem:
    """
    FileLibraryFolderItem dataclass

    Args:
        can_manage (bool)        :
        create_time (datetime)   : The time and date this item was created.
        date_uploaded (datetime) :
        deleted (bool)           :
        file_ext (str)           :
        file_size (str)          :
        id_ (str)                : Maps from 'id'
        is_private (bool)        :
        is_unrestricted (bool)   :
        ldda_id (str)            :
        name (str)               :
        raw_size (int)           :
        state (DatasetState)     :
        tags (List[str])         : The collection of tags associated with an item.
        type_ (LibraryFolderContentsIndexResultFolderContentsItemTypeEnum)
                                 : Maps from 'type'
        update_time (datetime)   : The last time and date this item was updated.
        message (FileLibraryFolderItemMessage | None)
                                 :
    """

    can_manage: bool
    create_time: datetime  # The time and date this item was created.
    date_uploaded: datetime
    deleted: bool
    file_ext: str
    file_size: str
    id_: str  # Maps from 'id'
    is_private: bool
    is_unrestricted: bool
    ldda_id: str
    name: str
    raw_size: int
    state: DatasetState
    tags: list[str]  # The collection of tags associated with an item.
    type_: LibraryFolderContentsIndexResultFolderContentsItemTypeEnum  # Maps from 'type'
    update_time: datetime  # The last time and date this item was updated.
    message: FileLibraryFolderItemMessage | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "can_manage": "can_manage",
            "create_time": "create_time",
            "date_uploaded": "date_uploaded",
            "deleted": "deleted",
            "file_ext": "file_ext",
            "file_size": "file_size",
            "id": "id_",
            "is_private": "is_private",
            "is_unrestricted": "is_unrestricted",
            "ldda_id": "ldda_id",
            "message": "message",
            "name": "name",
            "raw_size": "raw_size",
            "state": "state",
            "tags": "tags",
            "type": "type_",
            "update_time": "update_time",
        }
        key_transform_with_dump = {
            "can_manage": "can_manage",
            "create_time": "create_time",
            "date_uploaded": "date_uploaded",
            "deleted": "deleted",
            "file_ext": "file_ext",
            "file_size": "file_size",
            "id_": "id",
            "is_private": "is_private",
            "is_unrestricted": "is_unrestricted",
            "ldda_id": "ldda_id",
            "message": "message",
            "name": "name",
            "raw_size": "raw_size",
            "state": "state",
            "tags": "tags",
            "type_": "type",
            "update_time": "update_time",
        }
