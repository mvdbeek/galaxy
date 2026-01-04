from dataclasses import dataclass
from datetime import datetime

from .copied_from_ldda_id import CopiedFromLddaId
from .dataset_state import DatasetState
from .name import Name
from .tags import Tags
from .type_id import TypeId
from .update_time import UpdateTime

__all__ = ["HdaInaccessible"]


@dataclass
class HdaInaccessible:
    """
    History Dataset Association information when the user can not access it.

    Args:
        accessible (bool)        :
        create_time (datetime)   : The time and date this item was created.
        deleted (bool)           : Whether this item is marked as deleted.
        hid (int)                : The index position of this item in the History.
        history_content_type (str): This is always `dataset` for datasets.
        history_id (str)         :
        id_ (str)                :
        name (Optional[Name])    : The name of the creator.
        state (DatasetState)     :
        tags (Tags)              : The collection of tags associated with an item.
        type_ (str)              : The type of this item.
        update_time (Optional[UpdateTime])
                                 : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        visible (bool)           : Whether this item is visible or hidden to the user by
                                   default.
        copied_from_ldda_id (Optional[CopiedFromLddaId])
                                 :
        type_id (Optional[TypeId]): The type and the encoded ID of this item. Used for
                                    caching.
    """

    accessible: bool
    create_time: datetime  # The time and date this item was created.
    deleted: bool  # Whether this item is marked as deleted.
    hid: int  # The index position of this item in the History.
    history_content_type: str  # This is always `dataset` for datasets.
    history_id: str
    id_: str
    name: Name | None  # The name of the creator.
    state: DatasetState
    tags: Tags  # The collection of tags associated with an item.
    type_: str  # The type of this item.
    update_time: UpdateTime | None  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    visible: bool  # Whether this item is visible or hidden to the user by default.
    copied_from_ldda_id: CopiedFromLddaId | None = None
    type_id: TypeId | None = None  # The type and the encoded ID of this item. Used for caching.
