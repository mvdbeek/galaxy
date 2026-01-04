from enum import Enum


class RemoteFilesDisableMode(str, Enum):
    FILES = "files"
    FOLDERS = "folders"

    def __str__(self) -> str:
        return str(self.value)
