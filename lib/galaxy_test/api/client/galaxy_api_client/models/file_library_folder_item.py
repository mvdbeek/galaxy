from dataclasses import dataclass
from datetime import datetime

from .dataset_state import DatasetState
from .message import Message
from .tags import Tags

__all__ = ["FileLibraryFolderItem"]


@dataclass
class FileLibraryFolderItem:
    """
    FileLibraryFolderItem dataclass.

    Args:
        can_manage (bool)        :
        create_time (datetime)   : The time and date this item was created.
        date_uploaded (datetime) :
        deleted (bool)           :
        file_ext (str)           :
        file_size (str)          :
        id_ (str)                :
        is_private (bool)        :
        is_unrestricted (bool)   :
        ldda_id (str)            :
        name (str)               :
        raw_size (int)           :
        state (DatasetState)     :
        tags (Tags)              : The collection of tags associated with an item.
        type_ (str)              :
        update_time (datetime)   : The last time and date this item was updated.
        message (Optional[Message])
                                 : The optional message sent with the error report.
    """

    can_manage: bool
    create_time: datetime  # The time and date this item was created.
    date_uploaded: datetime
    deleted: bool
    file_ext: str
    file_size: str
    id_: str
    is_private: bool
    is_unrestricted: bool
    ldda_id: str
    name: str
    raw_size: int
    state: DatasetState
    tags: Tags  # The collection of tags associated with an item.
    type_: str
    update_time: datetime  # The last time and date this item was updated.
    message: Message | None = None  # The optional message sent with the error report.
