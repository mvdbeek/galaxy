from dataclasses import dataclass

from .collection_type import CollectionType
from .column_definitions import ColumnDefinitions
from .elements import Elements
from .hdca_destination import HdcaDestination
from .name import Name
from .tags import Tags

__all__ = ["HdcaDataItemsTarget"]


@dataclass
class HdcaDataItemsTarget:
    """
    HdcaDataItemsTarget dataclass.

    Args:
        destination (HdcaDestination)
                                 :
        elements (Elements)      :
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
        name (Optional[Name])    : The name of the creator.
        tags (Optional[Tags])    : The collection of tags associated with an item.
    """

    destination: HdcaDestination
    elements: Elements
    auto_decompress: bool | None = (
        False  # This is a boolean value that indicates whether the dataset should be automatically decompressed if it is compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not explicitly set to a compressed datatype.
    )
    collection_type: CollectionType | None = (
        None  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    )
    column_definitions: ColumnDefinitions | None = None  # Column data associated with each element of this collection.
    name: Name | None = None  # The name of the creator.
    tags: Tags | None = None  # The collection of tags associated with an item.
