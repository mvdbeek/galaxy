from dataclasses import dataclass

from .library_folder_contents_index_result_folder_contents import LibraryFolderContentsIndexResultFolderContents
from .library_folder_metadata import LibraryFolderMetadata

__all__ = ["LibraryFolderContentsIndexResult"]


@dataclass
class LibraryFolderContentsIndexResult:
    """
    LibraryFolderContentsIndexResult dataclass

    Args:
        folder_contents (LibraryFolderContentsIndexResultFolderContents)
                                 :
        metadata (LibraryFolderMetadata)
                                 :
    """

    folder_contents: LibraryFolderContentsIndexResultFolderContents
    metadata: LibraryFolderMetadata

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "folder_contents": "folder_contents",
            "metadata": "metadata",
        }
        key_transform_with_dump = {
            "folder_contents": "folder_contents",
            "metadata": "metadata",
        }
