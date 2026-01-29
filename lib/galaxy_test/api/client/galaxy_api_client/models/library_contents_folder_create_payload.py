from dataclasses import dataclass

from .create_type import CreateType
from .extended_metadata import ExtendedMetadata
from .from_hda_id import FromHdaId
from .from_hdca_id import FromHdcaId
from .tags import Tags
from .upload_option import UploadOption

__all__ = ["LibraryContentsFolderCreatePayload"]


@dataclass
class LibraryContentsFolderCreatePayload:
    """
    LibraryContentsFolderCreatePayload dataclass.

    Args:
        create_type (CreateType) :
        folder_id (str)          : the encoded id of the parent folder of the new item
        description (Optional[str])
                                 :
        extended_metadata (Optional[ExtendedMetadata])
                                 : sub-dictionary containing any extended metadata to
                                   associate with the item
        from_hda_id (Optional[FromHdaId])
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDA to copy into the library
        from_hdca_id (Optional[FromHdcaId])
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDCA to copy into the library
        ldda_message (Optional[str])
                                 : the new message attribute of the LDDA created
        name (Optional[str])     :
        tag_using_filenames (Optional[bool])
                                 : create tags on datasets using the file's original name
        tags (Optional[Tags])    : create the given list of tags on datasets
        upload_option (Optional[UploadOption])
                                 :
    """

    create_type: CreateType
    folder_id: str  # the encoded id of the parent folder of the new item
    description: str | None = ""
    extended_metadata: ExtendedMetadata | None = (
        None  # sub-dictionary containing any extended metadata to associate with the item
    )
    from_hda_id: FromHdaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDA to copy into the library
    )
    from_hdca_id: FromHdcaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDCA to copy into the library
    )
    ldda_message: str | None = ""  # the new message attribute of the LDDA created
    name: str | None = ""
    tag_using_filenames: bool | None = False  # create tags on datasets using the file's original name
    tags: Tags | None = None  # create the given list of tags on datasets
    upload_option: UploadOption | None = "upload_file"
