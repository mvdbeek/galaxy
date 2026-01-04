from enum import Enum, unique

__all__ = ["PrefixColumnsType"]


@unique
class PrefixColumnsType(str, Enum):
    """
    PrefixColumnsType Enum

    Args:
        URI (str)                : Value for URI
        ModelObjects (str)       : Value for MODELOBJECTS
    """

    URI = "URI"
    MODELOBJECTS = "ModelObjects"
