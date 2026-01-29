from dataclasses import dataclass
from datetime import datetime

from .archived_history_summary_annotation import ArchivedHistorySummaryAnnotation
from .archived_history_summary_export_record_data import ArchivedHistorySummaryExportRecordData
from .archived_history_summary_preferred_object_store_id import ArchivedHistorySummaryPreferredObjectStoreId

__all__ = ["ArchivedHistorySummary"]


@dataclass
class ArchivedHistorySummary:
    """
    ArchivedHistorySummary dataclass

    Args:
        annotation (ArchivedHistorySummaryAnnotation)
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
        export_record_data (ArchivedHistorySummaryExportRecordData | None)
                                 : The export record data associated with this archived
                                   history. Used to recover the history.
        preferred_object_store_id (ArchivedHistorySummaryPreferredObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   new datasets in this history.
    """

    annotation: ArchivedHistorySummaryAnnotation  # An annotation to provide details or to help understand the purpose and usage of this item.
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
    export_record_data: ArchivedHistorySummaryExportRecordData | None = (
        None  # The export record data associated with this archived history. Used to recover the history.
    )
    preferred_object_store_id: ArchivedHistorySummaryPreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store new datasets in this history.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "archived": "archived",
            "count": "count",
            "deleted": "deleted",
            "export_record_data": "export_record_data",
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
            "export_record_data": "export_record_data",
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
