from dataclasses import dataclass

from .hashes import Hashes

__all__ = ["RemoteFile"]


@dataclass
class RemoteFile:
    """
    RemoteFile dataclass.

    Args:
        class_ (str)             :
        ctime (str)              : The creation time of the file.
        name (str)               : The name of the entry.
        path (str)               : The path of the entry.
        size (int)               : The size of the file in bytes.
        uri (str)                : The URI of the entry.
        hashes (Optional[Hashes]): List of precomputed hashes for the file, if available.
    """

    class_: str
    ctime: str  # The creation time of the file.
    name: str  # The name of the entry.
    path: str  # The path of the entry.
    size: int  # The size of the file in bytes.
    uri: str  # The URI of the entry.
    hashes: Hashes | None = None  # List of precomputed hashes for the file, if available.
