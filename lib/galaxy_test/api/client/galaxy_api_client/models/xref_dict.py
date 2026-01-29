from dataclasses import dataclass

__all__ = ["XrefDict"]


@dataclass
class XrefDict:
    """
    XrefDict dataclass

    Args:
        type_ (str)              : Maps from 'type'
        value (str)              :
    """

    type_: str  # Maps from 'type'
    value: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "type": "type_",
            "value": "value",
        }
        key_transform_with_dump = {
            "type_": "type",
            "value": "value",
        }
