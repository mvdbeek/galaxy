from dataclasses import dataclass
from datetime import datetime

from .history_summary_annotation import HistorySummaryAnnotation
from .history_summary_preferred_object_store_id import HistorySummaryPreferredObjectStoreId

__all__ = ["HistorySummary"]


@dataclass
class HistorySummary:
    """
    History summary information.

    Args:
        annotation (HistorySummaryAnnotation)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        archived (bool)          : Whether this item has been archived and is no longer
                                   active.
        count (int)              : The number of items in the history.
        deleted (bool)           : Whether this item is marked as deleted.
        id_ (str)                : Maps from 'id'
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the history.
        published (bool)         : Whether this resource is currently publicly available to
                                   all users.
        purged (bool)            : Whether this item has been permanently removed.
        tags (List[str])         : The collection of tags associated with an item.
        update_time (datetime)   : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        preferred_object_store_id (HistorySummaryPreferredObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   new datasets in this history.
    """

    annotation: HistorySummaryAnnotation  # An annotation to provide details or to help understand the purpose and usage of this item.
    archived: bool  # Whether this item has been archived and is no longer active.
    count: int  # The number of items in the history.
    deleted: bool  # Whether this item is marked as deleted.
    id_: str  # Maps from 'id'
    model_class: str  # The name of the database model class.
    name: str  # The name of the history.
    published: bool  # Whether this resource is currently publicly available to all users.
    purged: bool  # Whether this item has been permanently removed.
    tags: list[str]  # The collection of tags associated with an item.
    update_time: datetime  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    preferred_object_store_id: HistorySummaryPreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store new datasets in this history.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "archived": "archived",
            "count": "count",
            "deleted": "deleted",
            "id": "id_",
            "model_class": "model_class",
            "name": "name",
            "preferred_object_store_id": "preferred_object_store_id",
            "published": "published",
            "purged": "purged",
            "tags": "tags",
            "update_time": "update_time",
            "url": "url",
        }
        key_transform_with_dump = {
            "annotation": "annotation",
            "archived": "archived",
            "count": "count",
            "deleted": "deleted",
            "id_": "id",
            "model_class": "model_class",
            "name": "name",
            "preferred_object_store_id": "preferred_object_store_id",
            "published": "published",
            "purged": "purged",
            "tags": "tags",
            "update_time": "update_time",
            "url": "url",
        }
