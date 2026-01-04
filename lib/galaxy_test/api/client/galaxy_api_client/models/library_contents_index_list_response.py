from typing import TypeAlias

from .library_contents_index_list_response_item import LibraryContentsIndexListResponseItem

__all__ = ["LibraryContentsIndexListResponse"]

LibraryContentsIndexListResponse: TypeAlias = list[LibraryContentsIndexListResponseItem]
