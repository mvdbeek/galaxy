from dataclasses import dataclass

from .details import Details

__all__ = ["InvocationFailureExpressionEvaluationFailedResponse"]


@dataclass
class InvocationFailureExpressionEvaluationFailedResponse:
    """
    InvocationFailureExpressionEvaluationFailedResponse dataclass.

    Args:
        reason (str)             :
        workflow_step_id (int)   : Workflow step id of step that failed.
        details (Optional[Details])
                                 : May contains details to help troubleshoot this problem.
    """

    reason: str
    workflow_step_id: int  # Workflow step id of step that failed.
    details: Details | None = None  # May contains details to help troubleshoot this problem.
