from enum import Enum, unique

__all__ = ["CreateType"]


@unique
class CreateType(str, Enum):
    """
    CreateType Enum

    Args:
        file (str)               : Value for FILE
        folder (str)             : Value for FOLDER
        collection (str)         : Value for COLLECTION
    """

    FILE = "file"
    FOLDER = "folder"
    COLLECTION = "collection"
