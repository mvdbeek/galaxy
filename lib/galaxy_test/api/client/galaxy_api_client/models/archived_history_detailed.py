from dataclasses import dataclass
from datetime import datetime

from .archived_history_detailed_annotation import ArchivedHistoryDetailedAnnotation
from .archived_history_detailed_export_record_data import ArchivedHistoryDetailedExportRecordData
from .archived_history_detailed_genome_build import ArchivedHistoryDetailedGenomeBuild
from .archived_history_detailed_preferred_object_store_id import ArchivedHistoryDetailedPreferredObjectStoreId
from .archived_history_detailed_slug import ArchivedHistoryDetailedSlug
from .archived_history_detailed_state_details import ArchivedHistoryDetailedStateDetails
from .archived_history_detailed_state_ids import ArchivedHistoryDetailedStateIds
from .archived_history_detailed_user_id import ArchivedHistoryDetailedUserId
from .archived_history_detailed_username import ArchivedHistoryDetailedUsername
from .archived_history_detailed_username_and_slug import ArchivedHistoryDetailedUsernameAndSlug
from .dataset_state import DatasetState

__all__ = ["ArchivedHistoryDetailed"]


@dataclass
class ArchivedHistoryDetailed:
    """
    ArchivedHistoryDetailed dataclass

    Args:
        annotation (ArchivedHistoryDetailedAnnotation)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        archived (bool)          : Whether this item has been archived and is no longer
                                   active.
        contents_url (str)       : The relative URL to access the contents of this History.
        count (int)              : The number of items in the history.
        create_time (datetime)   : The time and date this item was created.
        deleted (bool)           : Whether this item is marked as deleted.
        id_ (str)                : Maps from 'id'
        importable (bool)        : Whether this History can be imported by other users with
                                   a shared link.
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the history.
        published (bool)         : Whether this resource is currently publicly available to
                                   all users.
        purged (bool)            : Whether this item has been permanently removed.
        size (int)               : The total size of the contents of this history in bytes.
        state (DatasetState)     :
        state_details (ArchivedHistoryDetailedStateDetails)
                                 : A dictionary keyed to possible dataset states and valued
                                   with the number of datasets in this history that have
                                   those states.
        state_ids (ArchivedHistoryDetailedStateIds)
                                 : A dictionary keyed to possible dataset states and valued
                                   with lists containing the ids of each HDA in that state.
        tags (List[str])         : The collection of tags associated with an item.
        update_time (datetime)   : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        export_record_data (ArchivedHistoryDetailedExportRecordData | None)
                                 : The export record data associated with this archived
                                   history. Used to recover the history.
        genome_build (ArchivedHistoryDetailedGenomeBuild | None)
                                 : TODO
        preferred_object_store_id (ArchivedHistoryDetailedPreferredObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   new datasets in this history.
        slug (ArchivedHistoryDetailedSlug | None)
                                 : Part of the URL to uniquely identify this History by link
                                   in a readable way.
        user_id (ArchivedHistoryDetailedUserId | None)
                                 : The encoded ID of the user that owns this History.
        username (ArchivedHistoryDetailedUsername | None)
                                 : Owner of the history
        username_and_slug (ArchivedHistoryDetailedUsernameAndSlug | None)
                                 : The relative URL in the form of /u/{username}/h/{slug}
    """

    annotation: ArchivedHistoryDetailedAnnotation  # An annotation to provide details or to help understand the purpose and usage of this item.
    archived: bool  # Whether this item has been archived and is no longer active.
    contents_url: str  # The relative URL to access the contents of this History.
    count: int  # The number of items in the history.
    create_time: datetime  # The time and date this item was created.
    deleted: bool  # Whether this item is marked as deleted.
    id_: str  # Maps from 'id'
    importable: bool  # Whether this History can be imported by other users with a shared link.
    model_class: str  # The name of the database model class.
    name: str  # The name of the history.
    published: bool  # Whether this resource is currently publicly available to all users.
    purged: bool  # Whether this item has been permanently removed.
    size: int  # The total size of the contents of this history in bytes.
    state: DatasetState
    state_details: ArchivedHistoryDetailedStateDetails  # A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states.
    state_ids: ArchivedHistoryDetailedStateIds  # A dictionary keyed to possible dataset states and valued with lists containing the ids of each HDA in that state.
    tags: list[str]  # The collection of tags associated with an item.
    update_time: datetime  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    export_record_data: ArchivedHistoryDetailedExportRecordData | None = (
        None  # The export record data associated with this archived history. Used to recover the history.
    )
    genome_build: ArchivedHistoryDetailedGenomeBuild | None = "?"  # TODO
    preferred_object_store_id: ArchivedHistoryDetailedPreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store new datasets in this history.
    )
    slug: ArchivedHistoryDetailedSlug | None = (
        None  # Part of the URL to uniquely identify this History by link in a readable way.
    )
    user_id: ArchivedHistoryDetailedUserId | None = None  # The encoded ID of the user that owns this History.
    username: ArchivedHistoryDetailedUsername | None = None  # Owner of the history
    username_and_slug: ArchivedHistoryDetailedUsernameAndSlug | None = (
        None  # The relative URL in the form of /u/{username}/h/{slug}
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "archived": "archived",
            "contents_url": "contents_url",
            "count": "count",
            "create_time": "create_time",
            "deleted": "deleted",
            "export_record_data": "export_record_data",
            "genome_build": "genome_build",
            "id": "id_",
            "importable": "importable",
            "model_class": "model_class",
            "name": "name",
            "preferred_object_store_id": "preferred_object_store_id",
            "published": "published",
            "purged": "purged",
            "size": "size",
            "slug": "slug",
            "state": "state",
            "state_details": "state_details",
            "state_ids": "state_ids",
            "tags": "tags",
            "update_time": "update_time",
            "url": "url",
            "user_id": "user_id",
            "username": "username",
            "username_and_slug": "username_and_slug",
        }
        key_transform_with_dump = {
            "annotation": "annotation",
            "archived": "archived",
            "contents_url": "contents_url",
            "count": "count",
            "create_time": "create_time",
            "deleted": "deleted",
            "export_record_data": "export_record_data",
            "genome_build": "genome_build",
            "id_": "id",
            "importable": "importable",
            "model_class": "model_class",
            "name": "name",
            "preferred_object_store_id": "preferred_object_store_id",
            "published": "published",
            "purged": "purged",
            "size": "size",
            "slug": "slug",
            "state": "state",
            "state_details": "state_details",
            "state_ids": "state_ids",
            "tags": "tags",
            "update_time": "update_time",
            "url": "url",
            "user_id": "user_id",
            "username": "username",
            "username_and_slug": "username_and_slug",
        }
