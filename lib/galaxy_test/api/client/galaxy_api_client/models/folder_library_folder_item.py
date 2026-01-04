from dataclasses import dataclass
from datetime import datetime

from .description import Description

__all__ = ["FolderLibraryFolderItem"]


@dataclass
class FolderLibraryFolderItem:
    """
    FolderLibraryFolderItem dataclass.

    Args:
        can_manage (bool)        :
        can_modify (bool)        :
        create_time (datetime)   : The time and date this item was created.
        deleted (bool)           :
        id_ (str)                :
        name (str)               :
        type_ (str)              :
        update_time (datetime)   : The last time and date this item was updated.
        description (Optional[Description])
                                 : Detailed text description for this Quota.
    """

    can_manage: bool
    can_modify: bool
    create_time: datetime  # The time and date this item was created.
    deleted: bool
    id_: str
    name: str
    type_: str
    update_time: datetime  # The last time and date this item was updated.
    description: Description | None = ""  # Detailed text description for this Quota.
