from dataclasses import dataclass

from .badge_dict_message import BadgeDictMessage
from .badge_dict_source import BadgeDictSource
from .type__2 import Type2

__all__ = ["BadgeDict"]


@dataclass
class BadgeDict:
    """
    BadgeDict dataclass

    Args:
        message (BadgeDictMessage):
        source (BadgeDictSource) :
        type_ (Type2)            : Maps from 'type'
    """

    message: BadgeDictMessage
    source: BadgeDictSource
    type_: Type2  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "message": "message",
            "source": "source",
            "type": "type_",
        }
        key_transform_with_dump = {
            "message": "message",
            "source": "source",
            "type_": "type",
        }
