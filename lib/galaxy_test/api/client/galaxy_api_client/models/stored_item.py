from dataclasses import dataclass
from datetime import datetime

from .type_ import Type_

__all__ = ["StoredItem"]


@dataclass
class StoredItem:
    """
    StoredItem dataclass.

    Args:
        id_ (str)                :
        name (str)               :
        size (int)               :
        type_ (Type_)            : The type of content to be created in the history.
        update_time (datetime)   : The last time and date this item was updated.
    """

    id_: str
    name: str
    size: int
    type_: Type_  # The type of content to be created in the history.
    update_time: datetime  # The last time and date this item was updated.
