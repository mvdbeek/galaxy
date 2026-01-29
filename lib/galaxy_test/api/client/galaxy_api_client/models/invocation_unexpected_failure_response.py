from dataclasses import dataclass

from .invocation_message_response_union_reason_enum import InvocationMessageResponseUnionReasonEnum
from .invocation_unexpected_failure_response_details import InvocationUnexpectedFailureResponseDetails
from .invocation_unexpected_failure_response_workflow_step_id import InvocationUnexpectedFailureResponseWorkflowStepId

__all__ = ["InvocationUnexpectedFailureResponse"]


@dataclass
class InvocationUnexpectedFailureResponse:
    """
    InvocationUnexpectedFailureResponse dataclass

    Args:
        reason (InvocationMessageResponseUnionReasonEnum)
                                 :
        details (InvocationUnexpectedFailureResponseDetails | None)
                                 : May contains details to help troubleshoot this problem.
        workflow_step_id (InvocationUnexpectedFailureResponseWorkflowStepId | None)
                                 : Workflow step id of step that failed.
    """

    reason: InvocationMessageResponseUnionReasonEnum
    details: InvocationUnexpectedFailureResponseDetails | None = (
        None  # May contains details to help troubleshoot this problem.
    )
    workflow_step_id: InvocationUnexpectedFailureResponseWorkflowStepId | None = (
        None  # Workflow step id of step that failed.
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
