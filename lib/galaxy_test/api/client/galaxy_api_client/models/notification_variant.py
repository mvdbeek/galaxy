from enum import Enum, unique

__all__ = ["NotificationVariant"]


@unique
class NotificationVariant(str, Enum):
    """
    The notification variant communicates the intent or relevance of the notification.

    Args:
        info (str)               : Value for INFO
        warning (str)            : Value for WARNING
        urgent (str)             : Value for URGENT
    """

    INFO = "info"
    WARNING = "warning"
    URGENT = "urgent"
