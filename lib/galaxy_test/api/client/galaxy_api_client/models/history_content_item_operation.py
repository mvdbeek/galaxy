from enum import Enum


class HistoryContentItemOperation(str, Enum):
    ADD_TAGS = "add_tags"
    CHANGE_DATATYPE = "change_datatype"
    CHANGE_DBKEY = "change_dbkey"
    DELETE = "delete"
    HIDE = "hide"
    PURGE = "purge"
    REMOVE_TAGS = "remove_tags"
    UNDELETE = "undelete"
    UNHIDE = "unhide"

    def __str__(self) -> str:
        return str(self.value)
