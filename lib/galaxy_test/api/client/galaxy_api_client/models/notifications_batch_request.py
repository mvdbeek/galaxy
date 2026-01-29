from dataclasses import dataclass

__all__ = ["NotificationsBatchRequest"]


@dataclass
class NotificationsBatchRequest:
    """
    NotificationsBatchRequest dataclass

    Args:
        notification_ids (List[str])
                                 : The list of encoded notification IDs of the notifications
                                   that should be updated.
    """

    notification_ids: list[str]  # The list of encoded notification IDs of the notifications that should be updated.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "notification_ids": "notification_ids",
        }
        key_transform_with_dump = {
            "notification_ids": "notification_ids",
        }
