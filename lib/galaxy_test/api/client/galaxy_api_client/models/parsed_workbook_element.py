from dataclasses import dataclass

from .object__2 import Object2
from .parsed_workbook_element_element_type import ParsedWorkbookElementElementType

__all__ = ["ParsedWorkbookElement"]


@dataclass
class ParsedWorkbookElement:
    """
    ParsedWorkbookElement dataclass

    Args:
        element_identifier (str) :
        element_index (int)      :
        element_type (ParsedWorkbookElementElementType)
                                 :
        object_ (Object2)        : Maps from 'object'
    """

    element_identifier: str
    element_index: int
    element_type: ParsedWorkbookElementElementType
    object_: Object2  # Maps from 'object'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "element_identifier": "element_identifier",
            "element_index": "element_index",
            "element_type": "element_type",
            "object": "object_",
        }
        key_transform_with_dump = {
            "element_identifier": "element_identifier",
            "element_index": "element_index",
            "element_type": "element_type",
            "object_": "object",
        }
