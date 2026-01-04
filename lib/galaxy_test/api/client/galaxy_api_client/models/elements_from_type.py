from enum import Enum


class ElementsFromType(str, Enum):
    ARCHIVE = "archive"
    BAGIT = "bagit"
    BAGIT_ARCHIVE = "bagit_archive"
    DIRECTORY = "directory"

    def __str__(self) -> str:
        return str(self.value)
