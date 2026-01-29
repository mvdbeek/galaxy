from dataclasses import dataclass
from datetime import datetime

from .dataset_state import DatasetState
from .hda_inaccessible_copied_from_ldda_id import HdaInaccessibleCopiedFromLddaId
from .hda_inaccessible_name import HdaInaccessibleName
from .hda_inaccessible_type_id import HdaInaccessibleTypeId
from .hda_inaccessible_update_time import HdaInaccessibleUpdateTime

__all__ = ["HdaInaccessible2"]


@dataclass
class HdaInaccessible2:
    """
    History Dataset Association information when the user can not access it.

    Args:
        accessible (bool)        :
        create_time (datetime)   : The time and date this item was created.
        deleted (bool)           : Whether this item is marked as deleted.
        hid (int)                : The index position of this item in the History.
        history_content_type (str): This is always `dataset` for datasets.
        history_id (str)         :
        id_ (str)                : Maps from 'id'
        name (HdaInaccessibleName): The name of the item.
        state (DatasetState)     :
        tags (List[str])         : The collection of tags associated with an item.
        type_ (str)              : The type of this item. (maps from 'type')
        update_time (HdaInaccessibleUpdateTime)
                                 : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        visible (bool)           : Whether this item is visible or hidden to the user by
                                   default.
        copied_from_ldda_id (HdaInaccessibleCopiedFromLddaId | None)
                                 :
        type_id (HdaInaccessibleTypeId | None)
                                 : The type and the encoded ID of this item. Used for
                                   caching.
    """

    accessible: bool
    create_time: datetime  # The time and date this item was created.
    deleted: bool  # Whether this item is marked as deleted.
    hid: int  # The index position of this item in the History.
    history_content_type: str  # This is always `dataset` for datasets.
    history_id: str
    id_: str  # Maps from 'id'
    name: HdaInaccessibleName  # The name of the item.
    state: DatasetState
    tags: list[str]  # The collection of tags associated with an item.
    type_: str  # The type of this item. (maps from 'type')
    update_time: HdaInaccessibleUpdateTime  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    visible: bool  # Whether this item is visible or hidden to the user by default.
    copied_from_ldda_id: HdaInaccessibleCopiedFromLddaId | None = None
    type_id: HdaInaccessibleTypeId | None = None  # The type and the encoded ID of this item. Used for caching.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "accessible": "accessible",
            "copied_from_ldda_id": "copied_from_ldda_id",
            "create_time": "create_time",
            "deleted": "deleted",
            "hid": "hid",
            "history_content_type": "history_content_type",
            "history_id": "history_id",
            "id": "id_",
            "name": "name",
            "state": "state",
            "tags": "tags",
            "type": "type_",
            "type_id": "type_id",
            "update_time": "update_time",
            "url": "url",
            "visible": "visible",
        }
        key_transform_with_dump = {
            "accessible": "accessible",
            "copied_from_ldda_id": "copied_from_ldda_id",
            "create_time": "create_time",
            "deleted": "deleted",
            "hid": "hid",
            "history_content_type": "history_content_type",
            "history_id": "history_id",
            "id_": "id",
            "name": "name",
            "state": "state",
            "tags": "tags",
            "type_": "type",
            "type_id": "type_id",
            "update_time": "update_time",
            "url": "url",
            "visible": "visible",
        }
