from dataclasses import dataclass

from .type__9 import Type9

__all__ = ["ParsedColumn"]


@dataclass
class ParsedColumn:
    """
    ParsedColumn dataclass

    Args:
        title (str)              :
        type_ (Type9)            : Maps from 'type'
        type_index (int)         :
    """

    title: str
    type_: Type9  # Maps from 'type'
    type_index: int

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "title": "title",
            "type": "type_",
            "type_index": "type_index",
        }
        key_transform_with_dump = {
            "title": "title",
            "type_": "type",
            "type_index": "type_index",
        }
