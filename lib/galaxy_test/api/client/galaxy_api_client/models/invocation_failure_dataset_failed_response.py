from dataclasses import dataclass

from .dependent_workflow_step_id import DependentWorkflowStepId

__all__ = ["InvocationFailureDatasetFailedResponse"]


@dataclass
class InvocationFailureDatasetFailedResponse:
    """
    InvocationFailureDatasetFailedResponse dataclass.

    Args:
        hda_id (str)             : HistoryDatasetAssociation ID that relates to failure.
        reason (str)             :
        workflow_step_id (int)   : Workflow step id of step that failed.
        dependent_workflow_step_id (Optional[DependentWorkflowStepId])
                                 : Workflow step id of step that caused failure.
    """

    hda_id: str  # HistoryDatasetAssociation ID that relates to failure.
    reason: str
    workflow_step_id: int  # Workflow step id of step that failed.
    dependent_workflow_step_id: DependentWorkflowStepId | None = None  # Workflow step id of step that caused failure.
