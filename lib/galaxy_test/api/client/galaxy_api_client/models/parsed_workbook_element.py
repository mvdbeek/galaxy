from dataclasses import dataclass

from .element_type import ElementType
from .object_ import Object_

__all__ = ["ParsedWorkbookElement"]


@dataclass
class ParsedWorkbookElement:
    """
    ParsedWorkbookElement dataclass.

    Args:
        element_identifier (str) :
        element_index (int)      :
        element_type (Optional[ElementType])
                                 : The type of the element. Used to interpret the `object`
                                   field.
        object_ (Optional[Object_])
                                 : The element's specific data depending on the value of
                                   `element_type`.
    """

    element_identifier: str
    element_index: int
    element_type: ElementType | None  # The type of the element. Used to interpret the `object` field.
    object_: Object_ | None  # The element's specific data depending on the value of `element_type`.
