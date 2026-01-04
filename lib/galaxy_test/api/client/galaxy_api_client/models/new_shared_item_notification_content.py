from dataclasses import dataclass

from .item_type import ItemType

__all__ = ["NewSharedItemNotificationContent"]


@dataclass
class NewSharedItemNotificationContent:
    """
    NewSharedItemNotificationContent dataclass.

    Args:
        item_name (str)          : The name of the shared item.
        item_type (ItemType)     : The type of the shared item.
        owner_name (str)         : The name of the owner of the shared item.
        slug (str)               : The slug of the shared item. Used for the link to the
                                   item.
        category (Optional[str]) :
    """

    item_name: str  # The name of the shared item.
    item_type: ItemType  # The type of the shared item.
    owner_name: str  # The name of the owner of the shared item.
    slug: str  # The slug of the shared item. Used for the link to the item.
    category: str | None = "new_shared_item"
