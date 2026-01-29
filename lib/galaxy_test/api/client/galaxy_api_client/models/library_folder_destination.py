from dataclasses import dataclass

from .data_elements_from_target_destination_type_enum import DataElementsFromTargetDestinationTypeEnum

__all__ = ["LibraryFolderDestination"]


@dataclass
class LibraryFolderDestination:
    """
    LibraryFolderDestination dataclass

    Args:
        library_folder_id (str)  :
        type_ (DataElementsFromTargetDestinationTypeEnum)
                                 : Maps from 'type'
    """

    library_folder_id: str
    type_: DataElementsFromTargetDestinationTypeEnum  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "library_folder_id": "library_folder_id",
            "type": "type_",
        }
        key_transform_with_dump = {
            "library_folder_id": "library_folder_id",
            "type_": "type",
        }
