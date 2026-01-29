from enum import Enum, unique

__all__ = ["ItemsFromSrc"]


@unique
class ItemsFromSrc(str, Enum):
    """
    ItemsFromSrc Enum

    Args:
        url (str)                : Value for URL
        files (str)              : Value for FILES
        path (str)               : Value for PATH
        ftp_import (str)         : Value for FTP_IMPORT
        server_dir (str)         : Value for SERVER_DIR
    """

    URL = "url"
    FILES = "files"
    PATH = "path"
    FTP_IMPORT = "ftp_import"
    SERVER_DIR = "server_dir"
