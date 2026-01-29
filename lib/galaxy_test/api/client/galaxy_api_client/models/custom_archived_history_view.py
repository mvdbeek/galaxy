from dataclasses import dataclass

from .custom_archived_history_view_annotation import CustomArchivedHistoryViewAnnotation
from .custom_archived_history_view_archived import CustomArchivedHistoryViewArchived
from .custom_archived_history_view_contents_active import CustomArchivedHistoryViewContentsActive
from .custom_archived_history_view_contents_states import CustomArchivedHistoryViewContentsStates
from .custom_archived_history_view_contents_url import CustomArchivedHistoryViewContentsUrl
from .custom_archived_history_view_count import CustomArchivedHistoryViewCount
from .custom_archived_history_view_create_time import CustomArchivedHistoryViewCreateTime
from .custom_archived_history_view_deleted import CustomArchivedHistoryViewDeleted
from .custom_archived_history_view_export_record_data import CustomArchivedHistoryViewExportRecordData
from .custom_archived_history_view_genome_build import CustomArchivedHistoryViewGenomeBuild
from .custom_archived_history_view_importable import CustomArchivedHistoryViewImportable
from .custom_archived_history_view_name import CustomArchivedHistoryViewName
from .custom_archived_history_view_nice_size import CustomArchivedHistoryViewNiceSize
from .custom_archived_history_view_preferred_object_store_id import CustomArchivedHistoryViewPreferredObjectStoreId
from .custom_archived_history_view_published import CustomArchivedHistoryViewPublished
from .custom_archived_history_view_purged import CustomArchivedHistoryViewPurged
from .custom_archived_history_view_size import CustomArchivedHistoryViewSize
from .custom_archived_history_view_slug import CustomArchivedHistoryViewSlug
from .custom_archived_history_view_state import CustomArchivedHistoryViewState
from .custom_archived_history_view_state_details import CustomArchivedHistoryViewStateDetails
from .custom_archived_history_view_state_ids import CustomArchivedHistoryViewStateIds
from .custom_archived_history_view_tags import CustomArchivedHistoryViewTags
from .custom_archived_history_view_update_time import CustomArchivedHistoryViewUpdateTime
from .custom_archived_history_view_url import CustomArchivedHistoryViewUrl
from .custom_archived_history_view_user_id import CustomArchivedHistoryViewUserId
from .custom_archived_history_view_username import CustomArchivedHistoryViewUsername
from .custom_archived_history_view_username_and_slug import CustomArchivedHistoryViewUsernameAndSlug

__all__ = ["CustomArchivedHistoryView"]


