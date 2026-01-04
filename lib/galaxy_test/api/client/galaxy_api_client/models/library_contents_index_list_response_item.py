from typing import TypeAlias

from .library_contents_index_dataset_response import LibraryContentsIndexDatasetResponse
from .library_contents_index_folder_response import LibraryContentsIndexFolderResponse

__all__ = ["LibraryContentsIndexListResponseItem"]

LibraryContentsIndexListResponseItem: TypeAlias = (
    LibraryContentsIndexDatasetResponse | LibraryContentsIndexFolderResponse
)
