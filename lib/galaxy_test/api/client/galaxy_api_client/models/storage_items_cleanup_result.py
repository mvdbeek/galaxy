from dataclasses import dataclass

from .storage_item_cleanup_error import StorageItemCleanupError

__all__ = ["StorageItemsCleanupResult"]


@dataclass
class StorageItemsCleanupResult:
    """
    StorageItemsCleanupResult dataclass

    Args:
        errors (List[StorageItemCleanupError])
                                 :
        success_item_count (int) :
        total_free_bytes (int)   :
        total_item_count (int)   :
    """

    errors: list[StorageItemCleanupError]
    success_item_count: int
    total_free_bytes: int
    total_item_count: int

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "errors": "errors",
            "success_item_count": "success_item_count",
            "total_free_bytes": "total_free_bytes",
            "total_item_count": "total_item_count",
        }
        key_transform_with_dump = {
            "errors": "errors",
            "success_item_count": "success_item_count",
            "total_free_bytes": "total_free_bytes",
            "total_item_count": "total_item_count",
        }
