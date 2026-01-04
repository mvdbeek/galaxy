from dataclasses import dataclass

from .notification_ids import NotificationIds
from .user_notification_update_request import UserNotificationUpdateRequest

__all__ = ["UserNotificationsBatchUpdateRequest"]


@dataclass
class UserNotificationsBatchUpdateRequest:
    """
    A batch update request specific for user notifications.

    Args:
        changes (UserNotificationUpdateRequest)
                                 : A notification update request specific to the user.
        notification_ids (NotificationIds)
                                 : The list of encoded notification IDs of the notifications
                                   that should be updated.
    """

    changes: UserNotificationUpdateRequest  # A notification update request specific to the user.
    notification_ids: (
        NotificationIds  # The list of encoded notification IDs of the notifications that should be updated.
    )
