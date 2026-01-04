from dataclasses import dataclass

from .notification_ids import NotificationIds

__all__ = ["NotificationsBatchRequest"]


@dataclass
class NotificationsBatchRequest:
    """
    NotificationsBatchRequest dataclass.

    Args:
        notification_ids (NotificationIds)
                                 : The list of encoded notification IDs of the notifications
                                   that should be updated.
    """

    notification_ids: (
        NotificationIds  # The list of encoded notification IDs of the notifications that should be updated.
    )
