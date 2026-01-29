from typing import TypeAlias

from .delete_library_payload import DeleteLibraryPayload

__all__ = ["LibrariesDeleteRequestBody"]

LibrariesDeleteRequestBody: TypeAlias = DeleteLibraryPayload | None
