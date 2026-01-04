from enum import Enum


class LibraryFolderPermissionAction(str, Enum):
    SET_PERMISSIONS = "set_permissions"

    def __str__(self) -> str:
        return str(self.value)
