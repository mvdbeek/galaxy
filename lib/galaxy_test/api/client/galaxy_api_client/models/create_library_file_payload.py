from dataclasses import dataclass

from .create_library_file_payload_from_hda_id import CreateLibraryFilePayloadFromHdaId
from .create_library_file_payload_from_hdca_id import CreateLibraryFilePayloadFromHdcaId
from .create_library_file_payload_ldda_message import CreateLibraryFilePayloadLddaMessage

__all__ = ["CreateLibraryFilePayload"]


@dataclass
class CreateLibraryFilePayload:
    """
    CreateLibraryFilePayload dataclass

    Args:
        from_hda_id (CreateLibraryFilePayloadFromHdaId | None)
                                 : The ID of an accessible HDA to copy into the library.
        from_hdca_id (CreateLibraryFilePayloadFromHdcaId | None)
                                 : The ID of an accessible HDCA to copy into the library.
                                   Nested collections are not allowed, you must flatten the
                                   collection first.
        ldda_message (CreateLibraryFilePayloadLddaMessage | None)
                                 : The new message attribute of the LDDA created.
    """

    from_hda_id: CreateLibraryFilePayloadFromHdaId | None = (
        None  # The ID of an accessible HDA to copy into the library.
    )
    from_hdca_id: CreateLibraryFilePayloadFromHdcaId | None = (
        None  # The ID of an accessible HDCA to copy into the library. Nested collections are not allowed, you must flatten the collection first.
    )
    ldda_message: CreateLibraryFilePayloadLddaMessage | None = ""  # The new message attribute of the LDDA created.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "from_hda_id": "from_hda_id",
            "from_hdca_id": "from_hdca_id",
            "ldda_message": "ldda_message",
        }
        key_transform_with_dump = {
            "from_hda_id": "from_hda_id",
            "from_hdca_id": "from_hdca_id",
            "ldda_message": "ldda_message",
        }
