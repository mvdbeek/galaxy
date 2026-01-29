from enum import Enum, unique

__all__ = ["PersonalNotificationCategory"]


@unique
class PersonalNotificationCategory(str, Enum):
    """
    These notification categories can be opt-out by the user and will be displayed in the
    notification preferences.

    Args:
        message (str)            : Value for MESSAGE
        new_shared_item (str)    : Value for NEW_SHARED_ITEM
    """

    MESSAGE = "message"
    NEW_SHARED_ITEM = "new_shared_item"
