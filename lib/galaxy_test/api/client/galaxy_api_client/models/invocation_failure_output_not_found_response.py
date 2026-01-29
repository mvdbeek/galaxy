from dataclasses import dataclass

from .invocation_message_response_union_reason_enum import InvocationMessageResponseUnionReasonEnum

__all__ = ["InvocationFailureOutputNotFoundResponse"]


@dataclass
class InvocationFailureOutputNotFoundResponse:
    """
    InvocationFailureOutputNotFoundResponse dataclass

    Args:
        dependent_workflow_step_id (int)
                                 : Workflow step id of step that caused failure.
        output_name (str)        :
        reason (InvocationMessageResponseUnionReasonEnum)
                                 :
        workflow_step_id (int)   : Workflow step id of step that failed.
    """

    dependent_workflow_step_id: int  # Workflow step id of step that caused failure.
    output_name: str
    reason: InvocationMessageResponseUnionReasonEnum
    workflow_step_id: int  # Workflow step id of step that failed.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "dependent_workflow_step_id": "dependent_workflow_step_id",
            "output_name": "output_name",
            "reason": "reason",
            "workflow_step_id": "workflow_step_id",
        }
        key_transform_with_dump = {
            "dependent_workflow_step_id": "dependent_workflow_step_id",
            "output_name": "output_name",
            "reason": "reason",
            "workflow_step_id": "workflow_step_id",
        }
