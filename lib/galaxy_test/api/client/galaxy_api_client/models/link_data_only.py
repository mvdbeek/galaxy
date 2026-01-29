from enum import Enum, unique

__all__ = ["LinkDataOnly"]


@unique
class LinkDataOnly(str, Enum):
    """
    LinkDataOnly Enum

    Args:
        copy_files (str)         : Value for COPY_FILES
        link_to_files (str)      : Value for LINK_TO_FILES
    """

    COPY_FILES = "copy_files"
    LINK_TO_FILES = "link_to_files"
