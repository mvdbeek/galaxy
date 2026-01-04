from enum import Enum


class FilePatternDatasetCollectionDescriptionSortKey(str, Enum):
    DBKEY = "dbkey"
    DESIGNATION = "designation"
    FILENAME = "filename"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
