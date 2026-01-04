from dataclasses import dataclass
from datetime import datetime

from .copied_from_ldda_id import CopiedFromLddaId
from .dataset_state import DatasetState
from .extension import Extension
from .genome_build import GenomeBuild
from .name import Name
from .object_store_id import ObjectStoreId
from .tags import Tags
from .type_id import TypeId
from .update_time import UpdateTime

__all__ = ["HdaSummary"]


@dataclass
class HdaSummary:
    """
    History Dataset Association summary information.

    Args:
        create_time (datetime)   : The time and date this item was created.
        dataset_id (str)         : The encoded ID of the dataset associated with this item.
        deleted (bool)           : Whether this item is marked as deleted.
        extension (Optional[Extension])
                                 : The extension of the dataset.
        hid (int)                : The index position of this item in the History.
        history_content_type (str): This is always `dataset` for datasets.
        history_id (str)         :
        id_ (str)                :
        name (Optional[Name])    : The name of the creator.
        purged (bool)            : Whether this dataset has been removed from disk.
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
        genome_build (Optional[GenomeBuild])
                                 : TODO
        object_store_id (Optional[ObjectStoreId])
                                 : The ID of the object store that this dataset is stored
                                   in.
        type_id (Optional[TypeId]): The type and the encoded ID of this item. Used for
                                    caching.
    """

    create_time: datetime  # The time and date this item was created.
    dataset_id: str  # The encoded ID of the dataset associated with this item.
    deleted: bool  # Whether this item is marked as deleted.
    extension: Extension | None  # The extension of the dataset.
    hid: int  # The index position of this item in the History.
    history_content_type: str  # This is always `dataset` for datasets.
    history_id: str
    id_: str
    name: Name | None  # The name of the creator.
    purged: bool  # Whether this dataset has been removed from disk.
    state: DatasetState
    tags: Tags  # The collection of tags associated with an item.
    type_: str  # The type of this item.
    update_time: UpdateTime | None  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    visible: bool  # Whether this item is visible or hidden to the user by default.
    copied_from_ldda_id: CopiedFromLddaId | None = None
    genome_build: GenomeBuild | None = "?"  # TODO
    object_store_id: ObjectStoreId | None = None  # The ID of the object store that this dataset is stored in.
    type_id: TypeId | None = None  # The type and the encoded ID of this item. Used for caching.
