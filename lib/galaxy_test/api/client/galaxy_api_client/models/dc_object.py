from dataclasses import dataclass, field

from .column_definitions import ColumnDefinitions
from .contents_url import ContentsUrl
from .dce_summary_3 import DceSummary3
from .element_count import ElementCount
from .elements_datatypes import ElementsDatatypes
from .elements_states_dict import ElementsStatesDict

__all__ = ["DcObject"]


@dataclass
class DcObject:
    """
    Dataset Collection Object

    Args:
        collection_type (str)    : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        elements_datatypes (ElementsDatatypes)
                                 : A set containing all the different element datatypes in
                                   the collection.
        elements_deleted (int)   : The number of elements in the collection that are marked
                                   as deleted.
        elements_states (ElementsStatesDict)
                                 :
        id_ (str)                :
        model_class (str)        : The name of the database model class.
        column_definitions (Optional[ColumnDefinitions])
                                 : Column data associated with each element of this
                                   collection.
        contents_url (Optional[ContentsUrl])
                                 : The relative URL to access the contents of this History.
        element_count (Optional[ElementCount])
                                 : The number of elements contained in the dataset
                                   collection. It may be None or undefined if the collection
                                   could not be populated.
        elements (Optional[List[DceSummary3]])
                                 : The summary information of each of the elements inside
                                   the dataset collection.
        populated (Optional[bool]): Whether the dataset collection elements (and any
                                    subcollections elements) were successfully populated.
    """

    collection_type: str  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    elements_datatypes: ElementsDatatypes  # A set containing all the different element datatypes in the collection.
    elements_deleted: int  # The number of elements in the collection that are marked as deleted.
    elements_states: ElementsStatesDict
    id_: str
    model_class: str  # The name of the database model class.
    column_definitions: ColumnDefinitions | None = None  # Column data associated with each element of this collection.
    contents_url: ContentsUrl | None = None  # The relative URL to access the contents of this History.
    element_count: ElementCount | None = (
        None  # The number of elements contained in the dataset collection. It may be None or undefined if the collection could not be populated.
    )
    elements: list[DceSummary3] | None = field(
        default_factory=list
    )  # The summary information of each of the elements inside the dataset collection.
    populated: bool | None = (
        None  # Whether the dataset collection elements (and any subcollections elements) were successfully populated.
    )