@dataclass
class CustomArchivedHistoryView:
    """
    Archived History Response with all optional fields.  It is used for serializing only
    specific attributes using the "keys" query parameter.

    Args:
        annotation (CustomArchivedHistoryViewAnnotation | None)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        archived (CustomArchivedHistoryViewArchived | None)
                                 : Whether this item has been archived and is no longer
                                   active.
        contents_active (CustomArchivedHistoryViewContentsActive | None)
                                 : Contains the number of active, deleted or hidden items in
                                   a History.
        contents_states (CustomArchivedHistoryViewContentsStates | None)
                                 : A dictionary keyed to possible dataset states and valued
                                   with the number of datasets in this history that have
                                   those states.
        contents_url (CustomArchivedHistoryViewContentsUrl | None)
                                 : The relative URL to access the contents of this History.
        count (CustomArchivedHistoryViewCount | None)
                                 : The number of items in the history.
        create_time (CustomArchivedHistoryViewCreateTime | None)
                                 : The time and date this item was created.
        deleted (CustomArchivedHistoryViewDeleted | None)
                                 : Whether this item is marked as deleted.
        export_record_data (CustomArchivedHistoryViewExportRecordData | None)
                                 : The export record data associated with this archived
                                   history. Used to recover the history.
        genome_build (CustomArchivedHistoryViewGenomeBuild | None)
                                 : TODO
        id_ (str | None)         : Maps from 'id'
        importable (CustomArchivedHistoryViewImportable | None)
                                 : Whether this History can be imported by other users with
                                   a shared link.
        model_class (str | None) : The name of the database model class.
        name (CustomArchivedHistoryViewName | None)
                                 : The name of the history.
        nice_size (CustomArchivedHistoryViewNiceSize | None)
                                 : The total size of the contents of this history in a
                                   human-readable format.
        preferred_object_store_id (CustomArchivedHistoryViewPreferredObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   new datasets in this history.
        published (CustomArchivedHistoryViewPublished | None)
                                 : Whether this resource is currently publicly available to
                                   all users.
        purged (CustomArchivedHistoryViewPurged | None)
                                 : Whether this item has been permanently removed.
        size (CustomArchivedHistoryViewSize | None)
                                 : The total size of the contents of this history in bytes.
        slug (CustomArchivedHistoryViewSlug | None)
                                 : Part of the URL to uniquely identify this History by link
                                   in a readable way.
        state (CustomArchivedHistoryViewState | None)
                                 : The current state of the History based on the states of
                                   the datasets it contains.
        state_details (CustomArchivedHistoryViewStateDetails | None)
                                 : A dictionary keyed to possible dataset states and valued
                                   with the number of datasets in this history that have
                                   those states.
        state_ids (CustomArchivedHistoryViewStateIds | None)
                                 : A dictionary keyed to possible dataset states and valued
                                   with lists containing the ids of each HDA in that state.
        tags (CustomArchivedHistoryViewTags | None)
                                 : The collection of tags associated with an item.
        update_time (CustomArchivedHistoryViewUpdateTime | None)
                                 : The last time and date this item was updated.
        url (CustomArchivedHistoryViewUrl | None)
                                 : The relative URL to access this item.
        user_id (CustomArchivedHistoryViewUserId | None)
                                 : The encoded ID of the user that owns this History.
        username (CustomArchivedHistoryViewUsername | None)
                                 : Owner of the history
        username_and_slug (CustomArchivedHistoryViewUsernameAndSlug | None)
                                 : The relative URL in the form of /u/{username}/h/{slug}
    """

    annotation: CustomArchivedHistoryViewAnnotation | None = (
        None  # An annotation to provide details or to help understand the purpose and usage of this item.
    )
    archived: CustomArchivedHistoryViewArchived | None = (
        None  # Whether this item has been archived and is no longer active.
    )
    contents_active: CustomArchivedHistoryViewContentsActive | None = (
        None  # Contains the number of active, deleted or hidden items in a History.
    )
    contents_states: CustomArchivedHistoryViewContentsStates | None = (
        None  # A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states.
    )
    contents_url: CustomArchivedHistoryViewContentsUrl | None = (
        None  # The relative URL to access the contents of this History.
    )
    count: CustomArchivedHistoryViewCount | None = None  # The number of items in the history.
    create_time: CustomArchivedHistoryViewCreateTime | None = None  # The time and date this item was created.
    deleted: CustomArchivedHistoryViewDeleted | None = None  # Whether this item is marked as deleted.
    export_record_data: CustomArchivedHistoryViewExportRecordData | None = (
        None  # The export record data associated with this archived history. Used to recover the history.
    )
    genome_build: CustomArchivedHistoryViewGenomeBuild | None = "?"  # TODO
    id_: str | None = None  # Maps from 'id'
    importable: CustomArchivedHistoryViewImportable | None = (
        None  # Whether this History can be imported by other users with a shared link.
    )
    model_class: str | None = None  # The name of the database model class.
    name: CustomArchivedHistoryViewName | None = None  # The name of the history.
    nice_size: CustomArchivedHistoryViewNiceSize | None = (
        None  # The total size of the contents of this history in a human-readable format.
    )
    preferred_object_store_id: CustomArchivedHistoryViewPreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store new datasets in this history.
    )
    published: CustomArchivedHistoryViewPublished | None = (
        None  # Whether this resource is currently publicly available to all users.
    )
    purged: CustomArchivedHistoryViewPurged | None = None  # Whether this item has been permanently removed.
    size: CustomArchivedHistoryViewSize | None = None  # The total size of the contents of this history in bytes.
    slug: CustomArchivedHistoryViewSlug | None = (
        None  # Part of the URL to uniquely identify this History by link in a readable way.
    )
    state: CustomArchivedHistoryViewState | None = (
        None  # The current state of the History based on the states of the datasets it contains.
    )
    state_details: CustomArchivedHistoryViewStateDetails | None = (
        None  # A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states.
    )
    state_ids: CustomArchivedHistoryViewStateIds | None = (
        None  # A dictionary keyed to possible dataset states and valued with lists containing the ids of each HDA in that state.
    )
    tags: CustomArchivedHistoryViewTags | None = None  # The collection of tags associated with an item.
    update_time: CustomArchivedHistoryViewUpdateTime | None = None  # The last time and date this item was updated.
    url: CustomArchivedHistoryViewUrl | None = None  # The relative URL to access this item.
    user_id: CustomArchivedHistoryViewUserId | None = None  # The encoded ID of the user that owns this History.
    username: CustomArchivedHistoryViewUsername | None = None  # Owner of the history
    username_and_slug: CustomArchivedHistoryViewUsernameAndSlug | None = (
        None  # The relative URL in the form of /u/{username}/h/{slug}
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "archived": "archived",
            "contents_active": "contents_active",
            "contents_states": "contents_states",
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
            "nice_size": "nice_size",
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
            "contents_active": "contents_active",
            "contents_states": "contents_states",
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
            "nice_size": "nice_size",
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
