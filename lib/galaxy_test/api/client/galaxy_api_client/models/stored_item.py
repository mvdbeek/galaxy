from dataclasses import dataclass
from datetime import datetime

from .type__11 import Type11

__all__ = ["StoredItem"]


@dataclass
class StoredItem:
    """
    StoredItem dataclass

    Args:
        id_ (str)                : Maps from 'id'
        name (str)               :
        size (int)               :
        type_ (Type11)           : Maps from 'type'
        update_time (datetime)   : The last time and date this item was updated.
    """

    id_: str  # Maps from 'id'
    name: str
    size: int
    type_: Type11  # Maps from 'type'
    update_time: datetime  # The last time and date this item was updated.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "name": "name",
            "size": "size",
            "type": "type_",
            "update_time": "update_time",
        }
        key_transform_with_dump = {
            "id_": "id",
            "name": "name",
            "size": "size",
            "type_": "type",
            "update_time": "update_time",
        }
