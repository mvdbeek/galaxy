from enum import Enum


class DatasetCollectionsContentsContentsInstanceType(str, Enum):
    HISTORY = "history"
    LIBRARY = "library"

    def __str__(self) -> str:
        return str(self.value)
