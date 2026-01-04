from enum import Enum, unique

__all__ = ["Source"]


@unique
class Source(str, Enum):
    """
    The source of the notification. Represents the agent that created the notification.

    Args:
        admin (str)              : Value for ADMIN
        galaxy (str)             : Value for GALAXY
    """

    ADMIN = "admin"
    GALAXY = "galaxy"
