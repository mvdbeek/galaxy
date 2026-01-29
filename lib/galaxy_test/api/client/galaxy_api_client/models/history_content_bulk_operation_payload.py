from dataclasses import dataclass

from .history_content_bulk_operation_payload_items import HistoryContentBulkOperationPayloadItems
from .history_content_bulk_operation_payload_params import HistoryContentBulkOperationPayloadParams
from .history_content_item_operation import HistoryContentItemOperation

__all__ = ["HistoryContentBulkOperationPayload"]


@dataclass
class HistoryContentBulkOperationPayload:
    """
    HistoryContentBulkOperationPayload dataclass

    Args:
        operation (HistoryContentItemOperation)
                                 :
        items (HistoryContentBulkOperationPayloadItems | None)
                                 :
        params (HistoryContentBulkOperationPayloadParams | None)
                                 :
    """

    operation: HistoryContentItemOperation
    items: HistoryContentBulkOperationPayloadItems | None = None
    params: HistoryContentBulkOperationPayloadParams | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "items": "items",
            "operation": "operation",
            "params": "params",
        }
        key_transform_with_dump = {
            "items": "items",
            "operation": "operation",
            "params": "params",
        }
