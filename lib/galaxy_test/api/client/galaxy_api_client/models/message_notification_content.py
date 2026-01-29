from dataclasses import dataclass

from .user_notification_response_content_category_enum import UserNotificationResponseContentCategoryEnum

__all__ = ["MessageNotificationContent"]


@dataclass
class MessageNotificationContent:
    """
    MessageNotificationContent dataclass

    Args:
        message (str)            : The message of the notification (supports Markdown).
        subject (str)            : The subject of the notification.
        category (UserNotificationResponseContentCategoryEnum | None)
                                 :
    """

    message: str  # The message of the notification (supports Markdown).
    subject: str  # The subject of the notification.
    category: UserNotificationResponseContentCategoryEnum | None = UserNotificationResponseContentCategoryEnum.MESSAGE

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "category": "category",
            "message": "message",
            "subject": "subject",
        }
        key_transform_with_dump = {
            "category": "category",
            "message": "message",
            "subject": "subject",
        }
