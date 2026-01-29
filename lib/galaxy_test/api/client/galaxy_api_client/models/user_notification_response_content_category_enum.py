from enum import Enum, unique

__all__ = ["UserNotificationResponseContentCategoryEnum"]


@unique
class UserNotificationResponseContentCategoryEnum(str, Enum):
    """
    Discriminator enum for UserNotificationResponseContent union types.

    Args:
        message (str)            : Value for MESSAGE
        new_shared_item (str)    : Value for NEW_SHARED_ITEM
    """

    MESSAGE = "message"
    NEW_SHARED_ITEM = "new_shared_item"
