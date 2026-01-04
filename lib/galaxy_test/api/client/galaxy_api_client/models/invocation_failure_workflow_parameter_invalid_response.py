from dataclasses import dataclass

__all__ = ["InvocationFailureWorkflowParameterInvalidResponse"]


@dataclass
class InvocationFailureWorkflowParameterInvalidResponse:
    """
    InvocationFailureWorkflowParameterInvalidResponse dataclass.

    Args:
        details (str)            : Message raised by validator
        reason (str)             :
        workflow_step_id (int)   :
    """

    details: str  # Message raised by validator
    reason: str
    workflow_step_id: int
