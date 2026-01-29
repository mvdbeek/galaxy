from dataclasses import dataclass

from .invocation_failure_expression_evaluation_failed_response_details import (
    InvocationFailureExpressionEvaluationFailedResponseDetails,
)
from .invocation_message_response_union_reason_enum import InvocationMessageResponseUnionReasonEnum

__all__ = ["InvocationFailureExpressionEvaluationFailedResponse"]


@dataclass
class InvocationFailureExpressionEvaluationFailedResponse:
    """
    InvocationFailureExpressionEvaluationFailedResponse dataclass

    Args:
        reason (InvocationMessageResponseUnionReasonEnum)
                                 :
        workflow_step_id (int)   : Workflow step id of step that failed.
        details (InvocationFailureExpressionEvaluationFailedResponseDetails | None)
                                 : May contain details to help troubleshoot this problem.
    """

    reason: InvocationMessageResponseUnionReasonEnum
    workflow_step_id: int  # Workflow step id of step that failed.
    details: InvocationFailureExpressionEvaluationFailedResponseDetails | None = (
        None  # May contain details to help troubleshoot this problem.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "details": "details",
            "reason": "reason",
            "workflow_step_id": "workflow_step_id",
        }
        key_transform_with_dump = {
            "details": "details",
            "reason": "reason",
            "workflow_step_id": "workflow_step_id",
        }
