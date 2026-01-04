from enum import Enum, unique

__all__ = ["Requirement"]


@unique
class Requirement(str, Enum):
    """
    Available types of job sources (model classes) that produce dataset collections.

    Args:
        logged_in (str)          : Value for LOGGED_IN
        new_history (str)        : Value for NEW_HISTORY
        admin (str)              : Value for ADMIN
    """

    LOGGED_IN = "logged_in"
    NEW_HISTORY = "new_history"
    ADMIN = "admin"
