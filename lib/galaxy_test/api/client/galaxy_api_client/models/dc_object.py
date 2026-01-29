from dataclasses import dataclass, field

from .dc_object_column_definitions import DcObjectColumnDefinitions
from .dc_object_contents_url import DcObjectContentsUrl
from .dc_object_element_count import DcObjectElementCount
from .dce_summary import DceSummary
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
        elements_datatypes (List[str])
                                 : A set containing all the different element datatypes in
                                   the collection.
        elements_deleted (int)   : The number of elements in the collection that are marked
                                   as deleted.
        elements_states (ElementsStatesDict)
                                 :
        id_ (str)                : Maps from 'id'
        model_class (str)        : The name of the database model class.
        column_definitions (DcObjectColumnDefinitions | None)
                                 : Column definitions for sample sheet collections.
        contents_url (DcObjectContentsUrl | None)
                                 :
        element_count (DcObjectElementCount | None)
                                 : The number of elements contained in the dataset
                                   collection. It may be None or undefined if the collection
                                   could not be populated.
        elements (List[DceSummary] | None)
                                 : The summary information of each of the elements inside
                                   the dataset collection.
        populated (bool | None)  : Whether the dataset collection elements (and any
                                   subcollections elements) were successfully populated.
    """

    collection_type: str  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    elements_datatypes: list[str]  # A set containing all the different element datatypes in the collection.
    elements_deleted: int  # The number of elements in the collection that are marked as deleted.
    elements_states: ElementsStatesDict
    id_: str  # Maps from 'id'
    model_class: str  # The name of the database model class.
    column_definitions: DcObjectColumnDefinitions | None = None  # Column definitions for sample sheet collections.
    contents_url: DcObjectContentsUrl | None = None
    element_count: DcObjectElementCount | None = (
        None  # The number of elements contained in the dataset collection. It may be None or undefined if the collection could not be populated.
    )
    elements: list[DceSummary] | None = field(
        default_factory=list
    )  # The summary information of each of the elements inside the dataset collection.
    populated: bool | None = (
        None  # Whether the dataset collection elements (and any subcollections elements) were successfully populated.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "contents_url": "contents_url",
            "element_count": "element_count",
            "elements": "elements",
            "elements_datatypes": "elements_datatypes",
            "elements_deleted": "elements_deleted",
            "elements_states": "elements_states",
            "id": "id_",
            "model_class": "model_class",
            "populated": "populated",
        }
        key_transform_with_dump = {
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "contents_url": "contents_url",
            "element_count": "element_count",
            "elements": "elements",
            "elements_datatypes": "elements_datatypes",
            "elements_deleted": "elements_deleted",
            "elements_states": "elements_states",
            "id_": "id",
            "model_class": "model_class",
            "populated": "populated",
        }
