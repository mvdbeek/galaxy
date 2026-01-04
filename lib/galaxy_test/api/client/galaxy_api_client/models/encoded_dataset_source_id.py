from dataclasses import dataclass

from .dataset_source_type import DatasetSourceType

__all__ = ["EncodedDatasetSourceId"]


@dataclass
class EncodedDatasetSourceId:
    """
    EncodedDatasetSourceId dataclass.

    Args:
        id_ (str)                :
        src (DatasetSourceType)  :
    """

    id_: str
    src: DatasetSourceType
