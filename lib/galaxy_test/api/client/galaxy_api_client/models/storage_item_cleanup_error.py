from dataclasses import dataclass

__all__ = ["StorageItemCleanupError"]


@dataclass
class StorageItemCleanupError:
    """
    StorageItemCleanupError dataclass

    Args:
        error (str)              :
        item_id (str)            :
    """

    error: str
    item_id: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "error": "error",
            "item_id": "item_id",
        }
        key_transform_with_dump = {
            "error": "error",
            "item_id": "item_id",
        }
