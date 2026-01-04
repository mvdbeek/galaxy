from enum import Enum


class DatasetCollectionsAttributesAttributesInstanceType(str, Enum):
    HISTORY = "history"
    LIBRARY = "library"

    def __str__(self) -> str:
        return str(self.value)
