from dataclasses import dataclass

from .data_item_source_type import DataItemSourceType

__all__ = ["EncodedDataItemSourceId"]


@dataclass
class EncodedDataItemSourceId:
    """
    EncodedDataItemSourceId dataclass.

    Args:
        id_ (str)                :
        src (DataItemSourceType) :
    """

    id_: str
    src: DataItemSourceType
