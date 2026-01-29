from dataclasses import dataclass

from .bulk_operation_item_error import BulkOperationItemError

__all__ = ["HistoryContentBulkOperationResult"]


@dataclass
class HistoryContentBulkOperationResult:
    """
    HistoryContentBulkOperationResult dataclass.

    Args:
        errors (List[BulkOperationItemError])
                                 :
        success_count (int)      :
    """

    errors: list[BulkOperationItemError]
    success_count: int
