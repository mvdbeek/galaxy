from dataclasses import dataclass
from datetime import datetime

from .annotation import Annotation
from .dataset_state import DatasetState
from .export_record_data import ExportRecordData
from .genome_build import GenomeBuild
from .preferred_object_store_id import PreferredObjectStoreId
from .slug import Slug
from .state_details import StateDetails
from .state_ids import StateIds
from .tags import Tags
from .user_id import UserId
from .username import Username
from .username_and_slug import UsernameAndSlug

__all__ = ["ArchivedHistoryDetailed"]


@dataclass
class ArchivedHistoryDetailed:
    """
    ArchivedHistoryDetailed dataclass.

    Args:
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        archived (bool)          : Whether this item has been archived and is no longer
                                   active.
        contents_url (str)       : The relative URL to access the contents of this History.
        count (int)              : The number of items in the history.
        create_time (datetime)   : The time and date this item was created.
        deleted (bool)           : Whether this item is marked as deleted.
        id_ (str)                :
        importable (bool)        : Whether this History can be imported by other users with
                                   a shared link.
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the history.
        published (bool)         : Whether this resource is currently publicly available to
                                   all users.
        purged (bool)            : Whether this item has been permanently removed.
        size (int)               : The total size of the contents of this history in bytes.
        state (DatasetState)     :
        state_details (StateDetails)
                                 : A dictionary keyed to possible dataset states and valued
                                   with the number of datasets in this history that have
                                   those states.
        state_ids (StateIds)     : A dictionary keyed to possible dataset states and valued
                                   with lists containing the ids of each HDA in that state.
        tags (Tags)              : The collection of tags associated with an item.
        update_time (datetime)   : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        export_record_data (Optional[ExportRecordData])
                                 : The export record data associated with this archived
                                   history. Used to recover the history.
        genome_build (Optional[GenomeBuild])
                                 : TODO
        preferred_object_store_id (Optional[PreferredObjectStoreId])
                                 : The ID of the object store that should be used to store
                                   all datasets (can instead specify object store IDs for
                                   intermediate and outputs datasts separately) -  -
                                   Galaxy's job configuration may override this in some
                                   cases but this workflow preference will override tool and
                                   user preferences
        slug (Optional[Slug])    : The slug of the visualization.
        user_id (Optional[UserId]): User ID of user that ran this job
        username (Optional[Username])
                                 : The name of the user.
        username_and_slug (Optional[UsernameAndSlug])
                                 : The relative URL in the form of
                                   /u/{username}/{resource_single_char}/{slug}
    """

    annotation: Annotation | None  # The annotation of this Visualization.
    archived: bool  # Whether this item has been archived and is no longer active.
    contents_url: str  # The relative URL to access the contents of this History.
    count: int  # The number of items in the history.
    create_time: datetime  # The time and date this item was created.
    deleted: bool  # Whether this item is marked as deleted.
    id_: str
    importable: bool  # Whether this History can be imported by other users with a shared link.
    model_class: str  # The name of the database model class.
    name: str  # The name of the history.
    published: bool  # Whether this resource is currently publicly available to all users.
    purged: bool  # Whether this item has been permanently removed.
    size: int  # The total size of the contents of this history in bytes.
    state: DatasetState
    state_details: StateDetails  # A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states.
    state_ids: StateIds  # A dictionary keyed to possible dataset states and valued with lists containing the ids of each HDA in that state.
    tags: Tags  # The collection of tags associated with an item.
    update_time: datetime  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    export_record_data: ExportRecordData | None = (
        None  # The export record data associated with this archived history. Used to recover the history.
    )
    genome_build: GenomeBuild | None = "?"  # TODO
    preferred_object_store_id: PreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
    slug: Slug | None = None  # The slug of the visualization.
    user_id: UserId | None = None  # User ID of user that ran this job
    username: Username | None = None  # The name of the user.
    username_and_slug: UsernameAndSlug | None = (
        None  # The relative URL in the form of /u/{username}/{resource_single_char}/{slug}
    )
