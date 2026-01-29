from dataclasses import dataclass

__all__ = ["CleanupStorageItemsRequest"]


@dataclass
class CleanupStorageItemsRequest:
    """
    CleanupStorageItemsRequest dataclass

    Args:
        item_ids (List[str])     :
    """

    item_ids: list[str]

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "item_ids": "item_ids",
        }
        key_transform_with_dump = {
            "item_ids": "item_ids",
        }
