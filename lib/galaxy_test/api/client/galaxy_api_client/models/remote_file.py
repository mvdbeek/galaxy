from dataclasses import dataclass

from .list_uri_response_item_class_enum import ListUriResponseItemClassEnum
from .remote_file_hashes import RemoteFileHashes

__all__ = ["RemoteFile"]


@dataclass
class RemoteFile:
    """
    RemoteFile dataclass

    Args:
        class_ (ListUriResponseItemClassEnum)
                                 : Maps from 'class'
        ctime (str)              : The creation time of the file.
        name (str)               : The name of the entry.
        path (str)               : The path of the entry.
        size (int)               : The size of the file in bytes.
        uri (str)                : The URI of the entry.
        hashes (RemoteFileHashes | None)
                                 : List of precomputed hashes for the file, if available.
    """

    class_: ListUriResponseItemClassEnum  # Maps from 'class'
    ctime: str  # The creation time of the file.
    name: str  # The name of the entry.
    path: str  # The path of the entry.
    size: int  # The size of the file in bytes.
    uri: str  # The URI of the entry.
    hashes: RemoteFileHashes | None = None  # List of precomputed hashes for the file, if available.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "class": "class_",
            "ctime": "ctime",
            "hashes": "hashes",
            "name": "name",
            "path": "path",
            "size": "size",
            "uri": "uri",
        }
        key_transform_with_dump = {
            "class_": "class",
            "ctime": "ctime",
            "hashes": "hashes",
            "name": "name",
            "path": "path",
            "size": "size",
            "uri": "uri",
        }
