from enum import Enum, unique

__all__ = ["StoredItemOrderBy"]


@unique
class StoredItemOrderBy(str, Enum):
    """
    Available options for sorting Stored Items results.

    Args:
        name-asc (str)           : Value for NAME_ASC
        name-dsc (str)           : Value for NAME_DSC
        size-asc (str)           : Value for SIZE_ASC
        size-dsc (str)           : Value for SIZE_DSC
        update_time-asc (str)    : Value for UPDATE_TIME_ASC
        update_time-dsc (str)    : Value for UPDATE_TIME_DSC
    """

    NAME_ASC = "name-asc"
    NAME_DSC = "name-dsc"
    SIZE_ASC = "size-asc"
    SIZE_DSC = "size-dsc"
    UPDATE_TIME_ASC = "update_time-asc"
    UPDATE_TIME_DSC = "update_time-dsc"
