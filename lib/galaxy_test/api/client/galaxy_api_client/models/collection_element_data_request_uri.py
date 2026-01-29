from dataclasses import dataclass

from .created_from_basename import CreatedFromBasename
from .hashes import Hashes
from .info import Info
from .name import Name
from .src import Src
from .tags import Tags

__all__ = ["CollectionElementDataRequestUri"]


@dataclass
class CollectionElementDataRequestUri:
    """
    CollectionElementDataRequestUri dataclass.

    Args:
        class_ (str)             :
        ext (str)                :
        identifier (str)         : A unique identifier for this element within the
                                   collection.
        location (str)           :
        created_from_basename (Optional[CreatedFromBasename])
                                 : The basename of the output that produced this dataset.
        dbkey (Optional[str])    :
        deferred (Optional[bool]):
        hashes (Optional[Hashes]): List of precomputed hashes for the file, if available.
        info (Optional[Info])    : Free text field that can be used to store arbitrary
                                   information about the dataset. This used to be
                                   prominently displayed in the Galaxy user interface, but
                                   now is largely unused.
        name (Optional[Name])    : The name of the creator.
        space_to_tab (Optional[bool])
                                 :
        src (Optional[Src])      : Source type of the input dataset/dataset collection.
        tags (Optional[Tags])    : The collection of tags associated with an item.
        to_posix_lines (Optional[bool])
                                 :
    """

    class_: str
    ext: str
    identifier: str  # A unique identifier for this element within the collection.
    location: str
    created_from_basename: CreatedFromBasename | None = None  # The basename of the output that produced this dataset.
    dbkey: str | None = "?"
    deferred: bool | None = False
    hashes: Hashes | None = None  # List of precomputed hashes for the file, if available.
    info: Info | None = (
        None  # Free text field that can be used to store arbitrary information about the dataset. This used to be prominently displayed in the Galaxy user interface, but now is largely unused.
    )
    name: Name | None = None  # The name of the creator.
    space_to_tab: bool | None = False
    src: Src | None = None  # Source type of the input dataset/dataset collection.
    tags: Tags | None = None  # The collection of tags associated with an item.
    to_posix_lines: bool | None = False
