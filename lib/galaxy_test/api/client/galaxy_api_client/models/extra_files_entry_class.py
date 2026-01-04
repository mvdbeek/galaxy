from enum import Enum


class ExtraFilesEntryClass(str, Enum):
    DIRECTORY = "Directory"
    FILE = "File"

    def __str__(self) -> str:
        return str(self.value)
