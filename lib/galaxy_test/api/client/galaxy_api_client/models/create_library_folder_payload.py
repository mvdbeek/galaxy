from dataclasses import dataclass

from .create_library_folder_payload_description import CreateLibraryFolderPayloadDescription

__all__ = ["CreateLibraryFolderPayload"]


@dataclass
class CreateLibraryFolderPayload:
    """
    CreateLibraryFolderPayload dataclass

    Args:
        name (str)               : The name of the library folder.
        description (CreateLibraryFolderPayloadDescription | None)
                                 : A detailed description of the library folder.
    """

    name: str  # The name of the library folder.
    description: CreateLibraryFolderPayloadDescription | None = ""  # A detailed description of the library folder.

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
