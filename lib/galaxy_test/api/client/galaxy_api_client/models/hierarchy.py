from enum import Enum, unique

__all__ = ["Hierarchy"]


@unique
class Hierarchy(str, Enum):
    """
    Hierarchy Enum

    Args:
        recurse (str)            : Value for RECURSE
        exact (str)              : Value for EXACT
    """

    RECURSE = "recurse"
    EXACT = "exact"
