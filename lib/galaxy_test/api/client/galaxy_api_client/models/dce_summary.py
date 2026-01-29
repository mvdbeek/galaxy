from dataclasses import dataclass
from typing import Any

from .dce_summary_columns import DceSummaryColumns
from .dce_summary_element_type import DceSummaryElementType

__all__ = ["DceSummary"]


@dataclass
class DceSummary:
    """
    Dataset Collection Element summary information.

    Args:
        element_identifier (str) : The actual name of this element.
        element_index (int)      : The position index of this element inside the collection.
        id_ (str)                : Maps from 'id'
        model_class (str)        : The name of the database model class.
        columns (DceSummaryColumns | None)
                                 : A row (or list of columns) of data associated with this
                                   element
        element_type (DceSummaryElementType | None)
                                 : The type of the element. Used to interpret the `object`
                                   field.
        object_ (dict[str, Any] | None)
                                 : The element's specific data depending on the value of
                                   `element_type`. (maps from 'object')
    """

    element_identifier: str  # The actual name of this element.
    element_index: int  # The position index of this element inside the collection.
    id_: str  # Maps from 'id'
    model_class: str  # The name of the database model class.
    columns: DceSummaryColumns | None = None  # A row (or list of columns) of data associated with this element
    element_type: DceSummaryElementType | None = None  # The type of the element. Used to interpret the `object` field.
    object_: dict[str, Any] | None = (
        None  # The element's specific data depending on the value of `element_type`. (maps from 'object')
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "columns": "columns",
            "element_identifier": "element_identifier",
            "element_index": "element_index",
            "element_type": "element_type",
            "id": "id_",
            "model_class": "model_class",
            "object": "object_",
        }
        key_transform_with_dump = {
            "columns": "columns",
            "element_identifier": "element_identifier",
            "element_index": "element_index",
            "element_type": "element_type",
            "id_": "id",
            "model_class": "model_class",
            "object_": "object",
        }
