from dataclasses import dataclass

from .create_type import CreateType
from .element_identifiers import ElementIdentifiers
from .extended_metadata import ExtendedMetadata
from .from_hda_id import FromHdaId
from .from_hdca_id import FromHdcaId
from .name import Name
from .tags import Tags
from .upload_option import UploadOption

__all__ = ["LibraryContentsCollectionCreatePayload"]


@dataclass
class LibraryContentsCollectionCreatePayload:
    """
    LibraryContentsCollectionCreatePayload dataclass.

    Args:
        collection_type (str)    :
        create_type (CreateType) :
        element_identifiers (Optional[ElementIdentifiers])
                                 : List of elements that should be in the new collection.
        folder_id (str)          : the encoded id of the parent folder of the new item
        copy_elements (Optional[bool])
                                 : if True, copy the elements into the collection
        extended_metadata (Optional[ExtendedMetadata])
                                 : sub-dictionary containing any extended metadata to
                                   associate with the item
        from_hda_id (Optional[FromHdaId])
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDA to copy into the library
        from_hdca_id (Optional[FromHdcaId])
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDCA to copy into the library
        hide_source_items (Optional[bool])
                                 : if True, hide the source items in the collection
        ldda_message (Optional[str])
                                 : the new message attribute of the LDDA created
        name (Optional[Name])    : The name of the creator.
        tag_using_filenames (Optional[bool])
                                 : create tags on datasets using the file's original name
        tags (Optional[Tags])    : create the given list of tags on datasets
        upload_option (Optional[UploadOption])
                                 :
    """

    collection_type: str
    create_type: CreateType
    element_identifiers: ElementIdentifiers | None  # List of elements that should be in the new collection.
    folder_id: str  # the encoded id of the parent folder of the new item
    copy_elements: bool | None = False  # if True, copy the elements into the collection
    extended_metadata: ExtendedMetadata | None = (
        None  # sub-dictionary containing any extended metadata to associate with the item
    )
    from_hda_id: FromHdaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDA to copy into the library
    )
    from_hdca_id: FromHdcaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDCA to copy into the library
    )
    hide_source_items: bool | None = False  # if True, hide the source items in the collection
    ldda_message: str | None = ""  # the new message attribute of the LDDA created
    name: Name | None = None  # The name of the creator.
    tag_using_filenames: bool | None = False  # create tags on datasets using the file's original name
    tags: Tags | None = None  # create the given list of tags on datasets
    upload_option: UploadOption | None = "upload_file"
