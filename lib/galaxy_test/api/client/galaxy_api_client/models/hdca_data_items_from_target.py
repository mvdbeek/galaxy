from dataclasses import dataclass

from .collection_type import CollectionType
from .column_definitions import ColumnDefinitions
from .elements_from_type import ElementsFromType
from .ftp_path import FtpPath
from .hdca_destination import HdcaDestination
from .items_from_src import ItemsFromSrc
from .name import Name
from .path import Path
from .server_dir import ServerDir
from .tags import Tags
from .url import Url

__all__ = ["HdcaDataItemsFromTarget"]


@dataclass
class HdcaDataItemsFromTarget:
    """
    HdcaDataItemsFromTarget dataclass.

    Args:
        destination (HdcaDestination)
                                 :
        items_from (ElementsFromType)
                                 :
        src (ItemsFromSrc)       :
        auto_decompress (Optional[bool])
                                 : This is a boolean value that indicates whether the
                                   dataset should be automatically decompressed if it is
                                   compressed. If set to true, Galaxy will attempt to
                                   decompress the dataset if it is compressed and it is not
                                   explicitly set to a compressed datatype.
        collection_type (Optional[CollectionType])
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        column_definitions (Optional[ColumnDefinitions])
                                 : Column data associated with each element of this
                                   collection.
        ftp_path (Optional[FtpPath])
                                 :
        name (Optional[Name])    : The name of the creator.
        path (Optional[Path])    :
        server_dir (Optional[ServerDir])
                                 :
        tags (Optional[Tags])    : The collection of tags associated with an item.
        url (Optional[Url])      : The relative URL to access this item.
    """

    destination: HdcaDestination
    items_from: ElementsFromType
    src: ItemsFromSrc
    auto_decompress: bool | None = (
        False  # This is a boolean value that indicates whether the dataset should be automatically decompressed if it is compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not explicitly set to a compressed datatype.
    )
    collection_type: CollectionType | None = (
        None  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    )
    column_definitions: ColumnDefinitions | None = None  # Column data associated with each element of this collection.
    ftp_path: FtpPath | None = None
    name: Name | None = None  # The name of the creator.
    path: Path | None = None
    server_dir: ServerDir | None = ""
    tags: Tags | None = None  # The collection of tags associated with an item.
    url: Url | None = None  # The relative URL to access this item.
