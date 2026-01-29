from dataclasses import dataclass
from datetime import datetime

from .library_summary_description import LibrarySummaryDescription
from .library_summary_synopsis import LibrarySummarySynopsis

__all__ = ["LibrarySummary"]


@dataclass
class LibrarySummary:
    """
    LibrarySummary dataclass

    Args:
        can_user_add (bool)      : Whether the current user can add contents to this
                                   Library.
        can_user_manage (bool)   : Whether the current user can manage the Library and its
                                   contents.
        can_user_modify (bool)   : Whether the current user can modify this Library.
        create_time (datetime)   : The time and date this item was created.
        create_time_pretty (str) : Nice time representation of the creation date.
        deleted (bool)           : Whether this Library has been deleted.
        id_ (str)                : Encoded ID of the Library. (maps from 'id')
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the Library.
        public (bool)            : Whether this Library has been deleted.
        root_folder_id (str)     : Encoded ID of the Library's base folder.
        description (LibrarySummaryDescription | None)
                                 : A detailed description of the Library.
        synopsis (LibrarySummarySynopsis | None)
                                 : A short text describing the contents of the Library.
    """

    can_user_add: bool  # Whether the current user can add contents to this Library.
    can_user_manage: bool  # Whether the current user can manage the Library and its contents.
    can_user_modify: bool  # Whether the current user can modify this Library.
    create_time: datetime  # The time and date this item was created.
    create_time_pretty: str  # Nice time representation of the creation date.
    deleted: bool  # Whether this Library has been deleted.
    id_: str  # Encoded ID of the Library. (maps from 'id')
    model_class: str  # The name of the database model class.
    name: str  # The name of the Library.
    public: bool  # Whether this Library has been deleted.
    root_folder_id: str  # Encoded ID of the Library's base folder.
    description: LibrarySummaryDescription | None = ""  # A detailed description of the Library.
    synopsis: LibrarySummarySynopsis | None = None  # A short text describing the contents of the Library.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "can_user_add": "can_user_add",
            "can_user_manage": "can_user_manage",
            "can_user_modify": "can_user_modify",
            "create_time": "create_time",
            "create_time_pretty": "create_time_pretty",
            "deleted": "deleted",
            "description": "description",
            "id": "id_",
            "model_class": "model_class",
            "name": "name",
            "public": "public",
            "root_folder_id": "root_folder_id",
            "synopsis": "synopsis",
        }
        key_transform_with_dump = {
            "can_user_add": "can_user_add",
            "can_user_manage": "can_user_manage",
            "can_user_modify": "can_user_modify",
            "create_time": "create_time",
            "create_time_pretty": "create_time_pretty",
            "deleted": "deleted",
            "description": "description",
            "id_": "id",
            "model_class": "model_class",
            "name": "name",
            "public": "public",
            "root_folder_id": "root_folder_id",
            "synopsis": "synopsis",
        }
