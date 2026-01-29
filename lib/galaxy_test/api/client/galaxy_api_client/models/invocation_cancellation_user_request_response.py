from dataclasses import dataclass

from .invocation_message_response_union_reason_enum import InvocationMessageResponseUnionReasonEnum

__all__ = ["InvocationCancellationUserRequestResponse"]


@dataclass
class InvocationCancellationUserRequestResponse:
    """
    InvocationCancellationUserRequestResponse dataclass

    Args:
        reason (InvocationMessageResponseUnionReasonEnum)
                                 :
    """

    reason: InvocationMessageResponseUnionReasonEnum

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "reason": "reason",
        }
        key_transform_with_dump = {
            "reason": "reason",
        }
