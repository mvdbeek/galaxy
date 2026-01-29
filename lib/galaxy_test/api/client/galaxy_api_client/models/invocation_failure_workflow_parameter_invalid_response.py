from dataclasses import dataclass

from .invocation_message_response_union_reason_enum import InvocationMessageResponseUnionReasonEnum

__all__ = ["InvocationFailureWorkflowParameterInvalidResponse"]


@dataclass
class InvocationFailureWorkflowParameterInvalidResponse:
    """
    InvocationFailureWorkflowParameterInvalidResponse dataclass

    Args:
        details (str)            : Message raised by validator
        reason (InvocationMessageResponseUnionReasonEnum)
                                 :
        workflow_step_id (int)   :
    """

    details: str  # Message raised by validator
    reason: InvocationMessageResponseUnionReasonEnum
    workflow_step_id: int

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
