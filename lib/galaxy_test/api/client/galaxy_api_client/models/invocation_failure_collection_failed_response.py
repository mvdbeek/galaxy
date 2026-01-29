from dataclasses import dataclass

from .invocation_message_response_union_reason_enum import InvocationMessageResponseUnionReasonEnum

__all__ = ["InvocationFailureCollectionFailedResponse"]


@dataclass
class InvocationFailureCollectionFailedResponse:
    """
    InvocationFailureCollectionFailedResponse dataclass

    Args:
        dependent_workflow_step_id (int)
                                 : Workflow step id of step that caused failure.
        hdca_id (str)            : HistoryDatasetCollectionAssociation ID that relates to
                                   failure.
        reason (InvocationMessageResponseUnionReasonEnum)
                                 :
        workflow_step_id (int)   : Workflow step id of step that failed.
    """

    dependent_workflow_step_id: int  # Workflow step id of step that caused failure.
    hdca_id: str  # HistoryDatasetCollectionAssociation ID that relates to failure.
    reason: InvocationMessageResponseUnionReasonEnum
    workflow_step_id: int  # Workflow step id of step that failed.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "dependent_workflow_step_id": "dependent_workflow_step_id",
            "hdca_id": "hdca_id",
            "reason": "reason",
            "workflow_step_id": "workflow_step_id",
        }
        key_transform_with_dump = {
            "dependent_workflow_step_id": "dependent_workflow_step_id",
            "hdca_id": "hdca_id",
            "reason": "reason",
            "workflow_step_id": "workflow_step_id",
        }
