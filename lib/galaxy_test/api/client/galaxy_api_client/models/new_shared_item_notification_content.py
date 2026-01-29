from dataclasses import dataclass

from .new_shared_item_notification_content_item_type import NewSharedItemNotificationContentItemType
from .user_notification_response_content_category_enum import UserNotificationResponseContentCategoryEnum

__all__ = ["NewSharedItemNotificationContent"]


@dataclass
class NewSharedItemNotificationContent:
    """
    NewSharedItemNotificationContent dataclass

    Args:
        item_name (str)          : The name of the shared item.
        item_type (NewSharedItemNotificationContentItemType)
                                 : The type of the shared item.
        owner_name (str)         : The name of the owner of the shared item.
        slug (str)               : The slug of the shared item. Used for the link to the
                                   item.
        category (UserNotificationResponseContentCategoryEnum | None)
                                 :
    """

    item_name: str  # The name of the shared item.
    item_type: NewSharedItemNotificationContentItemType  # The type of the shared item.
    owner_name: str  # The name of the owner of the shared item.
    slug: str  # The slug of the shared item. Used for the link to the item.
    category: UserNotificationResponseContentCategoryEnum | None = (
        UserNotificationResponseContentCategoryEnum.NEW_SHARED_ITEM
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "category": "category",
            "item_name": "item_name",
            "item_type": "item_type",
            "owner_name": "owner_name",
            "slug": "slug",
        }
        key_transform_with_dump = {
            "category": "category",
            "item_name": "item_name",
            "item_type": "item_type",
            "owner_name": "owner_name",
            "slug": "slug",
        }
