from enum import Enum, unique

__all__ = ["MandatoryNotificationCategory"]


@unique
class MandatoryNotificationCategory(str, Enum):
    """
    These notification categories cannot be opt-out by the user.  The user will always
    receive notifications from these categories.

    Args:
        broadcast (str)          : Value for BROADCAST
    """

    BROADCAST = "broadcast"
