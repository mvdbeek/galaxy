from dataclasses import dataclass

from .update_content_item import UpdateContentItem

__all__ = ["UpdateHistoryContentsBatchPayload"]


@dataclass
class UpdateHistoryContentsBatchPayload:
    """
    Contains property values that will be updated for all the history `items` provided.

    Args:
        items (List[UpdateContentItem])
                                 : A list of content items to update with the changes.
    """

    items: list[UpdateContentItem]  # A list of content items to update with the changes.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "items": "items",
        }
        key_transform_with_dump = {
            "items": "items",
        }
