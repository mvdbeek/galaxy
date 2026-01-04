from dataclasses import dataclass

__all__ = ["InvocationFailureWhenNotBooleanResponse"]


@dataclass
class InvocationFailureWhenNotBooleanResponse:
    """
    InvocationFailureWhenNotBooleanResponse dataclass.

    Args:
        details (str)            : Contains details to help troubleshoot this problem.
        reason (str)             :
        workflow_step_id (int)   : Workflow step id of step that failed.
    """

    details: str  # Contains details to help troubleshoot this problem.
    reason: str
    workflow_step_id: int  # Workflow step id of step that failed.
