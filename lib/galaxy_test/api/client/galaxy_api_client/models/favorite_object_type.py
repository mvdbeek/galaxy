from enum import Enum, unique

__all__ = ["FavoriteObjectType"]


@unique
class FavoriteObjectType(str, Enum):
    """
    FavoriteObjectType Enum

    Args:
        tools (str)              : Value for TOOLS
    """

    TOOLS = "tools"
