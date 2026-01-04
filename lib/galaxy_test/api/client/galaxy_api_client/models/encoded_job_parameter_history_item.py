from dataclasses import dataclass

from .data_item_source_type import DataItemSourceType
from .hid import Hid

__all__ = ["EncodedJobParameterHistoryItem"]


@dataclass
class EncodedJobParameterHistoryItem:
    """
    EncodedJobParameterHistoryItem dataclass.

    Args:
        id_ (str)                :
        name (str)               :
        src (DataItemSourceType) :
        hid (Optional[Hid])      : The index position of this item in the History.
    """

    id_: str
    name: str
    src: DataItemSourceType
    hid: Hid | None = None  # The index position of this item in the History.
