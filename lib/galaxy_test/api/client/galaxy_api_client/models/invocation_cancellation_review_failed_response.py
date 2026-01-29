from dataclasses import dataclass

from .invocation_message_response_union_reason_enum import InvocationMessageResponseUnionReasonEnum

__all__ = ["InvocationCancellationReviewFailedResponse"]


@dataclass
class InvocationCancellationReviewFailedResponse:
    """
    InvocationCancellationReviewFailedResponse dataclass

    Args:
        reason (InvocationMessageResponseUnionReasonEnum)
                                 :
        workflow_step_id (int)   : Workflow step id of paused step that did not pass review.
    """

    reason: InvocationMessageResponseUnionReasonEnum
    workflow_step_id: int  # Workflow step id of paused step that did not pass review.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "reason": "reason",
            "workflow_step_id": "workflow_step_id",
        }
        key_transform_with_dump = {
            "reason": "reason",
            "workflow_step_id": "workflow_step_id",
        }
