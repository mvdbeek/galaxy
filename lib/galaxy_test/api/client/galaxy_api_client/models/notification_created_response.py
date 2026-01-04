from dataclasses import dataclass

from .notification_response import NotificationResponse

__all__ = ["NotificationCreatedResponse"]


@dataclass
class NotificationCreatedResponse:
    """
    NotificationCreatedResponse dataclass.

    Args:
        notification (NotificationResponse)
                                 : Basic common fields for all notification responses.
        total_notifications_sent (int)
                                 : The total number of notifications that were sent to the
                                   recipients.
    """

    notification: NotificationResponse  # Basic common fields for all notification responses.
    total_notifications_sent: int  # The total number of notifications that were sent to the recipients.
