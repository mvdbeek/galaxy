from enum import Enum, unique

__all__ = ["DrillDownParameterModelOutputHierarchy"]


@unique
class DrillDownParameterModelOutputHierarchy(str, Enum):
    """
    DrillDownParameterModelOutputHierarchy Enum

    Args:
        recurse (str)            : Value for RECURSE
        exact (str)              : Value for EXACT
    """

    RECURSE = "recurse"
    EXACT = "exact"
