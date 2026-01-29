from dataclasses import dataclass

from .update_library_payload_description import UpdateLibraryPayloadDescription
from .update_library_payload_name import UpdateLibraryPayloadName
from .update_library_payload_synopsis import UpdateLibraryPayloadSynopsis

__all__ = ["UpdateLibraryPayload"]


@dataclass
class UpdateLibraryPayload:
    """
    UpdateLibraryPayload dataclass

    Args:
        description (UpdateLibraryPayloadDescription | None)
                                 : A detailed description of the Library. Leave unset to
                                   keep the existing.
        name (UpdateLibraryPayloadName | None)
                                 : The new name of the Library. Leave unset to keep the
                                   existing.
        synopsis (UpdateLibraryPayloadSynopsis | None)
                                 : A short text describing the contents of the Library.
                                   Leave unset to keep the existing.
    """

    description: UpdateLibraryPayloadDescription | None = (
        None  # A detailed description of the Library. Leave unset to keep the existing.
    )
    name: UpdateLibraryPayloadName | None = None  # The new name of the Library. Leave unset to keep the existing.
    synopsis: UpdateLibraryPayloadSynopsis | None = (
        None  # A short text describing the contents of the Library. Leave unset to keep the existing.
    )

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
