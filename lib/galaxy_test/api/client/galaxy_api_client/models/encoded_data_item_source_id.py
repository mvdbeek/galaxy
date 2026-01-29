from dataclasses import dataclass

from .data_item_source_type import DataItemSourceType

__all__ = ["EncodedDataItemSourceId"]


@dataclass
class EncodedDataItemSourceId:
    """
    EncodedDataItemSourceId dataclass

    Args:
        id_ (str)                : Maps from 'id'
        src (DataItemSourceType) :
    """

    id_: str  # Maps from 'id'
    src: DataItemSourceType

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "src": "src",
        }
        key_transform_with_dump = {
            "id_": "id",
            "src": "src",
        }
