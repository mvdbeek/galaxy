from dataclasses import dataclass, field

from .create_type import CreateType
from .library_contents_folder_create_payload_extended_metadata import LibraryContentsFolderCreatePayloadExtendedMetadata
from .library_contents_folder_create_payload_from_hda_id import LibraryContentsFolderCreatePayloadFromHdaId
from .library_contents_folder_create_payload_from_hdca_id import LibraryContentsFolderCreatePayloadFromHdcaId
from .upload_option import UploadOption

__all__ = ["LibraryContentsFolderCreatePayload"]


@dataclass
class LibraryContentsFolderCreatePayload:
    """
    LibraryContentsFolderCreatePayload dataclass

    Args:
        create_type (CreateType) :
        folder_id (str)          : the encoded id of the parent folder of the new item
        description (str | None) :
        extended_metadata (LibraryContentsFolderCreatePayloadExtendedMetadata | None)
                                 : sub-dictionary containing any extended metadata to
                                   associate with the item
        from_hda_id (LibraryContentsFolderCreatePayloadFromHdaId | None)
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDA to copy into the library
        from_hdca_id (LibraryContentsFolderCreatePayloadFromHdcaId | None)
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDCA to copy into the library
        ldda_message (str | None): the new message attribute of the LDDA created
        name (str | None)        :
        tag_using_filenames (bool | None)
                                 : create tags on datasets using the file's original name
        tags (List[str] | None)  : create the given list of tags on datasets
        upload_option (UploadOption | None)
                                 :
    """

    create_type: CreateType
    folder_id: str  # the encoded id of the parent folder of the new item
    description: str | None = ""
    extended_metadata: LibraryContentsFolderCreatePayloadExtendedMetadata | None = (
        None  # sub-dictionary containing any extended metadata to associate with the item
    )
    from_hda_id: LibraryContentsFolderCreatePayloadFromHdaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDA to copy into the library
    )
    from_hdca_id: LibraryContentsFolderCreatePayloadFromHdcaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDCA to copy into the library
    )
    ldda_message: str | None = ""  # the new message attribute of the LDDA created
    name: str | None = ""
    tag_using_filenames: bool | None = False  # create tags on datasets using the file's original name
    tags: list[str] | None = field(default_factory=list)  # create the given list of tags on datasets
    upload_option: UploadOption | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "create_type": "create_type",
            "description": "description",
            "extended_metadata": "extended_metadata",
            "folder_id": "folder_id",
            "from_hda_id": "from_hda_id",
            "from_hdca_id": "from_hdca_id",
            "ldda_message": "ldda_message",
            "name": "name",
            "tag_using_filenames": "tag_using_filenames",
            "tags": "tags",
            "upload_option": "upload_option",
        }
        key_transform_with_dump = {
            "create_type": "create_type",
            "description": "description",
            "extended_metadata": "extended_metadata",
            "folder_id": "folder_id",
            "from_hda_id": "from_hda_id",
            "from_hdca_id": "from_hdca_id",
            "ldda_message": "ldda_message",
            "name": "name",
            "tag_using_filenames": "tag_using_filenames",
            "tags": "tags",
            "upload_option": "upload_option",
        }
