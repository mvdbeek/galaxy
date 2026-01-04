from enum import Enum, unique

__all__ = ["SortKey"]


@unique
class SortKey(str, Enum):
    """
    SortKey Enum

    Args:
        filename (str)           : Value for FILENAME
        name (str)               : Value for NAME
        designation (str)        : Value for DESIGNATION
        dbkey (str)              : Value for DBKEY
    """

    FILENAME = "filename"
    NAME = "name"
    DESIGNATION = "designation"
    DBKEY = "dbkey"
