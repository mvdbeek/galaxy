from dataclasses import dataclass

from .elements import Elements
from .name import Name
from .src import Src

__all__ = ["DataRequestCollectionUri"]


@dataclass
class DataRequestCollectionUri:
    """
    DataRequestCollectionUri dataclass.

    Args:
        class_ (str)             :
        collection_type (str)    :
        elements (Elements)      :
        deferred (Optional[bool]):
        name (Optional[Name])    : The name of the creator.
        src (Optional[Src])      : Source type of the input dataset/dataset collection.
    """

    class_: str
    collection_type: str
    elements: Elements
    deferred: bool | None = False
    name: Name | None = None  # The name of the creator.
    src: Src | None = None  # Source type of the input dataset/dataset collection.
