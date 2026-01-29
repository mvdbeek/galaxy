from dataclasses import dataclass
from typing import Annotated, TypeAlias

from .file_library_folder_item import FileLibraryFolderItem
from .folder_library_folder_item import FolderLibraryFolderItem

__all__ = [
    "LibraryFolderContentsIndexResultFolderContentsItem",
    "LibraryFolderContentsIndexResultFolderContentsItemDiscriminator",
]


@dataclass(frozen=True)
class LibraryFolderContentsIndexResultFolderContentsItemDiscriminator:
    """Discriminator metadata for LibraryFolderContentsIndexResultFolderContentsItem union."""

    property_name: str = "type"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("file", "FileLibraryFolderItem"),
        ("folder", "FolderLibraryFolderItem"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .file_library_folder_item import FileLibraryFolderItem
        from .folder_library_folder_item import FolderLibraryFolderItem

        return {
            "file": FileLibraryFolderItem,
            "folder": FolderLibraryFolderItem,
        }


LibraryFolderContentsIndexResultFolderContentsItem: TypeAlias = Annotated[
    FileLibraryFolderItem | FolderLibraryFolderItem, LibraryFolderContentsIndexResultFolderContentsItemDiscriminator()
]
