from dataclasses import dataclass

from .dataset_source_type import DatasetSourceType

__all__ = ["DatasetSourceId"]


@dataclass
class DatasetSourceId:
    """
    DatasetSourceId dataclass.

    Args:
        id_ (str)                :
        src (DatasetSourceType)  :
    """

    id_: str
    src: DatasetSourceType
