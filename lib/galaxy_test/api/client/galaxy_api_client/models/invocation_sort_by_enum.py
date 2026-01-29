from enum import Enum, unique

__all__ = ["InvocationSortByEnum"]


@unique
class InvocationSortByEnum(str, Enum):
    """
    InvocationSortByEnum Enum

    Args:
        create_time (str)        : Value for CREATE_TIME
        update_time (str)        : Value for UPDATE_TIME
        None (str)               : Value for NONE
    """

    CREATE_TIME = "create_time"
    UPDATE_TIME = "update_time"
    NONE = "None"
