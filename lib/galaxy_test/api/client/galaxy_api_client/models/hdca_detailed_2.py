from dataclasses import dataclass, field
from datetime import datetime

from .column_definitions import ColumnDefinitions
from .dataset_collection_populated_state import DatasetCollectionPopulatedState
from .dce_summary_9 import DceSummary9
from .element_count import ElementCount
from .elements_datatypes import ElementsDatatypes
from .elements_states_dict import ElementsStatesDict
from .implicit_collection_jobs_id import ImplicitCollectionJobsId
from .job_source_id import JobSourceId
from .job_source_type import JobSourceType
from .job_state_summary import JobStateSummary
from .name import Name
from .populated_state_message import PopulatedStateMessage
from .store_times_summary import StoreTimesSummary
from .tags import Tags
from .type_id import TypeId
from .update_time import UpdateTime

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
        elements_datatypes (ElementsDatatypes)
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
        id_ (str)                :
        model_class (str)        : The name of the database model class.
        name (Optional[Name])    : The name of the creator.
        populated_state (DatasetCollectionPopulatedState)
                                 :
        tags (Tags)              : The collection of tags associated with an item.
        update_time (Optional[UpdateTime])
                                 : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        visible (bool)           : Whether this item is visible or hidden to the user by
                                   default.
        column_definitions (Optional[ColumnDefinitions])
                                 : Column data associated with each element of this
                                   collection.
        element_count (Optional[ElementCount])
                                 : The number of elements contained in the dataset
                                   collection. It may be None or undefined if the collection
                                   could not be populated.
        elements (Optional[List[DceSummary9]])
                                 : The summary information of each of the elements inside
                                   the dataset collection.
        implicit_collection_jobs_id (Optional[ImplicitCollectionJobsId])
                                 : The implicit collection job ID associated with the
                                   workflow invocation step.
        job_source_id (Optional[JobSourceId])
                                 : The encoded ID of the Job that produced this dataset
                                   collection. Used to track the state of the job.
        job_source_type (Optional[JobSourceType])
                                 : The type of job (model class) that produced this dataset
                                   collection. Used to track the state of the job.
        job_state_summary (Optional[JobStateSummary])
                                 : Overview of the job states working inside the dataset
                                   collection.
        populated (Optional[bool]): Whether the dataset collection elements (and any
                                    subcollections elements) were successfully populated.
        populated_state_message (Optional[PopulatedStateMessage])
                                 : Optional message with further information in case the
                                   population of the dataset collection failed.
        store_times_summary (Optional[StoreTimesSummary])
                                 : A list of objects containing the object store ID and the
                                   oldest creation time of the datasets stored in that
                                   object store for this collection.This is used to
                                   determine the age of the datasets in the collection when
                                   the object store is short-lived.
        type_ (Optional[str])    : This is always `collection` for dataset collections.
        type_id (Optional[TypeId]): The type and the encoded ID of this item. Used for
                                    caching.
    """

    collection_id: str
    collection_type: str  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    contents_url: str  # The relative URL to access the contents of this History.
    create_time: datetime  # The time and date this item was created.
    deleted: bool  # Whether this item is marked as deleted.
    elements_datatypes: ElementsDatatypes  # A set containing all the different element datatypes in the collection.
    elements_deleted: int  # The number of elements in the collection that are marked as deleted.
    elements_states: ElementsStatesDict
    hid: int  # The index position of this item in the History.
    history_content_type: str  # This is always `dataset_collection` for dataset collections.
    history_id: str
    id_: str
    model_class: str  # The name of the database model class.
    name: Name | None  # The name of the creator.
    populated_state: DatasetCollectionPopulatedState
    tags: Tags  # The collection of tags associated with an item.
    update_time: UpdateTime | None  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    visible: bool  # Whether this item is visible or hidden to the user by default.
    column_definitions: ColumnDefinitions | None = None  # Column data associated with each element of this collection.
    element_count: ElementCount | None = (
        None  # The number of elements contained in the dataset collection. It may be None or undefined if the collection could not be populated.
    )
    elements: list[DceSummary9] | None = field(
        default_factory=list
    )  # The summary information of each of the elements inside the dataset collection.
    implicit_collection_jobs_id: ImplicitCollectionJobsId | None = (
        None  # The implicit collection job ID associated with the workflow invocation step.
    )
    job_source_id: JobSourceId | None = (
        None  # The encoded ID of the Job that produced this dataset collection. Used to track the state of the job.
    )
    job_source_type: JobSourceType | None = (
        None  # The type of job (model class) that produced this dataset collection. Used to track the state of the job.
    )
    job_state_summary: JobStateSummary | None = (
        None  # Overview of the job states working inside the dataset collection.
    )
    populated: bool | None = (
        None  # Whether the dataset collection elements (and any subcollections elements) were successfully populated.
    )
    populated_state_message: PopulatedStateMessage | None = (
        None  # Optional message with further information in case the population of the dataset collection failed.
    )
    store_times_summary: StoreTimesSummary | None = (
        None  # A list of objects containing the object store ID and the oldest creation time of the datasets stored in that object store for this collection.This is used to determine the age of the datasets in the collection when the object store is short-lived.
    )
    type_: str | None = "collection"  # This is always `collection` for dataset collections.
    type_id: TypeId | None = None  # The type and the encoded ID of this item. Used for caching.
