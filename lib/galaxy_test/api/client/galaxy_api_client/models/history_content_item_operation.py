from enum import Enum, unique

__all__ = ["HistoryContentItemOperation"]


@unique
class HistoryContentItemOperation(str, Enum):
    """
    HistoryContentItemOperation Enum

    Args:
        hide (str)               : Value for HIDE
        unhide (str)             : Value for UNHIDE
        delete (str)             : Value for DELETE
        undelete (str)           : Value for UNDELETE
        purge (str)              : Value for PURGE
        change_datatype (str)    : Value for CHANGE_DATATYPE
        change_dbkey (str)       : Value for CHANGE_DBKEY
        add_tags (str)           : Value for ADD_TAGS
        remove_tags (str)        : Value for REMOVE_TAGS
    """

    HIDE = "hide"
    UNHIDE = "unhide"
    DELETE = "delete"
    UNDELETE = "undelete"
    PURGE = "purge"
    CHANGE_DATATYPE = "change_datatype"
    CHANGE_DBKEY = "change_dbkey"
    ADD_TAGS = "add_tags"
    REMOVE_TAGS = "remove_tags"
