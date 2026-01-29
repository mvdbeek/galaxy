from dataclasses import dataclass

from .custom_history_view_annotation import CustomHistoryViewAnnotation
from .custom_history_view_archived import CustomHistoryViewArchived
from .custom_history_view_contents_active import CustomHistoryViewContentsActive
from .custom_history_view_contents_states import CustomHistoryViewContentsStates
from .custom_history_view_contents_url import CustomHistoryViewContentsUrl
from .custom_history_view_count import CustomHistoryViewCount
from .custom_history_view_create_time import CustomHistoryViewCreateTime
from .custom_history_view_deleted import CustomHistoryViewDeleted
from .custom_history_view_genome_build import CustomHistoryViewGenomeBuild
from .custom_history_view_importable import CustomHistoryViewImportable
from .custom_history_view_name import CustomHistoryViewName
from .custom_history_view_nice_size import CustomHistoryViewNiceSize
from .custom_history_view_preferred_object_store_id import CustomHistoryViewPreferredObjectStoreId
from .custom_history_view_published import CustomHistoryViewPublished
from .custom_history_view_purged import CustomHistoryViewPurged
from .custom_history_view_size import CustomHistoryViewSize
from .custom_history_view_slug import CustomHistoryViewSlug
from .custom_history_view_state import CustomHistoryViewState
from .custom_history_view_state_details import CustomHistoryViewStateDetails
from .custom_history_view_state_ids import CustomHistoryViewStateIds
from .custom_history_view_tags import CustomHistoryViewTags
from .custom_history_view_update_time import CustomHistoryViewUpdateTime
from .custom_history_view_url import CustomHistoryViewUrl
from .custom_history_view_user_id import CustomHistoryViewUserId
from .custom_history_view_username import CustomHistoryViewUsername
from .custom_history_view_username_and_slug import CustomHistoryViewUsernameAndSlug

__all__ = ["CustomHistoryView"]


