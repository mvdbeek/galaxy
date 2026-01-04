from dataclasses import dataclass

from .folder_contents import FolderContents
from .library_folder_metadata import LibraryFolderMetadata

__all__ = ["LibraryFolderContentsIndexResult"]


@dataclass
class LibraryFolderContentsIndexResult:
    """
    LibraryFolderContentsIndexResult dataclass.

    Args:
        folder_contents (FolderContents)
                                 :
        metadata (LibraryFolderMetadata)
                                 :
    """

    folder_contents: FolderContents
    metadata: LibraryFolderMetadata
