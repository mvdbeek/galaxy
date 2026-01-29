from dataclasses import dataclass, field

from .dce_summary_2 import DceSummary2
from .hdca_custom_collection_type import HdcaCustomCollectionType
from .hdca_custom_column_definitions import HdcaCustomColumnDefinitions
from .hdca_custom_contents_url import HdcaCustomContentsUrl
from .hdca_custom_create_time import HdcaCustomCreateTime
from .hdca_custom_deleted import HdcaCustomDeleted
from .hdca_custom_element_count import HdcaCustomElementCount
from .hdca_custom_elements_datatypes import HdcaCustomElementsDatatypes
from .hdca_custom_elements_deleted import HdcaCustomElementsDeleted
from .hdca_custom_elements_states import HdcaCustomElementsStates
from .hdca_custom_hid import HdcaCustomHid
from .hdca_custom_history_content_type import HdcaCustomHistoryContentType
from .hdca_custom_implicit_collection_jobs_id import HdcaCustomImplicitCollectionJobsId
from .hdca_custom_job_source_id import HdcaCustomJobSourceId
from .hdca_custom_job_source_type import HdcaCustomJobSourceType
from .hdca_custom_job_state_summary import HdcaCustomJobStateSummary
from .hdca_custom_name import HdcaCustomName
from .hdca_custom_populated_state import HdcaCustomPopulatedState
from .hdca_custom_populated_state_message import HdcaCustomPopulatedStateMessage
from .hdca_custom_store_times_summary import HdcaCustomStoreTimesSummary
from .hdca_custom_tags import HdcaCustomTags
from .hdca_custom_type_id import HdcaCustomTypeId
from .hdca_custom_update_time import HdcaCustomUpdateTime
from .hdca_custom_url import HdcaCustomUrl
from .hdca_custom_visible import HdcaCustomVisible

__all__ = ["HdcaCustom2"]


