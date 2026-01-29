from dataclasses import dataclass

__all__ = ["InvocationFailureJobFailedResponse"]


@dataclass
class InvocationFailureJobFailedResponse:
    """
    InvocationFailureJobFailedResponse dataclass.

    Args:
        dependent_workflow_step_id (int)
                                 : Workflow step id of step that caused failure.
        job_id (str)             : Job ID that relates to failure.
        reason (str)             :
        workflow_step_id (int)   : Workflow step id of step that failed.
    """

    dependent_workflow_step_id: int  # Workflow step id of step that caused failure.
    job_id: str  # Job ID that relates to failure.
    reason: str
    workflow_step_id: int  # Workflow step id of step that failed.
