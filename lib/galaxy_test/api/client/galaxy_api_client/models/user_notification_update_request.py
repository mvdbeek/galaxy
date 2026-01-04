from dataclasses import dataclass

from .deleted import Deleted
from .seen import Seen

__all__ = ["UserNotificationUpdateRequest"]


@dataclass
class UserNotificationUpdateRequest:
    """
    A notification update request specific to the user.

    Args:
        deleted (Optional[Deleted])
                                 : Whether this Visualization has been deleted.
        seen (Optional[Seen])    : Whether the notification should be marked as seen by the
                                   user. If not set, the notification will not be changed.
    """

    deleted: Deleted | None = False  # Whether this Visualization has been deleted.
    seen: Seen | None = (
        None  # Whether the notification should be marked as seen by the user. If not set, the notification will not be changed.
    )
