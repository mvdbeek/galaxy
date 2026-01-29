from enum import Enum, unique

__all__ = ["ListUriResponseItemClassEnum"]


@unique
class ListUriResponseItemClassEnum(str, Enum):
    """
    Discriminator enum for ListUriResponseItem union types.

    Args:
        File (str)               : Value for FILE
        Directory (str)          : Value for DIRECTORY
    """

    FILE = "File"
    DIRECTORY = "Directory"
