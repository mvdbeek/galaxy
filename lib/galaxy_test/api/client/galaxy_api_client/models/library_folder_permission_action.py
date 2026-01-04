from enum import Enum, unique

__all__ = ["LibraryFolderPermissionAction"]


@unique
class LibraryFolderPermissionAction(str, Enum):
    """
    LibraryFolderPermissionAction Enum

    Args:
        set_permissions (str)    : Value for SET_PERMISSIONS
    """

    SET_PERMISSIONS = "set_permissions"