@dataclass
class HdcaCustom2:
    """
    Can contain any serializable property of an HDCA.  Allows arbitrary custom keys to be
    specified in the serialization parameters without a particular view (predefined set of
    keys).

    Args:
        collection_id (str | None):
        collection_type (HdcaCustomCollectionType | None)
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        column_definitions (HdcaCustomColumnDefinitions | None)
                                 : Column data associated with each element of this
                                   collection.
        contents_url (HdcaCustomContentsUrl | None)
                                 : The relative URL to access the contents of this History.
        create_time (HdcaCustomCreateTime | None)
                                 : The time and date this item was created.
        deleted (HdcaCustomDeleted | None)
                                 : Whether this item is marked as deleted.
        element_count (HdcaCustomElementCount | None)
                                 : The number of elements contained in the dataset
                                   collection. It may be None or undefined if the collection
                                   could not be populated.
        elements (List[DceSummary2] | None)
                                 : The summary information of each of the elements inside
                                   the dataset collection.
        elements_datatypes (HdcaCustomElementsDatatypes | None)
                                 : A set containing all the different element datatypes in
                                   the collection.
        elements_deleted (HdcaCustomElementsDeleted | None)
                                 : The number of elements in the collection that are marked
                                   as deleted.
        elements_states (HdcaCustomElementsStates | None)
                                 : A dictionary containing counts for each dataset state in
                                   the collection.
        hid (HdcaCustomHid | None): The index position of this item in the History.
        history_content_type (HdcaCustomHistoryContentType | None)
                                 : This is always `dataset_collection` for dataset
                                   collections.
        history_id (str | None)  :
        id_ (str | None)         : Maps from 'id'
        implicit_collection_jobs_id (HdcaCustomImplicitCollectionJobsId | None)
                                 : Encoded ID for the ICJ object describing the collection
                                   of jobs corresponding to this collection
        job_source_id (HdcaCustomJobSourceId | None)
                                 : The encoded ID of the Job that produced this dataset
                                   collection. Used to track the state of the job.
        job_source_type (HdcaCustomJobSourceType | None)
                                 : The type of job (model class) that produced this dataset
                                   collection. Used to track the state of the job.
        job_state_summary (HdcaCustomJobStateSummary | None)
                                 : Overview of the job states working inside the dataset
                                   collection.
        model_class (str | None) : The name of the database model class.
        name (HdcaCustomName | None)
                                 : The name of the item.
        populated (bool | None)  : Whether the dataset collection elements (and any
                                   subcollections elements) were successfully populated.
        populated_state (HdcaCustomPopulatedState | None)
                                 : Indicates the general state of the elements in the
                                   dataset collection:- 'new': new dataset collection,
                                   unpopulated elements.- 'ok': collection elements
                                   populated (HDAs may or may not have errors).- 'failed':
                                   some problem populating, won't be populated.
        populated_state_message (HdcaCustomPopulatedStateMessage | None)
                                 : Optional message with further information in case the
                                   population of the dataset collection failed.
        store_times_summary (HdcaCustomStoreTimesSummary | None)
                                 : A list of objects containing the object store ID and the
                                   oldest creation time of the datasets stored in that
                                   object store for this collection.This is used to
                                   determine the age of the datasets in the collection when
                                   the object store is short-lived.
        tags (HdcaCustomTags | None)
                                 : The collection of tags associated with an item.
        type_ (str | None)       : This is always `collection` for dataset collections.
                                   (maps from 'type')
        type_id (HdcaCustomTypeId | None)
                                 : The type and the encoded ID of this item. Used for
                                   caching.
        update_time (HdcaCustomUpdateTime | None)
                                 : The last time and date this item was updated.
        url (HdcaCustomUrl | None): The relative URL to access this item.
        visible (HdcaCustomVisible | None)
                                 : Whether this item is visible or hidden to the user by
                                   default.
    """

    collection_id: str | None = None
    collection_type: HdcaCustomCollectionType | None = (
        None  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    )
    column_definitions: HdcaCustomColumnDefinitions | None = (
        None  # Column data associated with each element of this collection.
    )
    contents_url: HdcaCustomContentsUrl | None = None  # The relative URL to access the contents of this History.
    create_time: HdcaCustomCreateTime | None = None  # The time and date this item was created.
    deleted: HdcaCustomDeleted | None = None  # Whether this item is marked as deleted.
    element_count: HdcaCustomElementCount | None = (
        None  # The number of elements contained in the dataset collection. It may be None or undefined if the collection could not be populated.
    )
    elements: list[DceSummary2] | None = field(
        default_factory=list
    )  # The summary information of each of the elements inside the dataset collection.
    elements_datatypes: HdcaCustomElementsDatatypes | None = (
        None  # A set containing all the different element datatypes in the collection.
    )
    elements_deleted: HdcaCustomElementsDeleted | None = (
        None  # The number of elements in the collection that are marked as deleted.
    )
    elements_states: HdcaCustomElementsStates | None = (
        None  # A dictionary containing counts for each dataset state in the collection.
    )
    hid: HdcaCustomHid | None = None  # The index position of this item in the History.
    history_content_type: HdcaCustomHistoryContentType | None = (
        None  # This is always `dataset_collection` for dataset collections.
    )
    history_id: str | None = None
    id_: str | None = None  # Maps from 'id'
    implicit_collection_jobs_id: HdcaCustomImplicitCollectionJobsId | None = (
        None  # Encoded ID for the ICJ object describing the collection of jobs corresponding to this collection
    )
    job_source_id: HdcaCustomJobSourceId | None = (
        None  # The encoded ID of the Job that produced this dataset collection. Used to track the state of the job.
    )
    job_source_type: HdcaCustomJobSourceType | None = (
        None  # The type of job (model class) that produced this dataset collection. Used to track the state of the job.
    )
    job_state_summary: HdcaCustomJobStateSummary | None = (
        None  # Overview of the job states working inside the dataset collection.
    )
    model_class: str | None = None  # The name of the database model class.
    name: HdcaCustomName | None = None  # The name of the item.
    populated: bool | None = (
        None  # Whether the dataset collection elements (and any subcollections elements) were successfully populated.
    )
    populated_state: HdcaCustomPopulatedState | None = (
        None  # Indicates the general state of the elements in the dataset collection:- 'new': new dataset collection, unpopulated elements.- 'ok': collection elements populated (HDAs may or may not have errors).- 'failed': some problem populating, won't be populated.
    )
    populated_state_message: HdcaCustomPopulatedStateMessage | None = (
        None  # Optional message with further information in case the population of the dataset collection failed.
    )
    store_times_summary: HdcaCustomStoreTimesSummary | None = (
        None  # A list of objects containing the object store ID and the oldest creation time of the datasets stored in that object store for this collection.This is used to determine the age of the datasets in the collection when the object store is short-lived.
    )
    tags: HdcaCustomTags | None = None  # The collection of tags associated with an item.
    type_: str | None = "collection"  # This is always `collection` for dataset collections. (maps from 'type')
    type_id: HdcaCustomTypeId | None = None  # The type and the encoded ID of this item. Used for caching.
    update_time: HdcaCustomUpdateTime | None = None  # The last time and date this item was updated.
    url: HdcaCustomUrl | None = None  # The relative URL to access this item.
    visible: HdcaCustomVisible | None = None  # Whether this item is visible or hidden to the user by default.

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
