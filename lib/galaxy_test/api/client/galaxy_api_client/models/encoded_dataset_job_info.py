from dataclasses import dataclass

from .data_item_source_type import DataItemSourceType
from .uuid__3 import Uuid3

__all__ = ["EncodedDatasetJobInfo"]


@dataclass
class EncodedDatasetJobInfo:
    """
    EncodedDatasetJobInfo dataclass

    Args:
        id_ (str)                : Maps from 'id'
        src (DataItemSourceType) :
        uuid_ (Uuid3 | None)     : Universal unique identifier for this dataset. (maps from
                                   'uuid')
    """

    id_: str  # Maps from 'id'
    src: DataItemSourceType
    uuid_: Uuid3 | None = None  # Universal unique identifier for this dataset. (maps from 'uuid')

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "src": "src",
            "uuid": "uuid_",
        }
        key_transform_with_dump = {
            "id_": "id",
            "src": "src",
            "uuid_": "uuid",
        }
