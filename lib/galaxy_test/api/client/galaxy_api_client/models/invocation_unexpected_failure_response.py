from dataclasses import dataclass

from .details import Details
from .workflow_step_id import WorkflowStepId

__all__ = ["InvocationUnexpectedFailureResponse"]


@dataclass
class InvocationUnexpectedFailureResponse:
    """
    InvocationUnexpectedFailureResponse dataclass.

    Args:
        reason (str)             :
        details (Optional[Details])
                                 : May contains details to help troubleshoot this problem.
        workflow_step_id (Optional[WorkflowStepId])
                                 : Workflow step id of step that failed.
    """

    reason: str
    details: Details | None = None  # May contains details to help troubleshoot this problem.
    workflow_step_id: WorkflowStepId | None = None  # Workflow step id of step that failed.
