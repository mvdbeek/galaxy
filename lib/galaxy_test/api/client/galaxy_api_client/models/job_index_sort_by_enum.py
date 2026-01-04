from enum import Enum, unique

__all__ = ["JobIndexSortByEnum"]


@unique
class JobIndexSortByEnum(str, Enum):
    """
    JobIndexSortByEnum Enum

    Args:
        create_time (str)        : Value for CREATE_TIME
        update_time (str)        : Value for UPDATE_TIME
    """

    CREATE_TIME = "create_time"
    UPDATE_TIME = "update_time"
