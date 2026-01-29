from dataclasses import dataclass
from typing import Annotated, TypeAlias

from .hda_destination import HdaDestination
from .library_destination import LibraryDestination
from .library_folder_destination import LibraryFolderDestination

__all__ = ["DataElementsFromTargetDestination", "DataElementsFromTargetDestinationDiscriminator"]


@dataclass(frozen=True)
class DataElementsFromTargetDestinationDiscriminator:
    """Discriminator metadata for DataElementsFromTargetDestination union."""

    property_name: str = "type"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("hdas", "HdaDestination"),
        ("library", "LibraryDestination"),
        ("library_folder", "LibraryFolderDestination"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .hda_destination import HdaDestination
        from .library_destination import LibraryDestination
        from .library_folder_destination import LibraryFolderDestination

        return {
            "hdas": HdaDestination,
            "library": LibraryDestination,
            "library_folder": LibraryFolderDestination,
        }


DataElementsFromTargetDestination: TypeAlias = Annotated[
    HdaDestination | LibraryFolderDestination | LibraryDestination, DataElementsFromTargetDestinationDiscriminator()
]
