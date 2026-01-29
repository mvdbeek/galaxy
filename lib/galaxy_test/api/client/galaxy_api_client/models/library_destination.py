from dataclasses import dataclass

from .data_elements_from_target_destination_type_enum import DataElementsFromTargetDestinationTypeEnum
from .library_destination_description import LibraryDestinationDescription
from .library_destination_synopsis import LibraryDestinationSynopsis

__all__ = ["LibraryDestination"]


@dataclass
class LibraryDestination:
    """
    LibraryDestination dataclass

    Args:
        name (str)               : Must specify a library name
        type_ (DataElementsFromTargetDestinationTypeEnum)
                                 : Maps from 'type'
        description (LibraryDestinationDescription | None)
                                 : Description for library to create
        synopsis (LibraryDestinationSynopsis | None)
                                 : Description for library to create
    """

    name: str  # Must specify a library name
    type_: DataElementsFromTargetDestinationTypeEnum  # Maps from 'type'
    description: LibraryDestinationDescription | None = None  # Description for library to create
    synopsis: LibraryDestinationSynopsis | None = None  # Description for library to create

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "description": "description",
            "name": "name",
            "synopsis": "synopsis",
            "type": "type_",
        }
        key_transform_with_dump = {
            "description": "description",
            "name": "name",
            "synopsis": "synopsis",
            "type_": "type",
        }
