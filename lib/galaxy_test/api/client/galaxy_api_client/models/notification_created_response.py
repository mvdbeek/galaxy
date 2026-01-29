from dataclasses import dataclass

from .notification_response import NotificationResponse

__all__ = ["NotificationCreatedResponse"]


@dataclass
class NotificationCreatedResponse:
    """
    NotificationCreatedResponse dataclass

    Args:
        notification (NotificationResponse)
                                 : Basic common fields for all notification responses.
        total_notifications_sent (int)
                                 : The total number of notifications that were sent to the
                                   recipients.
    """

    notification: NotificationResponse  # Basic common fields for all notification responses.
    total_notifications_sent: int  # The total number of notifications that were sent to the recipients.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "notification": "notification",
            "total_notifications_sent": "total_notifications_sent",
        }
        key_transform_with_dump = {
            "notification": "notification",
            "total_notifications_sent": "total_notifications_sent",
        }
