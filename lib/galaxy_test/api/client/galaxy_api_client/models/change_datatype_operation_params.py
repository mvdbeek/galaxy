from dataclasses import dataclass

__all__ = ["ChangeDatatypeOperationParams"]


@dataclass
class ChangeDatatypeOperationParams:
    """
    ChangeDatatypeOperationParams dataclass

    Args:
        datatype (str)           :
        type_ (str)              : Maps from 'type'
    """

    datatype: str
    type_: str  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "datatype": "datatype",
            "type": "type_",
        }
        key_transform_with_dump = {
            "datatype": "datatype",
            "type_": "type",
        }
