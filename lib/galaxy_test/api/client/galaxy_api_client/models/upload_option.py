from enum import Enum, unique

__all__ = ["UploadOption"]


@unique
class UploadOption(str, Enum):
    """
    UploadOption Enum

    Args:
        upload_file (str)        : Value for UPLOAD_FILE
        upload_paths (str)       : Value for UPLOAD_PATHS
        upload_directory (str)   : Value for UPLOAD_DIRECTORY
    """

    UPLOAD_FILE = "upload_file"
    UPLOAD_PATHS = "upload_paths"
    UPLOAD_DIRECTORY = "upload_directory"
