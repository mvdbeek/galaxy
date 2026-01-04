from enum import Enum


class LibraryPermissionAction(str, Enum):
    REMOVE_RESTRICTIONS = "remove_restrictions"
    SET_PERMISSIONS = "set_permissions"

    def __str__(self) -> str:
        return str(self.value)
