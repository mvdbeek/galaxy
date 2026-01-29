from dataclasses import dataclass

from .bulk_operation_item_error import BulkOperationItemError

__all__ = ["HistoryContentBulkOperationResult"]


@dataclass
class HistoryContentBulkOperationResult:
    """
    HistoryContentBulkOperationResult dataclass

    Args:
        errors (List[BulkOperationItemError])
                                 :
        success_count (int)      :
    """

    errors: list[BulkOperationItemError]
    success_count: int

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "errors": "errors",
            "success_count": "success_count",
        }
        key_transform_with_dump = {
            "errors": "errors",
            "success_count": "success_count",
        }
