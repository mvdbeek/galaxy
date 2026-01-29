from dataclasses import dataclass

from .user_notification_update_request import UserNotificationUpdateRequest

__all__ = ["UserNotificationsBatchUpdateRequest"]


@dataclass
class UserNotificationsBatchUpdateRequest:
    """
    A batch update request specific for user notifications.

    Args:
        changes (UserNotificationUpdateRequest)
                                 : A notification update request specific to the user.
        notification_ids (List[str])
                                 : The list of encoded notification IDs of the notifications
                                   that should be updated.
    """

    changes: UserNotificationUpdateRequest  # A notification update request specific to the user.
    notification_ids: list[str]  # The list of encoded notification IDs of the notifications that should be updated.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "changes": "changes",
            "notification_ids": "notification_ids",
        }
        key_transform_with_dump = {
            "changes": "changes",
            "notification_ids": "notification_ids",
        }
