from dataclasses import dataclass

from .encoded_history_content_item import EncodedHistoryContentItem

__all__ = ["BulkOperationItemError"]


@dataclass
class BulkOperationItemError:
    """
    BulkOperationItemError dataclass

    Args:
        error (str)              :
        item (EncodedHistoryContentItem)
                                 :
    """

    error: str
    item: EncodedHistoryContentItem

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "error": "error",
            "item": "item",
        }
        key_transform_with_dump = {
            "error": "error",
            "item": "item",
        }
