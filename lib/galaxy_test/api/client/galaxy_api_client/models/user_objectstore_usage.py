from dataclasses import dataclass

__all__ = ["UserObjectstoreUsage"]


@dataclass
class UserObjectstoreUsage:
    """
    UserObjectstoreUsage dataclass

    Args:
        object_store_id (str)    :
        total_disk_usage (float) :
    """

    object_store_id: str
    total_disk_usage: float

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "object_store_id": "object_store_id",
            "total_disk_usage": "total_disk_usage",
        }
        key_transform_with_dump = {
            "object_store_id": "object_store_id",
            "total_disk_usage": "total_disk_usage",
        }
