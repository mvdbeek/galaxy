from dataclasses import dataclass, field

__all__ = ["NotificationRecipientsRequest"]


@dataclass
class NotificationRecipientsRequest:
    """
    NotificationRecipientsRequest dataclass

    Args:
        group_ids (List[str] | None)
                                 : The list of encoded group IDs of the groups that should
                                   receive the notification.
        role_ids (List[str] | None)
                                 : The list of encoded role IDs of the roles that should
                                   receive the notification.
        user_ids (List[str] | None)
                                 : The list of encoded user IDs of the users that should
                                   receive the notification.
    """

    group_ids: list[str] | None = field(
        default_factory=list
    )  # The list of encoded group IDs of the groups that should receive the notification.
    role_ids: list[str] | None = field(
        default_factory=list
    )  # The list of encoded role IDs of the roles that should receive the notification.
    user_ids: list[str] | None = field(
        default_factory=list
    )  # The list of encoded user IDs of the users that should receive the notification.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "group_ids": "group_ids",
            "role_ids": "role_ids",
            "user_ids": "user_ids",
        }
        key_transform_with_dump = {
            "group_ids": "group_ids",
            "role_ids": "role_ids",
            "user_ids": "user_ids",
        }
