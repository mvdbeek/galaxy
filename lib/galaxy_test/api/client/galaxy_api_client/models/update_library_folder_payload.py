from dataclasses import dataclass

from .update_library_folder_payload_description import UpdateLibraryFolderPayloadDescription
from .update_library_folder_payload_name import UpdateLibraryFolderPayloadName

__all__ = ["UpdateLibraryFolderPayload"]


@dataclass
class UpdateLibraryFolderPayload:
    """
    UpdateLibraryFolderPayload dataclass

    Args:
        description (UpdateLibraryFolderPayloadDescription | None)
                                 : The new description of the library folder.
        name (UpdateLibraryFolderPayloadName | None)
                                 : The new name of the library folder.
    """

    description: UpdateLibraryFolderPayloadDescription | None = None  # The new description of the library folder.
    name: UpdateLibraryFolderPayloadName | None = None  # The new name of the library folder.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "description": "description",
            "name": "name",
        }
        key_transform_with_dump = {
            "description": "description",
            "name": "name",
        }
