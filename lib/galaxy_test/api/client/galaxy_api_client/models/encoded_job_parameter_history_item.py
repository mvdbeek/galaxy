from dataclasses import dataclass

from .data_item_source_type import DataItemSourceType
from .encoded_job_parameter_history_item_hid import EncodedJobParameterHistoryItemHid

__all__ = ["EncodedJobParameterHistoryItem"]


@dataclass
class EncodedJobParameterHistoryItem:
    """
    EncodedJobParameterHistoryItem dataclass

    Args:
        id_ (str)                : Maps from 'id'
        name (str)               :
        src (DataItemSourceType) :
        hid (EncodedJobParameterHistoryItemHid | None)
                                 :
    """

    id_: str  # Maps from 'id'
    name: str
    src: DataItemSourceType
    hid: EncodedJobParameterHistoryItemHid | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "hid": "hid",
            "id": "id_",
            "name": "name",
            "src": "src",
        }
        key_transform_with_dump = {
            "hid": "hid",
            "id_": "id",
            "name": "name",
            "src": "src",
        }
