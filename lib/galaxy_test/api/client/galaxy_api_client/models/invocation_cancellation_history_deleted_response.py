from dataclasses import dataclass

from .invocation_message_response_union_reason_enum import InvocationMessageResponseUnionReasonEnum

__all__ = ["InvocationCancellationHistoryDeletedResponse"]


@dataclass
class InvocationCancellationHistoryDeletedResponse:
    """
    InvocationCancellationHistoryDeletedResponse dataclass

    Args:
        history_id (str)         : History ID of history that was deleted.
        reason (InvocationMessageResponseUnionReasonEnum)
                                 :
    """

    history_id: str  # History ID of history that was deleted.
    reason: InvocationMessageResponseUnionReasonEnum

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "history_id": "history_id",
            "reason": "reason",
        }
        key_transform_with_dump = {
            "history_id": "history_id",
            "reason": "reason",
        }
