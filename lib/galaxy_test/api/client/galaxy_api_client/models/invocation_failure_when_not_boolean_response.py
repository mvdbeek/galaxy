from dataclasses import dataclass

from .invocation_message_response_union_reason_enum import InvocationMessageResponseUnionReasonEnum

__all__ = ["InvocationFailureWhenNotBooleanResponse"]


@dataclass
class InvocationFailureWhenNotBooleanResponse:
    """
    InvocationFailureWhenNotBooleanResponse dataclass

    Args:
        details (str)            : Contains details to help troubleshoot this problem.
        reason (InvocationMessageResponseUnionReasonEnum)
                                 :
        workflow_step_id (int)   : Workflow step id of step that failed.
    """

    details: str  # Contains details to help troubleshoot this problem.
    reason: InvocationMessageResponseUnionReasonEnum
    workflow_step_id: int  # Workflow step id of step that failed.

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
