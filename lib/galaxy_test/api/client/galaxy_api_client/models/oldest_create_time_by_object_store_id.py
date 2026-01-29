from dataclasses import dataclass
from datetime import datetime

__all__ = ["OldestCreateTimeByObjectStoreId"]


@dataclass
class OldestCreateTimeByObjectStoreId:
    """
    Represents the oldest creation time of a set of datasets stored in a specific object
    store.

    Args:
        object_store_id (str)    : The ID of the object store.
        oldest_create_time (datetime)
                                 : The oldest creation time of a set of datasets stored in
                                   this object store.
    """

    object_store_id: str  # The ID of the object store.
    oldest_create_time: datetime  # The oldest creation time of a set of datasets stored in this object store.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "object_store_id": "object_store_id",
            "oldest_create_time": "oldest_create_time",
        }
        key_transform_with_dump = {
            "object_store_id": "object_store_id",
            "oldest_create_time": "oldest_create_time",
        }
