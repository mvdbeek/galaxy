from dataclasses import dataclass
from datetime import datetime

from .dataset_state import DatasetState
from .hda_summary_copied_from_ldda_id import HdaSummaryCopiedFromLddaId
from .hda_summary_extension import HdaSummaryExtension
from .hda_summary_genome_build import HdaSummaryGenomeBuild
from .hda_summary_name import HdaSummaryName
from .hda_summary_object_store_id import HdaSummaryObjectStoreId
from .hda_summary_type_id import HdaSummaryTypeId
from .hda_summary_update_time import HdaSummaryUpdateTime

__all__ = ["HdaSummary2"]


@dataclass
class HdaSummary2:
    """
    History Dataset Association summary information.

    Args:
        create_time (datetime)   : The time and date this item was created.
        dataset_id (str)         : The encoded ID of the dataset associated with this item.
        deleted (bool)           : Whether this item is marked as deleted.
        extension (HdaSummaryExtension)
                                 : The extension of the dataset.
        hid (int)                : The index position of this item in the History.
        history_content_type (str): This is always `dataset` for datasets.
        history_id (str)         :
        id_ (str)                : Maps from 'id'
        name (HdaSummaryName)    : The name of the item.
        purged (bool)            : Whether this dataset has been removed from disk.
        state (DatasetState)     :
        tags (List[str])         : The collection of tags associated with an item.
        type_ (str)              : The type of this item. (maps from 'type')
        update_time (HdaSummaryUpdateTime)
                                 : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        visible (bool)           : Whether this item is visible or hidden to the user by
                                   default.
        copied_from_ldda_id (HdaSummaryCopiedFromLddaId | None)
                                 :
        genome_build (HdaSummaryGenomeBuild | None)
                                 : TODO
        object_store_id (HdaSummaryObjectStoreId | None)
                                 : The ID of the object store that this dataset is stored
                                   in.
        type_id (HdaSummaryTypeId | None)
                                 : The type and the encoded ID of this item. Used for
                                   caching.
    """

    create_time: datetime  # The time and date this item was created.
    dataset_id: str  # The encoded ID of the dataset associated with this item.
    deleted: bool  # Whether this item is marked as deleted.
    extension: HdaSummaryExtension  # The extension of the dataset.
    hid: int  # The index position of this item in the History.
    history_content_type: str  # This is always `dataset` for datasets.
    history_id: str
    id_: str  # Maps from 'id'
    name: HdaSummaryName  # The name of the item.
    purged: bool  # Whether this dataset has been removed from disk.
    state: DatasetState
    tags: list[str]  # The collection of tags associated with an item.
    type_: str  # The type of this item. (maps from 'type')
    update_time: HdaSummaryUpdateTime  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    visible: bool  # Whether this item is visible or hidden to the user by default.
    copied_from_ldda_id: HdaSummaryCopiedFromLddaId | None = None
    genome_build: HdaSummaryGenomeBuild | None = "?"  # TODO
    object_store_id: HdaSummaryObjectStoreId | None = None  # The ID of the object store that this dataset is stored in.
    type_id: HdaSummaryTypeId | None = None  # The type and the encoded ID of this item. Used for caching.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "copied_from_ldda_id": "copied_from_ldda_id",
            "create_time": "create_time",
            "dataset_id": "dataset_id",
            "deleted": "deleted",
            "extension": "extension",
            "genome_build": "genome_build",
            "hid": "hid",
            "history_content_type": "history_content_type",
            "history_id": "history_id",
            "id": "id_",
            "name": "name",
            "object_store_id": "object_store_id",
            "purged": "purged",
            "state": "state",
            "tags": "tags",
            "type": "type_",
            "type_id": "type_id",
            "update_time": "update_time",
            "url": "url",
            "visible": "visible",
        }
        key_transform_with_dump = {
            "copied_from_ldda_id": "copied_from_ldda_id",
            "create_time": "create_time",
            "dataset_id": "dataset_id",
            "deleted": "deleted",
            "extension": "extension",
            "genome_build": "genome_build",
            "hid": "hid",
            "history_content_type": "history_content_type",
            "history_id": "history_id",
            "id_": "id",
            "name": "name",
            "object_store_id": "object_store_id",
            "purged": "purged",
            "state": "state",
            "tags": "tags",
            "type_": "type",
            "type_id": "type_id",
            "update_time": "update_time",
            "url": "url",
            "visible": "visible",
        }
