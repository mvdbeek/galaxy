from enum import Enum, unique

__all__ = ["DrillDownParameterModelInputHierarchy"]


@unique
class DrillDownParameterModelInputHierarchy(str, Enum):
    """
    DrillDownParameterModelInputHierarchy Enum

    Args:
        recurse (str)            : Value for RECURSE
        exact (str)              : Value for EXACT
    """

    RECURSE = "recurse"
    EXACT = "exact"
