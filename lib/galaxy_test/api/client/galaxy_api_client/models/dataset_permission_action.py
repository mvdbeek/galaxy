from enum import Enum, unique

__all__ = ["DatasetPermissionAction"]


@unique
class DatasetPermissionAction(str, Enum):
    """
    DatasetPermissionAction Enum

    Args:
        set_permissions (str)    : Value for SET_PERMISSIONS
        make_private (str)       : Value for MAKE_PRIVATE
        remove_restrictions (str): Value for REMOVE_RESTRICTIONS
    """

    SET_PERMISSIONS = "set_permissions"
    MAKE_PRIVATE = "make_private"
    REMOVE_RESTRICTIONS = "remove_restrictions"
