from enum import Enum, unique

__all__ = ["ExtraFilesEntryClass"]


@unique
class ExtraFilesEntryClass(str, Enum):
    """
    ExtraFilesEntryClass Enum

    Args:
        Directory (str)          : Value for DIRECTORY
        File (str)               : Value for FILE
    """

    DIRECTORY = "Directory"
    FILE = "File"
