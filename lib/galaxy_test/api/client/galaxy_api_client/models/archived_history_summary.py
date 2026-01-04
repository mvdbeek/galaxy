from dataclasses import dataclass
from datetime import datetime

from .annotation import Annotation
from .export_record_data import ExportRecordData
from .preferred_object_store_id import PreferredObjectStoreId
from .tags import Tags

__all__ = ["ArchivedHistorySummary"]


@dataclass
class ArchivedHistorySummary:
    """
    ArchivedHistorySummary dataclass.

    Args:
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        archived (bool)          : Whether this item has been archived and is no longer
                                   active.
        count (int)              : The number of items in the history.
        deleted (bool)           : Whether this item is marked as deleted.
        id_ (str)                :
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the history.
        published (bool)         : Whether this resource is currently publicly available to
                                   all users.
        purged (bool)            : Whether this item has been permanently removed.
        tags (Tags)              : The collection of tags associated with an item.
        update_time (datetime)   : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        export_record_data (Optional[ExportRecordData])
                                 : The export record data associated with this archived
                                   history. Used to recover the history.
        preferred_object_store_id (Optional[PreferredObjectStoreId])
                                 : The ID of the object store that should be used to store
                                   all datasets (can instead specify object store IDs for
                                   intermediate and outputs datasts separately) -  -
                                   Galaxy's job configuration may override this in some
                                   cases but this workflow preference will override tool and
                                   user preferences
    """

    annotation: Annotation | None  # The annotation of this Visualization.
    archived: bool  # Whether this item has been archived and is no longer active.
    count: int  # The number of items in the history.
    deleted: bool  # Whether this item is marked as deleted.
    id_: str
    model_class: str  # The name of the database model class.
    name: str  # The name of the history.
    published: bool  # Whether this resource is currently publicly available to all users.
    purged: bool  # Whether this item has been permanently removed.
    tags: Tags  # The collection of tags associated with an item.
    update_time: datetime  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    export_record_data: ExportRecordData | None = (
        None  # The export record data associated with this archived history. Used to recover the history.
    )
    preferred_object_store_id: PreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
