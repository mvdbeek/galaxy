from dataclasses import dataclass, field

from .collection_type import CollectionType
from .column_definitions import ColumnDefinitions
from .contents_url import ContentsUrl
from .create_time import CreateTime
from .dce_summary_9 import DceSummary9
from .deleted import Deleted
from .element_count import ElementCount
from .elements_datatypes import ElementsDatatypes
from .elements_deleted import ElementsDeleted
from .elements_states import ElementsStates
from .hid import Hid
from .history_content_type import HistoryContentType
from .implicit_collection_jobs_id import ImplicitCollectionJobsId
from .job_source_id import JobSourceId
from .job_source_type import JobSourceType
from .job_state_summary import JobStateSummary
from .model_class import ModelClass
from .name import Name
from .populated_state import PopulatedState
from .populated_state_message import PopulatedStateMessage
from .store_times_summary import StoreTimesSummary
from .tags import Tags
from .type_id import TypeId
from .update_time import UpdateTime
from .url import Url
from .visible import Visible

__all__ = ["HdcaCustom"]


@dataclass
class HdcaCustom:
    """
    Can contain any serializable property of an HDCA.  Allows arbitrary custom keys to be
    specified in the serialization parameters without a particular view (predefined set of
    keys).

    Args:
        collection_id (Optional[str])
                                 :
        collection_type (Optional[CollectionType])
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        column_definitions (Optional[ColumnDefinitions])
                                 : Column data associated with each element of this
                                   collection.
        contents_url (Optional[ContentsUrl])
                                 : The relative URL to access the contents of this History.
        create_time (Optional[CreateTime])
                                 : The time and date this item was created.
        deleted (Optional[Deleted])
                                 : Whether this Visualization has been deleted.
        element_count (Optional[ElementCount])
                                 : The number of elements contained in the dataset
                                   collection. It may be None or undefined if the collection
                                   could not be populated.
        elements (Optional[List[DceSummary9]])
                                 : The summary information of each of the elements inside
                                   the dataset collection.
        elements_datatypes (Optional[ElementsDatatypes])
                                 : A set containing all the different element datatypes in
                                   the collection.
        elements_deleted (Optional[ElementsDeleted])
                                 : The number of elements in the collection that are marked
                                   as deleted.
        elements_states (Optional[ElementsStates])
                                 : A dictionary containing counts for each dataset state in
                                   the collection.
        hid (Optional[Hid])      : The index position of this item in the History.
        history_content_type (Optional[HistoryContentType])
                                 : This is always `dataset_collection` for dataset
                                   collections.
        history_id (Optional[str]):
        id_ (Optional[str])      :
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
        model_class (Optional[ModelClass])
                                 : The name of the database model class.
        name (Optional[Name])    : The name of the creator.
        populated (Optional[bool]): Whether the dataset collection elements (and any
                                    subcollections elements) were successfully populated.
        populated_state (Optional[PopulatedState])
                                 : Indicates the general state of the elements in the
                                   dataset collection:- 'new': new dataset collection,
                                   unpopulated elements.- 'ok': collection elements
                                   populated (HDAs may or may not have errors).- 'failed':
                                   some problem populating, won't be populated.
        populated_state_message (Optional[PopulatedStateMessage])
                                 : Optional message with further information in case the
                                   population of the dataset collection failed.
        store_times_summary (Optional[StoreTimesSummary])
                                 : A list of objects containing the object store ID and the
                                   oldest creation time of the datasets stored in that
                                   object store for this collection.This is used to
                                   determine the age of the datasets in the collection when
                                   the object store is short-lived.
        tags (Optional[Tags])    : The collection of tags associated with an item.
        type_ (Optional[str])    : This is always `collection` for dataset collections.
        type_id (Optional[TypeId]): The type and the encoded ID of this item. Used for
                                    caching.
        update_time (Optional[UpdateTime])
                                 : The last time and date this item was updated.
        url (Optional[Url])      : The relative URL to access this item.
        visible (Optional[Visible])
                                 : Whether this item is visible in the history.
    """

    collection_id: str | None = None
    collection_type: CollectionType | None = (
        None  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    )
    column_definitions: ColumnDefinitions | None = None  # Column data associated with each element of this collection.
    contents_url: ContentsUrl | None = None  # The relative URL to access the contents of this History.
    create_time: CreateTime | None = None  # The time and date this item was created.
    deleted: Deleted | None = False  # Whether this Visualization has been deleted.
    element_count: ElementCount | None = (
        None  # The number of elements contained in the dataset collection. It may be None or undefined if the collection could not be populated.
    )
    elements: list[DceSummary9] | None = field(
        default_factory=list
    )  # The summary information of each of the elements inside the dataset collection.
    elements_datatypes: ElementsDatatypes | None = (
        None  # A set containing all the different element datatypes in the collection.
    )
    elements_deleted: ElementsDeleted | None = (
        None  # The number of elements in the collection that are marked as deleted.
    )
    elements_states: ElementsStates | None = (
        None  # A dictionary containing counts for each dataset state in the collection.
    )
    hid: Hid | None = None  # The index position of this item in the History.
    history_content_type: HistoryContentType | None = (
        None  # This is always `dataset_collection` for dataset collections.
    )
    history_id: str | None = None
    id_: str | None = None
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
    model_class: ModelClass | None = None  # The name of the database model class.
    name: Name | None = None  # The name of the creator.
    populated: bool | None = (
        None  # Whether the dataset collection elements (and any subcollections elements) were successfully populated.
    )
    populated_state: PopulatedState | None = (
        None  # Indicates the general state of the elements in the dataset collection:- 'new': new dataset collection, unpopulated elements.- 'ok': collection elements populated (HDAs may or may not have errors).- 'failed': some problem populating, won't be populated.
    )
    populated_state_message: PopulatedStateMessage | None = (
        None  # Optional message with further information in case the population of the dataset collection failed.
    )
    store_times_summary: StoreTimesSummary | None = (
        None  # A list of objects containing the object store ID and the oldest creation time of the datasets stored in that object store for this collection.This is used to determine the age of the datasets in the collection when the object store is short-lived.
    )
    tags: Tags | None = None  # The collection of tags associated with an item.
    type_: str | None = "collection"  # This is always `collection` for dataset collections.
    type_id: TypeId | None = None  # The type and the encoded ID of this item. Used for caching.
    update_time: UpdateTime | None = None  # The last time and date this item was updated.
    url: Url | None = None  # The relative URL to access this item.
    visible: Visible | None = None  # Whether this item is visible in the history.
