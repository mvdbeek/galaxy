from enum import Enum, unique

__all__ = ["ParsedWorkbookElementElementType"]


@unique
class ParsedWorkbookElementElementType(str, Enum):
    """
    ParsedWorkbookElementElementType Enum

    Args:
        hda (str)                : Value for HDA
        child_collection (str)   : Value for CHILD_COLLECTION
    """

    HDA = "hda"
    CHILD_COLLECTION = "child_collection"
