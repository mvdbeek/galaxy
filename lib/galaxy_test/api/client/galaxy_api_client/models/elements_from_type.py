from enum import Enum, unique

__all__ = ["ElementsFromType"]


@unique
class ElementsFromType(str, Enum):
    """
    ElementsFromType Enum

    Args:
        archive (str)            : Value for ARCHIVE
        bagit (str)              : Value for BAGIT
        bagit_archive (str)      : Value for BAGIT_ARCHIVE
        directory (str)          : Value for DIRECTORY
    """

    ARCHIVE = "archive"
    BAGIT = "bagit"
    BAGIT_ARCHIVE = "bagit_archive"
    DIRECTORY = "directory"
