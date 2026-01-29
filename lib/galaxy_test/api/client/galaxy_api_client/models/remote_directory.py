from dataclasses import dataclass

from .list_uri_response_item_class_enum import ListUriResponseItemClassEnum

__all__ = ["RemoteDirectory"]


@dataclass
class RemoteDirectory:
    """
    RemoteDirectory dataclass

    Args:
        class_ (ListUriResponseItemClassEnum)
                                 : Maps from 'class'
        name (str)               : The name of the entry.
        path (str)               : The path of the entry.
        uri (str)                : The URI of the entry.
    """

    class_: ListUriResponseItemClassEnum  # Maps from 'class'
    name: str  # The name of the entry.
    path: str  # The path of the entry.
    uri: str  # The URI of the entry.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "class": "class_",
            "name": "name",
            "path": "path",
            "uri": "uri",
        }
        key_transform_with_dump = {
            "class_": "class",
            "name": "name",
            "path": "path",
            "uri": "uri",
        }
