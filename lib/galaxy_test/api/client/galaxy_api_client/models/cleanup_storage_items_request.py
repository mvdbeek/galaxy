from dataclasses import dataclass

from .item_ids import ItemIds

__all__ = ["CleanupStorageItemsRequest"]


@dataclass
class CleanupStorageItemsRequest:
    """
    CleanupStorageItemsRequest dataclass.

    Args:
        item_ids (ItemIds)       :
    """

    item_ids: ItemIds
