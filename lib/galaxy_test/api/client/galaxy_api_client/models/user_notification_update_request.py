from dataclasses import dataclass

from .user_notification_update_request_deleted import UserNotificationUpdateRequestDeleted
from .user_notification_update_request_seen import UserNotificationUpdateRequestSeen

__all__ = ["UserNotificationUpdateRequest"]


@dataclass
class UserNotificationUpdateRequest:
    """
    A notification update request specific to the user.

    Args:
        deleted (UserNotificationUpdateRequestDeleted | None)
                                 : Whether the notification should be marked as deleted by
                                   the user. If not set, the notification will not be
                                   changed.
        seen (UserNotificationUpdateRequestSeen | None)
                                 : Whether the notification should be marked as seen by the
                                   user. If not set, the notification will not be changed.
    """

    deleted: UserNotificationUpdateRequestDeleted | None = (
        None  # Whether the notification should be marked as deleted by the user. If not set, the notification will not be changed.
    )
    seen: UserNotificationUpdateRequestSeen | None = (
        None  # Whether the notification should be marked as seen by the user. If not set, the notification will not be changed.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "deleted": "deleted",
            "seen": "seen",
        }
        key_transform_with_dump = {
            "deleted": "deleted",
            "seen": "seen",
        }
