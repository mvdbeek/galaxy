from dataclasses import dataclass
from datetime import datetime

from .description import Description
from .synopsis import Synopsis

__all__ = ["LibraryLegacySummary"]


@dataclass
class LibraryLegacySummary:
    """
    LibraryLegacySummary dataclass.

    Args:
        create_time (datetime)   : The time and date this item was created.
        deleted (bool)           : Whether this Library has been deleted.
        id_ (str)                : Encoded ID of the Library.
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the Library.
        root_folder_id (str)     : Encoded ID of the Library's base folder.
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        synopsis (Optional[Synopsis])
                                 : A short text describing the contents of the Library.
                                   Leave unset to keep the existing.
    """

    create_time: datetime  # The time and date this item was created.
    deleted: bool  # Whether this Library has been deleted.
    id_: str  # Encoded ID of the Library.
    model_class: str  # The name of the database model class.
    name: str  # The name of the Library.
    root_folder_id: str  # Encoded ID of the Library's base folder.
    description: Description | None = ""  # Detailed text description for this Quota.
    synopsis: Synopsis | None = (
        ""  # A short text describing the contents of the Library. Leave unset to keep the existing.
    )
