from enum import Enum, unique

__all__ = ["RemoteFilesFormat"]


@unique
class RemoteFilesFormat(str, Enum):
    """
    RemoteFilesFormat Enum

    Args:
        flat (str)               : Value for FLAT
        jstree (str)             : Value for JSTREE
        uri (str)                : Value for URI
    """

    FLAT = "flat"
    JSTREE = "jstree"
    URI = "uri"
