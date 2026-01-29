from dataclasses import dataclass

from .invocation_failure_dataset_failed_response_dependent_workflow_step_id import (
    InvocationFailureDatasetFailedResponseDependentWorkflowStepId,
)
from .invocation_message_response_union_reason_enum import InvocationMessageResponseUnionReasonEnum

__all__ = ["InvocationFailureDatasetFailedResponse"]


@dataclass
class InvocationFailureDatasetFailedResponse:
    """
    InvocationFailureDatasetFailedResponse dataclass

    Args:
        hda_id (str)             : HistoryDatasetAssociation ID that relates to failure.
        reason (InvocationMessageResponseUnionReasonEnum)
                                 :
        workflow_step_id (int)   : Workflow step id of step that failed.
        dependent_workflow_step_id (InvocationFailureDatasetFailedResponseDependentWorkflowStepId | None)
                                 : Workflow step id of step that caused failure.
    """

    hda_id: str  # HistoryDatasetAssociation ID that relates to failure.
    reason: InvocationMessageResponseUnionReasonEnum
    workflow_step_id: int  # Workflow step id of step that failed.
    dependent_workflow_step_id: InvocationFailureDatasetFailedResponseDependentWorkflowStepId | None = (
        None  # Workflow step id of step that caused failure.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "dependent_workflow_step_id": "dependent_workflow_step_id",
            "hda_id": "hda_id",
            "reason": "reason",
            "workflow_step_id": "workflow_step_id",
        }
        key_transform_with_dump = {
            "dependent_workflow_step_id": "dependent_workflow_step_id",
            "hda_id": "hda_id",
            "reason": "reason",
            "workflow_step_id": "workflow_step_id",
        }
