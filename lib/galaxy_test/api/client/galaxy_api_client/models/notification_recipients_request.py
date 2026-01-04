from dataclasses import dataclass

from .group_ids import GroupIds
from .role_ids import RoleIds
from .user_ids import UserIds

__all__ = ["NotificationRecipientsRequest"]


@dataclass
class NotificationRecipientsRequest:
    """
    NotificationRecipientsRequest dataclass.

    Args:
        group_ids (Optional[GroupIds])
                                 : The list of encoded group IDs of the groups that should
                                   receive the notification.
        role_ids (Optional[RoleIds])
                                 : The list of encoded role IDs of the roles that should
                                   receive the notification.
        user_ids (Optional[UserIds])
                                 : The list of encoded user IDs of the users that should
                                   receive the notification.
    """

    group_ids: GroupIds | None = (
        None  # The list of encoded group IDs of the groups that should receive the notification.
    )
    role_ids: RoleIds | None = None  # The list of encoded role IDs of the roles that should receive the notification.
    user_ids: UserIds | None = None  # The list of encoded user IDs of the users that should receive the notification.
