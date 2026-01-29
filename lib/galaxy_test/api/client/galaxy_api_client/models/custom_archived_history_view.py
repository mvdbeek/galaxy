from dataclasses import dataclass

from .annotation import Annotation
from .archived import Archived
from .contents_active import ContentsActive
from .contents_states import ContentsStates
from .contents_url import ContentsUrl
from .count import Count
from .create_time import CreateTime
from .deleted import Deleted
from .export_record_data import ExportRecordData
from .genome_build import GenomeBuild
from .importable import Importable
from .model_class import ModelClass
from .name import Name
from .nice_size import NiceSize
from .preferred_object_store_id import PreferredObjectStoreId
from .published import Published
from .purged import Purged
from .size import Size
from .slug import Slug
from .state import State
from .state_details import StateDetails
from .state_ids import StateIds
from .tags import Tags
from .update_time import UpdateTime
from .url import Url
from .user_id import UserId
from .username import Username
from .username_and_slug import UsernameAndSlug

__all__ = ["CustomArchivedHistoryView"]


@dataclass
class CustomArchivedHistoryView:
    """
    Archived History Response with all optional fields.  It is used for serializing only
    specific attributes using the "keys" query parameter.

    Args:
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        archived (Optional[Archived])
                                 : Whether this item has been archived and is no longer
                                   active.
        contents_active (Optional[ContentsActive])
                                 : Contains the number of active, deleted or hidden items in
                                   a History.
        contents_states (Optional[ContentsStates])
                                 : A dictionary keyed to possible dataset states and valued
                                   with the number of datasets in this history that have
                                   those states.
        contents_url (Optional[ContentsUrl])
                                 : The relative URL to access the contents of this History.
        count (Optional[Count])  : The number of items in the history.
        create_time (Optional[CreateTime])
                                 : The time and date this item was created.
        deleted (Optional[Deleted])
                                 : Whether this Visualization has been deleted.
        export_record_data (Optional[ExportRecordData])
                                 : The export record data associated with this archived
                                   history. Used to recover the history.
        genome_build (Optional[GenomeBuild])
                                 : TODO
        id_ (Optional[str])      :
        importable (Optional[Importable])
                                 : Indicates if the workflow is importable by the current
                                   user.
        model_class (Optional[ModelClass])
                                 : The name of the database model class.
        name (Optional[Name])    : The name of the creator.
        nice_size (Optional[NiceSize])
                                 : The total size of the contents of this history in a
                                   human-readable format.
        preferred_object_store_id (Optional[PreferredObjectStoreId])
                                 : The ID of the object store that should be used to store
                                   all datasets (can instead specify object store IDs for
                                   intermediate and outputs datasts separately) -  -
                                   Galaxy's job configuration may override this in some
                                   cases but this workflow preference will override tool and
                                   user preferences
        published (Optional[Published])
                                 : Whether this resource is currently publicly available to
                                   all users.
        purged (Optional[Purged]): Whether this dataset has been removed from disk.
        size (Optional[Size])    : The total size of the contents of this history in bytes.
        slug (Optional[Slug])    : The slug of the visualization.
        state (Optional[State])  : Current state of the job.
        state_details (Optional[StateDetails])
                                 : A dictionary keyed to possible dataset states and valued
                                   with the number of datasets in this history that have
                                   those states.
        state_ids (Optional[StateIds])
                                 : A dictionary keyed to possible dataset states and valued
                                   with lists containing the ids of each HDA in that state.
        tags (Optional[Tags])    : The collection of tags associated with an item.
        update_time (Optional[UpdateTime])
                                 : The last time and date this item was updated.
        url (Optional[Url])      : The relative URL to access this item.
        user_id (Optional[UserId]): User ID of user that ran this job
        username (Optional[Username])
                                 : The name of the user.
        username_and_slug (Optional[UsernameAndSlug])
                                 : The relative URL in the form of
                                   /u/{username}/{resource_single_char}/{slug}
    """

    annotation: Annotation | None = None  # The annotation of this Visualization.
    archived: Archived | None = None  # Whether this item has been archived and is no longer active.
    contents_active: ContentsActive | None = (
        None  # Contains the number of active, deleted or hidden items in a History.
    )
    contents_states: ContentsStates | None = (
        None  # A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states.
    )
    contents_url: ContentsUrl | None = None  # The relative URL to access the contents of this History.
    count: Count | None = None  # The number of items in the history.
    create_time: CreateTime | None = None  # The time and date this item was created.
    deleted: Deleted | None = False  # Whether this Visualization has been deleted.
    export_record_data: ExportRecordData | None = (
        None  # The export record data associated with this archived history. Used to recover the history.
    )
    genome_build: GenomeBuild | None = "?"  # TODO
    id_: str | None = None
    importable: Importable | None = None  # Indicates if the workflow is importable by the current user.
    model_class: ModelClass | None = None  # The name of the database model class.
    name: Name | None = None  # The name of the creator.
    nice_size: NiceSize | None = None  # The total size of the contents of this history in a human-readable format.
    preferred_object_store_id: PreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
    published: Published | None = None  # Whether this resource is currently publicly available to all users.
    purged: Purged | None = None  # Whether this dataset has been removed from disk.
    size: Size | None = None  # The total size of the contents of this history in bytes.
    slug: Slug | None = None  # The slug of the visualization.
    state: State | None = None  # Current state of the job.
    state_details: StateDetails | None = (
        None  # A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states.
    )
    state_ids: StateIds | None = (
        None  # A dictionary keyed to possible dataset states and valued with lists containing the ids of each HDA in that state.
    )
    tags: Tags | None = None  # The collection of tags associated with an item.
    update_time: UpdateTime | None = None  # The last time and date this item was updated.
    url: Url | None = None  # The relative URL to access this item.
    user_id: UserId | None = None  # User ID of user that ran this job
    username: Username | None = None  # The name of the user.
    username_and_slug: UsernameAndSlug | None = (
        None  # The relative URL in the form of /u/{username}/{resource_single_char}/{slug}
    )
