from dataclasses import dataclass

from .columns import Columns
from .element_type import ElementType
from .object_ import Object_

__all__ = ["DceSummary9"]


@dataclass
class DceSummary9:
    """
    Dataset Collection Element summary information.

    Args:
        element_identifier (str) : The actual name of this element.
        element_index (int)      : The position index of this element inside the collection.
        id_ (str)                :
        model_class (str)        : The name of the database model class.
        columns (Optional[Columns])
                                 : A list of column names
        element_type (Optional[ElementType])
                                 : The type of the element. Used to interpret the `object`
                                   field.
        object_ (Optional[Object_])
                                 : The element's specific data depending on the value of
                                   `element_type`.
    """

    element_identifier: str  # The actual name of this element.
    element_index: int  # The position index of this element inside the collection.
    id_: str
    model_class: str  # The name of the database model class.
    columns: Columns | None = None  # A list of column names
    element_type: ElementType | None = None  # The type of the element. Used to interpret the `object` field.
    object_: Object_ | None = None  # The element's specific data depending on the value of `element_type`.
