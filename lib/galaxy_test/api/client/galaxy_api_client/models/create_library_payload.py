from dataclasses import dataclass

from .create_library_payload_description import CreateLibraryPayloadDescription
from .create_library_payload_synopsis import CreateLibraryPayloadSynopsis

__all__ = ["CreateLibraryPayload"]


@dataclass
class CreateLibraryPayload:
    """
    CreateLibraryPayload dataclass

    Args:
        name (str)               : The name of the Library.
        description (CreateLibraryPayloadDescription | None)
                                 : A detailed description of the Library.
        synopsis (CreateLibraryPayloadSynopsis | None)
                                 : A short text describing the contents of the Library.
    """

    name: str  # The name of the Library.
    description: CreateLibraryPayloadDescription | None = ""  # A detailed description of the Library.
    synopsis: CreateLibraryPayloadSynopsis | None = ""  # A short text describing the contents of the Library.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "description": "description",
            "name": "name",
            "synopsis": "synopsis",
        }
        key_transform_with_dump = {
            "description": "description",
            "name": "name",
            "synopsis": "synopsis",
        }
