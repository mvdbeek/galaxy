from dataclasses import dataclass

__all__ = ["ChangeDbkeyOperationParams"]


@dataclass
class ChangeDbkeyOperationParams:
    """
    ChangeDbkeyOperationParams dataclass

    Args:
        dbkey (str)              :
        type_ (str)              : Maps from 'type'
    """

    dbkey: str
    type_: str  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "dbkey": "dbkey",
            "type": "type_",
        }
        key_transform_with_dump = {
            "dbkey": "dbkey",
            "type_": "type",
        }
