from dataclasses import dataclass

from .elements import Elements

__all__ = ["CollectionElementCollectionRequestUri"]


@dataclass
class CollectionElementCollectionRequestUri:
    """
    CollectionElementCollectionRequestUri dataclass.

    Args:
        class_ (str)             :
        collection_type (str)    :
        elements (Elements)      :
        identifier (str)         : A unique identifier for this element within the
                                   collection.
    """

    class_: str
    collection_type: str
    elements: Elements
    identifier: str  # A unique identifier for this element within the collection.
