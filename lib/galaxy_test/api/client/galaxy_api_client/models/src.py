from enum import Enum, unique

__all__ = ["Src"]


@unique
class Src(str, Enum):
    """
    Src Enum

    Args:
        url (str)                : Value for URL
        pasted (str)             : Value for PASTED
        files (str)              : Value for FILES
        path (str)               : Value for PATH
        composite (str)          : Value for COMPOSITE
        ftp_import (str)         : Value for FTP_IMPORT
        server_dir (str)         : Value for SERVER_DIR
    """

    URL = "url"
    PASTED = "pasted"
    FILES = "files"
    PATH = "path"
    COMPOSITE = "composite"
    FTP_IMPORT = "ftp_import"
    SERVER_DIR = "server_dir"
