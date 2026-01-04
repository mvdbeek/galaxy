from enum import Enum


class CreateType(str, Enum):
    COLLECTION = "collection"
    FILE = "file"
    FOLDER = "folder"

    def __str__(self) -> str:
        return str(self.value)
