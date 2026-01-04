from enum import Enum


class DatasetPermissionAction(str, Enum):
    MAKE_PRIVATE = "make_private"
    REMOVE_RESTRICTIONS = "remove_restrictions"
    SET_PERMISSIONS = "set_permissions"

    def __str__(self) -> str:
        return str(self.value)
