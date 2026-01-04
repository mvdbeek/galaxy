from dataclasses import dataclass

__all__ = ["InvocationFailureCollectionFailedResponse"]


@dataclass
class InvocationFailureCollectionFailedResponse:
    """
    InvocationFailureCollectionFailedResponse dataclass.

    Args:
        dependent_workflow_step_id (int)
                                 : Workflow step id of step that caused failure.
        hdca_id (str)            : HistoryDatasetCollectionAssociation ID that relates to
                                   failure.
        reason (str)             :
        workflow_step_id (int)   : Workflow step id of step that failed.
    """

    dependent_workflow_step_id: int  # Workflow step id of step that caused failure.
    hdca_id: str  # HistoryDatasetCollectionAssociation ID that relates to failure.
    reason: str
    workflow_step_id: int  # Workflow step id of step that failed.
