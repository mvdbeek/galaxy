from dataclasses import dataclass

__all__ = ["StorageItemCleanupError"]


@dataclass
class StorageItemCleanupError:
    """
    StorageItemCleanupError dataclass.

    Args:
        error (str)              :
        item_id (str)            :
    """

    error: str
    item_id: str
