from enum import Enum


class RemoteFilesFormat(str, Enum):
    FLAT = "flat"
    JSTREE = "jstree"
    URI = "uri"

    def __str__(self) -> str:
        return str(self.value)
