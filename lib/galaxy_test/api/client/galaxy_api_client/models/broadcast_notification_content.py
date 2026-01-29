from dataclasses import dataclass

from .broadcast_notification_content_action_links import BroadcastNotificationContentActionLinks
from .notification_response_content_category_enum import NotificationResponseContentCategoryEnum

__all__ = ["BroadcastNotificationContent"]


@dataclass
class BroadcastNotificationContent:
    """
    BroadcastNotificationContent dataclass

    Args:
        message (str)            : The message of the notification (supports Markdown).
        subject (str)            : The subject of the notification.
        action_links (BroadcastNotificationContentActionLinks | None)
                                 : The optional action links (buttons) to be displayed in
                                   the notification.
        category (NotificationResponseContentCategoryEnum | None)
                                 :
    """

    message: str  # The message of the notification (supports Markdown).
    subject: str  # The subject of the notification.
    action_links: BroadcastNotificationContentActionLinks | None = (
        None  # The optional action links (buttons) to be displayed in the notification.
    )
    category: NotificationResponseContentCategoryEnum | None = NotificationResponseContentCategoryEnum.BROADCAST

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_links": "action_links",
            "category": "category",
            "message": "message",
            "subject": "subject",
        }
        key_transform_with_dump = {
            "action_links": "action_links",
            "category": "category",
            "message": "message",
            "subject": "subject",
        }
