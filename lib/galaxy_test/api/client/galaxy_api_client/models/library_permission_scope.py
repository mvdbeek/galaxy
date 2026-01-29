from enum import Enum, unique

__all__ = ["LibraryPermissionScope"]


@unique
class LibraryPermissionScope(str, Enum):
    """
    LibraryPermissionScope Enum

    Args:
        current (str)            : Value for CURRENT
        available (str)          : Value for AVAILABLE
    """

    CURRENT = "current"
    AVAILABLE = "available"
