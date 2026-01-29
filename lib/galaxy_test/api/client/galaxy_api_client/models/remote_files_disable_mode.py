from enum import Enum, unique

__all__ = ["RemoteFilesDisableMode"]


@unique
class RemoteFilesDisableMode(str, Enum):
    """
    RemoteFilesDisableMode Enum

    Args:
        folders (str)            : Value for FOLDERS
        files (str)              : Value for FILES
    """

    FOLDERS = "folders"
    FILES = "files"
