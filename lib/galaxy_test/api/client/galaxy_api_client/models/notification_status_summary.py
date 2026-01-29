from dataclasses import dataclass

from .broadcast_notification_response import BroadcastNotificationResponse
from .user_notification_response import UserNotificationResponse

__all__ = ["NotificationStatusSummary"]


@dataclass
class NotificationStatusSummary:
    """
    A summary of the notification status for a user. Contains only updates since a
    particular timestamp.

    Args:
        broadcasts (List[BroadcastNotificationResponse])
                                 : The list of updated broadcasts.
        notifications (List[UserNotificationResponse])
                                 : The list of updated notifications for the user.
        total_unread_count (int) : The total number of unread notifications for the user.
    """

    broadcasts: list[BroadcastNotificationResponse]  # The list of updated broadcasts.
    notifications: list[UserNotificationResponse]  # The list of updated notifications for the user.
    total_unread_count: int  # The total number of unread notifications for the user.
