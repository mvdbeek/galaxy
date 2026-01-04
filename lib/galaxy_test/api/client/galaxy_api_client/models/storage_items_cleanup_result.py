from dataclasses import dataclass

from .storage_item_cleanup_error import StorageItemCleanupError

__all__ = ["StorageItemsCleanupResult"]


@dataclass
class StorageItemsCleanupResult:
    """
    StorageItemsCleanupResult dataclass.

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
