from enum import Enum, unique

__all__ = ["LibraryPermissionAction"]


@unique
class LibraryPermissionAction(str, Enum):
    """
    LibraryPermissionAction Enum

    Args:
        set_permissions (str)    : Value for SET_PERMISSIONS
        remove_restrictions (str): Value for REMOVE_RESTRICTIONS
    """

    SET_PERMISSIONS = "set_permissions"
    REMOVE_RESTRICTIONS = "remove_restrictions"
