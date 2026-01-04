from enum import Enum


class DataLibrariesFoldersContentsIndexSortBy(str, Enum):
    DESCRIPTION = "description"
    NAME = "name"
    SIZE = "size"
    TYPE = "type"
    UPDATE_TIME = "update_time"

    def __str__(self) -> str:
        return str(self.value)
