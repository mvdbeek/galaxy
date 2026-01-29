from dataclasses import dataclass

from .encoded_history_content_item import EncodedHistoryContentItem

__all__ = ["BulkOperationItemError"]


@dataclass
class BulkOperationItemError:
    """
    BulkOperationItemError dataclass.

    Args:
        error (str)              :
        item (EncodedHistoryContentItem)
                                 :
    """

    error: str
    item: EncodedHistoryContentItem
