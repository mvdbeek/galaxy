from dataclasses import dataclass

from .invocation_message_response_union_reason_enum import InvocationMessageResponseUnionReasonEnum

__all__ = ["InvocationEvaluationWarningWorkflowOutputNotFoundResponse"]


@dataclass
class InvocationEvaluationWarningWorkflowOutputNotFoundResponse:
    """
    InvocationEvaluationWarningWorkflowOutputNotFoundResponse dataclass

    Args:
        output_name (str)        : Output that was designated as workflow output but that
                                   has not been found
        reason (InvocationMessageResponseUnionReasonEnum)
                                 :
        workflow_step_id (int)   :
    """

    output_name: str  # Output that was designated as workflow output but that has not been found
    reason: InvocationMessageResponseUnionReasonEnum
    workflow_step_id: int

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "output_name": "output_name",
            "reason": "reason",
            "workflow_step_id": "workflow_step_id",
        }
        key_transform_with_dump = {
            "output_name": "output_name",
            "reason": "reason",
            "workflow_step_id": "workflow_step_id",
        }
