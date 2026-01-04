from dataclasses import dataclass

from .collection_source_type import CollectionSourceType
from .collection_type import CollectionType
from .element_identifiers import ElementIdentifiers
from .id_ import Id_
from .name import Name
from .tags import Tags

__all__ = ["CollectionElementIdentifier2"]


@dataclass
class CollectionElementIdentifier2:
    """
    CollectionElementIdentifier2 dataclass.

    Args:
        src (CollectionSourceType):
        collection_type (Optional[CollectionType])
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        element_identifiers (Optional[ElementIdentifiers])
                                 : List of elements that should be in the new collection.
        id_ (Optional[Id_])      : The encoded ID of the dataset/dataset collection.
        name (Optional[Name])    : The name of the creator.
        tags (Optional[Tags])    : The list of tags associated with the element.
    """

    src: CollectionSourceType
    collection_type: CollectionType | None = (
        None  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    )
    element_identifiers: ElementIdentifiers | None = None  # List of elements that should be in the new collection.
    id_: Id_ | None = None  # The encoded ID of the dataset/dataset collection.
    name: Name | None = None  # The name of the creator.
    tags: Tags | None = None  # The list of tags associated with the element.
