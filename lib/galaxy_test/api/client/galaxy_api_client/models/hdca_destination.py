from dataclasses import dataclass

__all__ = ["HdcaDestination"]


@dataclass
class HdcaDestination:
    """
    HdcaDestination dataclass

    Args:
        type_ (str)              : Maps from 'type'
    """

    type_: str  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "type": "type_",
        }
        key_transform_with_dump = {
            "type_": "type",
        }
