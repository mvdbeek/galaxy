from enum import Enum, unique

__all__ = ["ParseWorkbookPrefixColumnsType"]


@unique
class ParseWorkbookPrefixColumnsType(str, Enum):
    """
    ParseWorkbookPrefixColumnsType Enum

    Args:
        URI (str)                : Value for URI
        ModelObjects (str)       : Value for MODELOBJECTS
    """

    URI = "URI"
    MODELOBJECTS = "ModelObjects"
