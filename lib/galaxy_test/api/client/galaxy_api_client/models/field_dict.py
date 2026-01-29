from dataclasses import dataclass

from .format__5 import Format5
from .type__4 import Type4

__all__ = ["FieldDict"]


@dataclass
class FieldDict:
    """
    FieldDict dataclass

    Args:
        name (str)               :
        type_ (Type4)            : Maps from 'type'
        format_ (Format5 | None) : Maps from 'format'
    """

    name: str
    type_: Type4  # Maps from 'type'
    format_: Format5 | None = None  # Maps from 'format'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "format": "format_",
            "name": "name",
            "type": "type_",
        }
        key_transform_with_dump = {
            "format_": "format",
            "name": "name",
            "type_": "type",
        }
