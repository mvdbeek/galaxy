from dataclasses import dataclass, field
from datetime import datetime

from .dataset_collection_populated_state import DatasetCollectionPopulatedState
from .dce_summary_2 import DceSummary2
from .elements_states_dict import ElementsStatesDict
from .hdca_detailed_column_definitions import HdcaDetailedColumnDefinitions
from .hdca_detailed_element_count import HdcaDetailedElementCount
from .hdca_detailed_implicit_collection_jobs_id import HdcaDetailedImplicitCollectionJobsId
from .hdca_detailed_job_source_id import HdcaDetailedJobSourceId
from .hdca_detailed_job_source_type import HdcaDetailedJobSourceType
from .hdca_detailed_job_state_summary import HdcaDetailedJobStateSummary
from .hdca_detailed_name import HdcaDetailedName
from .hdca_detailed_populated_state_message import HdcaDetailedPopulatedStateMessage
from .hdca_detailed_store_times_summary import HdcaDetailedStoreTimesSummary
from .hdca_detailed_type_id import HdcaDetailedTypeId
from .hdca_detailed_update_time import HdcaDetailedUpdateTime

__all__ = ["HdcaDetailed2"]


@dataclass
class HdcaDetailed2:
    """
    History Dataset Collection Association detailed information.

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
        name (HdcaDetailedName)  : The name of the item.
        populated_state (DatasetCollectionPopulatedState)
                                 :
        tags (List[str])         : The collection of tags associated with an item.
        update_time (HdcaDetailedUpdateTime)
                                 : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        visible (bool)           : Whether this item is visible or hidden to the user by
                                   default.
        column_definitions (HdcaDetailedColumnDefinitions | None)
                                 : Column data associated with each element of this
                                   collection.
        element_count (HdcaDetailedElementCount | None)
                                 : The number of elements contained in the dataset
                                   collection. It may be None or undefined if the collection
                                   could not be populated.
        elements (List[DceSummary2] | None)
                                 : The summary information of each of the elements inside
                                   the dataset collection.
        implicit_collection_jobs_id (HdcaDetailedImplicitCollectionJobsId | None)
                                 : Encoded ID for the ICJ object describing the collection
                                   of jobs corresponding to this collection
        job_source_id (HdcaDetailedJobSourceId | None)
                                 : The encoded ID of the Job that produced this dataset
                                   collection. Used to track the state of the job.
        job_source_type (HdcaDetailedJobSourceType | None)
                                 : The type of job (model class) that produced this dataset
                                   collection. Used to track the state of the job.
        job_state_summary (HdcaDetailedJobStateSummary | None)
                                 : Overview of the job states working inside the dataset
                                   collection.
        populated (bool | None)  : Whether the dataset collection elements (and any
                                   subcollections elements) were successfully populated.
        populated_state_message (HdcaDetailedPopulatedStateMessage | None)
                                 : Optional message with further information in case the
                                   population of the dataset collection failed.
        store_times_summary (HdcaDetailedStoreTimesSummary | None)
                                 : A list of objects containing the object store ID and the
                                   oldest creation time of the datasets stored in that
                                   object store for this collection.This is used to
                                   determine the age of the datasets in the collection when
                                   the object store is short-lived.
        type_ (str | None)       : This is always `collection` for dataset collections.
                                   (maps from 'type')
        type_id (HdcaDetailedTypeId | None)
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
    name: HdcaDetailedName  # The name of the item.
    populated_state: DatasetCollectionPopulatedState
    tags: list[str]  # The collection of tags associated with an item.
    update_time: HdcaDetailedUpdateTime  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    visible: bool  # Whether this item is visible or hidden to the user by default.
    column_definitions: HdcaDetailedColumnDefinitions | None = (
        None  # Column data associated with each element of this collection.
    )
    element_count: HdcaDetailedElementCount | None = (
        None  # The number of elements contained in the dataset collection. It may be None or undefined if the collection could not be populated.
    )
    elements: list[DceSummary2] | None = field(
        default_factory=list
    )  # The summary information of each of the elements inside the dataset collection.
    implicit_collection_jobs_id: HdcaDetailedImplicitCollectionJobsId | None = (
        None  # Encoded ID for the ICJ object describing the collection of jobs corresponding to this collection
    )
    job_source_id: HdcaDetailedJobSourceId | None = (
        None  # The encoded ID of the Job that produced this dataset collection. Used to track the state of the job.
    )
    job_source_type: HdcaDetailedJobSourceType | None = (
        None  # The type of job (model class) that produced this dataset collection. Used to track the state of the job.
    )
    job_state_summary: HdcaDetailedJobStateSummary | None = (
        None  # Overview of the job states working inside the dataset collection.
    )
    populated: bool | None = (
        None  # Whether the dataset collection elements (and any subcollections elements) were successfully populated.
    )
    populated_state_message: HdcaDetailedPopulatedStateMessage | None = (
        None  # Optional message with further information in case the population of the dataset collection failed.
    )
    store_times_summary: HdcaDetailedStoreTimesSummary | None = (
        None  # A list of objects containing the object store ID and the oldest creation time of the datasets stored in that object store for this collection.This is used to determine the age of the datasets in the collection when the object store is short-lived.
    )
    type_: str | None = "collection"  # This is always `collection` for dataset collections. (maps from 'type')
    type_id: HdcaDetailedTypeId | None = None  # The type and the encoded ID of this item. Used for caching.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "collection_id": "collection_id",
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "contents_url": "contents_url",
            "create_time": "create_time",
            "deleted": "deleted",
            "element_count": "element_count",
            "elements": "elements",
            "elements_datatypes": "elements_datatypes",
            "elements_deleted": "elements_deleted",
            "elements_states": "elements_states",
            "hid": "hid",
            "history_content_type": "history_content_type",
            "history_id": "history_id",
            "id": "id_",
            "implicit_collection_jobs_id": "implicit_collection_jobs_id",
            "job_source_id": "job_source_id",
            "job_source_type": "job_source_type",
            "job_state_summary": "job_state_summary",
            "model_class": "model_class",
            "name": "name",
            "populated": "populated",
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
            "column_definitions": "column_definitions",
            "contents_url": "contents_url",
            "create_time": "create_time",
            "deleted": "deleted",
            "element_count": "element_count",
            "elements": "elements",
            "elements_datatypes": "elements_datatypes",
            "elements_deleted": "elements_deleted",
            "elements_states": "elements_states",
            "hid": "hid",
            "history_content_type": "history_content_type",
            "history_id": "history_id",
            "id_": "id",
            "implicit_collection_jobs_id": "implicit_collection_jobs_id",
            "job_source_id": "job_source_id",
            "job_source_type": "job_source_type",
            "job_state_summary": "job_state_summary",
            "model_class": "model_class",
            "name": "name",
            "populated": "populated",
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
