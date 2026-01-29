from dataclasses import dataclass

from .dataset_source_type import DatasetSourceType

__all__ = ["DatasetSourceId"]


@dataclass
class DatasetSourceId:
    """
    DatasetSourceId dataclass

    Args:
        id_ (str)                : Maps from 'id'
        src (DatasetSourceType)  :
    """

    id_: str  # Maps from 'id'
    src: DatasetSourceType

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
