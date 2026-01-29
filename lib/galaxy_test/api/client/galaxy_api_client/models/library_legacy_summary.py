from dataclasses import dataclass
from datetime import datetime

from .library_legacy_summary_description import LibraryLegacySummaryDescription
from .library_legacy_summary_synopsis import LibraryLegacySummarySynopsis

__all__ = ["LibraryLegacySummary"]


@dataclass
class LibraryLegacySummary:
    """
    LibraryLegacySummary dataclass

    Args:
        create_time (datetime)   : The time and date this item was created.
        deleted (bool)           : Whether this Library has been deleted.
        id_ (str)                : Encoded ID of the Library. (maps from 'id')
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the Library.
        root_folder_id (str)     : Encoded ID of the Library's base folder.
        description (LibraryLegacySummaryDescription | None)
                                 : A detailed description of the Library.
        synopsis (LibraryLegacySummarySynopsis | None)
                                 : A short text describing the contents of the Library.
    """

    create_time: datetime  # The time and date this item was created.
    deleted: bool  # Whether this Library has been deleted.
    id_: str  # Encoded ID of the Library. (maps from 'id')
    model_class: str  # The name of the database model class.
    name: str  # The name of the Library.
    root_folder_id: str  # Encoded ID of the Library's base folder.
    description: LibraryLegacySummaryDescription | None = ""  # A detailed description of the Library.
    synopsis: LibraryLegacySummarySynopsis | None = None  # A short text describing the contents of the Library.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "create_time": "create_time",
            "deleted": "deleted",
            "description": "description",
            "id": "id_",
            "model_class": "model_class",
            "name": "name",
            "root_folder_id": "root_folder_id",
            "synopsis": "synopsis",
        }
        key_transform_with_dump = {
            "create_time": "create_time",
            "deleted": "deleted",
            "description": "description",
            "id_": "id",
            "model_class": "model_class",
            "name": "name",
            "root_folder_id": "root_folder_id",
            "synopsis": "synopsis",
        }
