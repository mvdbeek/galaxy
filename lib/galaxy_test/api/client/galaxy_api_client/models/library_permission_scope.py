from enum import Enum


class LibraryPermissionScope(str, Enum):
    AVAILABLE = "available"
    CURRENT = "current"

    def __str__(self) -> str:
        return str(self.value)
