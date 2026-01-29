from dataclasses import dataclass

from .update_history_contents_payload_annotation import UpdateHistoryContentsPayloadAnnotation
from .update_history_contents_payload_deleted import UpdateHistoryContentsPayloadDeleted
from .update_history_contents_payload_name import UpdateHistoryContentsPayloadName
from .update_history_contents_payload_tags import UpdateHistoryContentsPayloadTags
from .update_history_contents_payload_visible import UpdateHistoryContentsPayloadVisible

__all__ = ["UpdateHistoryContentsPayload"]


@dataclass
class UpdateHistoryContentsPayload:
    """
    Can contain arbitrary/dynamic fields that will be updated for a particular history item.

    Args:
        annotation (UpdateHistoryContentsPayloadAnnotation | None)
                                 : A user-defined annotation for this item.
        deleted (UpdateHistoryContentsPayloadDeleted | None)
                                 : Whether this item is marked as deleted.
        name (UpdateHistoryContentsPayloadName | None)
                                 : The new name of the item.
        tags (UpdateHistoryContentsPayloadTags | None)
                                 : A list of tags to add to this item.
        visible (UpdateHistoryContentsPayloadVisible | None)
                                 : Whether this item is visible in the history.
    """

    annotation: UpdateHistoryContentsPayloadAnnotation | None = None  # A user-defined annotation for this item.
    deleted: UpdateHistoryContentsPayloadDeleted | None = None  # Whether this item is marked as deleted.
    name: UpdateHistoryContentsPayloadName | None = None  # The new name of the item.
    tags: UpdateHistoryContentsPayloadTags | None = None  # A list of tags to add to this item.
    visible: UpdateHistoryContentsPayloadVisible | None = None  # Whether this item is visible in the history.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "deleted": "deleted",
            "name": "name",
            "tags": "tags",
            "visible": "visible",
        }
        key_transform_with_dump = {
            "annotation": "annotation",
            "deleted": "deleted",
            "name": "name",
            "tags": "tags",
            "visible": "visible",
        }
