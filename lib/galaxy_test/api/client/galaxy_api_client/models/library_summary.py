from dataclasses import dataclass
from datetime import datetime

from .description import Description
from .synopsis import Synopsis

__all__ = ["LibrarySummary"]


@dataclass
class LibrarySummary:
    """
    LibrarySummary dataclass.

    Args:
        can_user_add (bool)      : Whether the current user can add contents to this
                                   Library.
        can_user_manage (bool)   : Whether the current user can manage the Library and its
                                   contents.
        can_user_modify (bool)   : Whether the current user can modify this Library.
        create_time (datetime)   : The time and date this item was created.
        create_time_pretty (str) : Nice time representation of the creation date.
        deleted (bool)           : Whether this Library has been deleted.
        id_ (str)                : Encoded ID of the Library.
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the Library.
        public (bool)            : Whether this Library has been deleted.
        root_folder_id (str)     : Encoded ID of the Library's base folder.
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        synopsis (Optional[Synopsis])
                                 : A short text describing the contents of the Library.
                                   Leave unset to keep the existing.
    """

    can_user_add: bool  # Whether the current user can add contents to this Library.
    can_user_manage: bool  # Whether the current user can manage the Library and its contents.
    can_user_modify: bool  # Whether the current user can modify this Library.
    create_time: datetime  # The time and date this item was created.
    create_time_pretty: str  # Nice time representation of the creation date.
    deleted: bool  # Whether this Library has been deleted.
    id_: str  # Encoded ID of the Library.
    model_class: str  # The name of the database model class.
    name: str  # The name of the Library.
    public: bool  # Whether this Library has been deleted.
    root_folder_id: str  # Encoded ID of the Library's base folder.
    description: Description | None = ""  # Detailed text description for this Quota.
    synopsis: Synopsis | None = (
        ""  # A short text describing the contents of the Library. Leave unset to keep the existing.
    )
