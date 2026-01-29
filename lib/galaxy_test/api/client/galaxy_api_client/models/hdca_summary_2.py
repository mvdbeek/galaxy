from dataclasses import dataclass
from datetime import datetime

from .dataset_collection_populated_state import DatasetCollectionPopulatedState
from .elements_states_dict import ElementsStatesDict
from .hdca_summary_element_count import HdcaSummaryElementCount
from .hdca_summary_job_source_id import HdcaSummaryJobSourceId
from .hdca_summary_job_source_type import HdcaSummaryJobSourceType
from .hdca_summary_job_state_summary import HdcaSummaryJobStateSummary
from .hdca_summary_name import HdcaSummaryName
from .hdca_summary_populated_state_message import HdcaSummaryPopulatedStateMessage
from .hdca_summary_store_times_summary import HdcaSummaryStoreTimesSummary
from .hdca_summary_type_id import HdcaSummaryTypeId
from .hdca_summary_update_time import HdcaSummaryUpdateTime

__all__ = ["HdcaSummary2"]


@dataclass
class HdcaSummary2:
    """
    History Dataset Collection Association summary information.

    Args:
        collection_id (str)      :
        collection_type (str)    : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        contents_url (str)       : The relative URL to access the contents of this History.
        create_time (datetime)   : The time and date this item was created.
        deleted (bool)           : Whether this item is marked as deleted.
        elements_datatypes (List[str])
                                 : A set containing all the different element datatypes in
                                   the collection.
        elements_deleted (int)   : The number of elements in the collection that are marked
                                   as deleted.
        elements_states (ElementsStatesDict)
                                 :
        hid (int)                : The index position of this item in the History.
        history_content_type (str): This is always `dataset_collection` for dataset
                                    collections.
        history_id (str)         :
        id_ (str)                : Maps from 'id'
        model_class (str)        : The name of the database model class.
        name (HdcaSummaryName)   : The name of the item.
        populated_state (DatasetCollectionPopulatedState)
                                 :
        tags (List[str])         : The collection of tags associated with an item.
        update_time (HdcaSummaryUpdateTime)
                                 : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        visible (bool)           : Whether this item is visible or hidden to the user by
                                   default.
        element_count (HdcaSummaryElementCount | None)
                                 : The number of elements contained in the dataset
                                   collection. It may be None or undefined if the collection
                                   could not be populated.
        job_source_id (HdcaSummaryJobSourceId | None)
                                 : The encoded ID of the Job that produced this dataset
                                   collection. Used to track the state of the job.
        job_source_type (HdcaSummaryJobSourceType | None)
                                 : The type of job (model class) that produced this dataset
                                   collection. Used to track the state of the job.
        job_state_summary (HdcaSummaryJobStateSummary | None)
                                 : Overview of the job states working inside the dataset
                                   collection.
        populated_state_message (HdcaSummaryPopulatedStateMessage | None)
                                 : Optional message with further information in case the
                                   population of the dataset collection failed.
        store_times_summary (HdcaSummaryStoreTimesSummary | None)
                                 : A list of objects containing the object store ID and the
                                   oldest creation time of the datasets stored in that
                                   object store for this collection.This is used to
                                   determine the age of the datasets in the collection when
                                   the object store is short-lived.
        type_ (str | None)       : This is always `collection` for dataset collections.
                                   (maps from 'type')
        type_id (HdcaSummaryTypeId | None)
                                 : The type and the encoded ID of this item. Used for
                                   caching.
    """

    collection_id: str
    collection_type: str  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    contents_url: str  # The relative URL to access the contents of this History.
    create_time: datetime  # The time and date this item was created.
    deleted: bool  # Whether this item is marked as deleted.
    elements_datatypes: list[str]  # A set containing all the different element datatypes in the collection.
    elements_deleted: int  # The number of elements in the collection that are marked as deleted.
    elements_states: ElementsStatesDict
    hid: int  # The index position of this item in the History.
    history_content_type: str  # This is always `dataset_collection` for dataset collections.
    history_id: str
    id_: str  # Maps from 'id'
    model_class: str  # The name of the database model class.
    name: HdcaSummaryName  # The name of the item.
    populated_state: DatasetCollectionPopulatedState
    tags: list[str]  # The collection of tags associated with an item.
    update_time: HdcaSummaryUpdateTime  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    visible: bool  # Whether this item is visible or hidden to the user by default.
    element_count: HdcaSummaryElementCount | None = (
        None  # The number of elements contained in the dataset collection. It may be None or undefined if the collection could not be populated.
    )
    job_source_id: HdcaSummaryJobSourceId | None = (
        None  # The encoded ID of the Job that produced this dataset collection. Used to track the state of the job.
    )
    job_source_type: HdcaSummaryJobSourceType | None = (
        None  # The type of job (model class) that produced this dataset collection. Used to track the state of the job.
    )
    job_state_summary: HdcaSummaryJobStateSummary | None = (
        None  # Overview of the job states working inside the dataset collection.
    )
    populated_state_message: HdcaSummaryPopulatedStateMessage | None = (
        None  # Optional message with further information in case the population of the dataset collection failed.
    )
    store_times_summary: HdcaSummaryStoreTimesSummary | None = (
        None  # A list of objects containing the object store ID and the oldest creation time of the datasets stored in that object store for this collection.This is used to determine the age of the datasets in the collection when the object store is short-lived.
    )
    type_: str | None = "collection"  # This is always `collection` for dataset collections. (maps from 'type')
    type_id: HdcaSummaryTypeId | None = None  # The type and the encoded ID of this item. Used for caching.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "collection_id": "collection_id",
            "collection_type": "collection_type",
            "contents_url": "contents_url",
            "create_time": "create_time",
            "deleted": "deleted",
            "element_count": "element_count",
            "elements_datatypes": "elements_datatypes",
            "elements_deleted": "elements_deleted",
            "elements_states": "elements_states",
            "hid": "hid",
            "history_content_type": "history_content_type",
            "history_id": "history_id",
            "id": "id_",
            "job_source_id": "job_source_id",
            "job_source_type": "job_source_type",
            "job_state_summary": "job_state_summary",
            "model_class": "model_class",
            "name": "name",
            "populated_state": "populated_state",
            "populated_state_message": "populated_state_message",
            "store_times_summary": "store_times_summary",
            "tags": "tags",
            "type": "type_",
            "type_id": "type_id",
            "update_time": "update_time",
            "url": "url",
            "visible": "visible",
        }
        key_transform_with_dump = {
            "collection_id": "collection_id",
            "collection_type": "collection_type",
            "contents_url": "contents_url",
            "create_time": "create_time",
            "deleted": "deleted",
            "element_count": "element_count",
            "elements_datatypes": "elements_datatypes",
            "elements_deleted": "elements_deleted",
            "elements_states": "elements_states",
            "hid": "hid",
            "history_content_type": "history_content_type",
            "history_id": "history_id",
            "id_": "id",
            "job_source_id": "job_source_id",
            "job_source_type": "job_source_type",
            "job_state_summary": "job_state_summary",
            "model_class": "model_class",
            "name": "name",
            "populated_state": "populated_state",
            "populated_state_message": "populated_state_message",
            "store_times_summary": "store_times_summary",
            "tags": "tags",
            "type_": "type",
            "type_id": "type_id",
            "update_time": "update_time",
            "url": "url",
            "visible": "visible",
        }
