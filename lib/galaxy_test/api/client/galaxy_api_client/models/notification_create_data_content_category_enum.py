from enum import Enum, unique

__all__ = ["NotificationCreateDataContentCategoryEnum"]


@unique
class NotificationCreateDataContentCategoryEnum(str, Enum):
    """
    Discriminator enum for NotificationCreateDataContent union types.

    Args:
        message (str)            : Value for MESSAGE
        new_shared_item (str)    : Value for NEW_SHARED_ITEM
        broadcast (str)          : Value for BROADCAST
    """

    MESSAGE = "message"
    NEW_SHARED_ITEM = "new_shared_item"
    BROADCAST = "broadcast"
