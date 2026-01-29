from dataclasses import dataclass, field

from .create_type import CreateType
from .library_contents_collection_create_payload_element_identifiers import (
    LibraryContentsCollectionCreatePayloadElementIdentifiers,
)
from .library_contents_collection_create_payload_extended_metadata import (
    LibraryContentsCollectionCreatePayloadExtendedMetadata,
)
from .library_contents_collection_create_payload_from_hda_id import LibraryContentsCollectionCreatePayloadFromHdaId
from .library_contents_collection_create_payload_from_hdca_id import LibraryContentsCollectionCreatePayloadFromHdcaId
from .library_contents_collection_create_payload_name import LibraryContentsCollectionCreatePayloadName
from .upload_option import UploadOption

__all__ = ["LibraryContentsCollectionCreatePayload"]


@dataclass
class LibraryContentsCollectionCreatePayload:
    """
    LibraryContentsCollectionCreatePayload dataclass

    Args:
        collection_type (str)    :
        create_type (CreateType) :
        element_identifiers (LibraryContentsCollectionCreatePayloadElementIdentifiers)
                                 :
        folder_id (str)          : the encoded id of the parent folder of the new item
        copy_elements (bool | None)
                                 : if True, copy the elements into the collection
        extended_metadata (LibraryContentsCollectionCreatePayloadExtendedMetadata | None)
                                 : sub-dictionary containing any extended metadata to
                                   associate with the item
        from_hda_id (LibraryContentsCollectionCreatePayloadFromHdaId | None)
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDA to copy into the library
        from_hdca_id (LibraryContentsCollectionCreatePayloadFromHdcaId | None)
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDCA to copy into the library
        hide_source_items (bool | None)
                                 : if True, hide the source items in the collection
        ldda_message (str | None): the new message attribute of the LDDA created
        name (LibraryContentsCollectionCreatePayloadName | None)
                                 :
        tag_using_filenames (bool | None)
                                 : create tags on datasets using the file's original name
        tags (List[str] | None)  : create the given list of tags on datasets
        upload_option (UploadOption | None)
                                 :
    """

    collection_type: str
    create_type: CreateType
    element_identifiers: LibraryContentsCollectionCreatePayloadElementIdentifiers
    folder_id: str  # the encoded id of the parent folder of the new item
    copy_elements: bool | None = False  # if True, copy the elements into the collection
    extended_metadata: LibraryContentsCollectionCreatePayloadExtendedMetadata | None = (
        None  # sub-dictionary containing any extended metadata to associate with the item
    )
    from_hda_id: LibraryContentsCollectionCreatePayloadFromHdaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDA to copy into the library
    )
    from_hdca_id: LibraryContentsCollectionCreatePayloadFromHdcaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDCA to copy into the library
    )
    hide_source_items: bool | None = False  # if True, hide the source items in the collection
    ldda_message: str | None = ""  # the new message attribute of the LDDA created
    name: LibraryContentsCollectionCreatePayloadName | None = None
    tag_using_filenames: bool | None = False  # create tags on datasets using the file's original name
    tags: list[str] | None = field(default_factory=list)  # create the given list of tags on datasets
    upload_option: UploadOption | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "collection_type": "collection_type",
            "copy_elements": "copy_elements",
            "create_type": "create_type",
            "element_identifiers": "element_identifiers",
            "extended_metadata": "extended_metadata",
            "folder_id": "folder_id",
            "from_hda_id": "from_hda_id",
            "from_hdca_id": "from_hdca_id",
            "hide_source_items": "hide_source_items",
            "ldda_message": "ldda_message",
            "name": "name",
            "tag_using_filenames": "tag_using_filenames",
            "tags": "tags",
            "upload_option": "upload_option",
        }
        key_transform_with_dump = {
            "collection_type": "collection_type",
            "copy_elements": "copy_elements",
            "create_type": "create_type",
            "element_identifiers": "element_identifiers",
            "extended_metadata": "extended_metadata",
            "folder_id": "folder_id",
            "from_hda_id": "from_hda_id",
            "from_hdca_id": "from_hdca_id",
            "hide_source_items": "hide_source_items",
            "ldda_message": "ldda_message",
            "name": "name",
            "tag_using_filenames": "tag_using_filenames",
            "tags": "tags",
            "upload_option": "upload_option",
        }