@dataclass
class CustomHistoryView:
    """
    History Response with all optional fields.  It is used for serializing only specific
    attributes using the "keys" query parameter. Unfortunately, we cannot know the exact
    fields that will be requested, so we have to allow all fields to be optional.

    Args:
        annotation (CustomHistoryViewAnnotation | None)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        archived (CustomHistoryViewArchived | None)
                                 : Whether this item has been archived and is no longer
                                   active.
        contents_active (CustomHistoryViewContentsActive | None)
                                 : Contains the number of active, deleted or hidden items in
                                   a History.
        contents_states (CustomHistoryViewContentsStates | None)
                                 : A dictionary keyed to possible dataset states and valued
                                   with the number of datasets in this history that have
                                   those states.
        contents_url (CustomHistoryViewContentsUrl | None)
                                 : The relative URL to access the contents of this History.
        count (CustomHistoryViewCount | None)
                                 : The number of items in the history.
        create_time (CustomHistoryViewCreateTime | None)
                                 : The time and date this item was created.
        deleted (CustomHistoryViewDeleted | None)
                                 : Whether this item is marked as deleted.
        genome_build (CustomHistoryViewGenomeBuild | None)
                                 : TODO
        id_ (str | None)         : Maps from 'id'
        importable (CustomHistoryViewImportable | None)
                                 : Whether this History can be imported by other users with
                                   a shared link.
        model_class (str | None) : The name of the database model class.
        name (CustomHistoryViewName | None)
                                 : The name of the history.
        nice_size (CustomHistoryViewNiceSize | None)
                                 : The total size of the contents of this history in a
                                   human-readable format.
        preferred_object_store_id (CustomHistoryViewPreferredObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   new datasets in this history.
        published (CustomHistoryViewPublished | None)
                                 : Whether this resource is currently publicly available to
                                   all users.
        purged (CustomHistoryViewPurged | None)
                                 : Whether this item has been permanently removed.
        size (CustomHistoryViewSize | None)
                                 : The total size of the contents of this history in bytes.
        slug (CustomHistoryViewSlug | None)
                                 : Part of the URL to uniquely identify this History by link
                                   in a readable way.
        state (CustomHistoryViewState | None)
                                 : The current state of the History based on the states of
                                   the datasets it contains.
        state_details (CustomHistoryViewStateDetails | None)
                                 : A dictionary keyed to possible dataset states and valued
                                   with the number of datasets in this history that have
                                   those states.
        state_ids (CustomHistoryViewStateIds | None)
                                 : A dictionary keyed to possible dataset states and valued
                                   with lists containing the ids of each HDA in that state.
        tags (CustomHistoryViewTags | None)
                                 : The collection of tags associated with an item.
        update_time (CustomHistoryViewUpdateTime | None)
                                 : The last time and date this item was updated.
        url (CustomHistoryViewUrl | None)
                                 : The relative URL to access this item.
        user_id (CustomHistoryViewUserId | None)
                                 : The encoded ID of the user that owns this History.
        username (CustomHistoryViewUsername | None)
                                 : Owner of the history
        username_and_slug (CustomHistoryViewUsernameAndSlug | None)
                                 : The relative URL in the form of /u/{username}/h/{slug}
    """

    annotation: CustomHistoryViewAnnotation | None = (
        None  # An annotation to provide details or to help understand the purpose and usage of this item.
    )
    archived: CustomHistoryViewArchived | None = None  # Whether this item has been archived and is no longer active.
    contents_active: CustomHistoryViewContentsActive | None = (
        None  # Contains the number of active, deleted or hidden items in a History.
    )
    contents_states: CustomHistoryViewContentsStates | None = (
        None  # A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states.
    )
    contents_url: CustomHistoryViewContentsUrl | None = None  # The relative URL to access the contents of this History.
    count: CustomHistoryViewCount | None = None  # The number of items in the history.
    create_time: CustomHistoryViewCreateTime | None = None  # The time and date this item was created.
    deleted: CustomHistoryViewDeleted | None = None  # Whether this item is marked as deleted.
    genome_build: CustomHistoryViewGenomeBuild | None = "?"  # TODO
    id_: str | None = None  # Maps from 'id'
    importable: CustomHistoryViewImportable | None = (
        None  # Whether this History can be imported by other users with a shared link.
    )
    model_class: str | None = None  # The name of the database model class.
    name: CustomHistoryViewName | None = None  # The name of the history.
    nice_size: CustomHistoryViewNiceSize | None = (
        None  # The total size of the contents of this history in a human-readable format.
    )
    preferred_object_store_id: CustomHistoryViewPreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store new datasets in this history.
    )
    published: CustomHistoryViewPublished | None = (
        None  # Whether this resource is currently publicly available to all users.
    )
    purged: CustomHistoryViewPurged | None = None  # Whether this item has been permanently removed.
    size: CustomHistoryViewSize | None = None  # The total size of the contents of this history in bytes.
    slug: CustomHistoryViewSlug | None = (
        None  # Part of the URL to uniquely identify this History by link in a readable way.
    )
    state: CustomHistoryViewState | None = (
        None  # The current state of the History based on the states of the datasets it contains.
    )
    state_details: CustomHistoryViewStateDetails | None = (
        None  # A dictionary keyed to possible dataset states and valued with the number of datasets in this history that have those states.
    )
    state_ids: CustomHistoryViewStateIds | None = (
        None  # A dictionary keyed to possible dataset states and valued with lists containing the ids of each HDA in that state.
    )
    tags: CustomHistoryViewTags | None = None  # The collection of tags associated with an item.
    update_time: CustomHistoryViewUpdateTime | None = None  # The last time and date this item was updated.
    url: CustomHistoryViewUrl | None = None  # The relative URL to access this item.
    user_id: CustomHistoryViewUserId | None = None  # The encoded ID of the user that owns this History.
    username: CustomHistoryViewUsername | None = None  # Owner of the history
    username_and_slug: CustomHistoryViewUsernameAndSlug | None = (
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
