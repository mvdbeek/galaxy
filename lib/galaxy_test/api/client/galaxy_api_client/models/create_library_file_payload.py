from dataclasses import dataclass

from .from_hda_id import FromHdaId
from .from_hdca_id import FromHdcaId
from .ldda_message import LddaMessage

__all__ = ["CreateLibraryFilePayload"]


@dataclass
class CreateLibraryFilePayload:
    """
    CreateLibraryFilePayload dataclass.

    Args:
        from_hda_id (Optional[FromHdaId])
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDA to copy into the library
        from_hdca_id (Optional[FromHdcaId])
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDCA to copy into the library
        ldda_message (Optional[LddaMessage])
                                 : The new message attribute of the LDDA created.
    """

    from_hda_id: FromHdaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDA to copy into the library
    )
    from_hdca_id: FromHdcaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDCA to copy into the library
    )
    ldda_message: LddaMessage | None = ""  # The new message attribute of the LDDA created.
