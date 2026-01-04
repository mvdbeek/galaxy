from dataclasses import dataclass

__all__ = ["InvocationFailureOutputNotFoundResponse"]


@dataclass
class InvocationFailureOutputNotFoundResponse:
    """
    InvocationFailureOutputNotFoundResponse dataclass.

    Args:
        dependent_workflow_step_id (int)
                                 : Workflow step id of step that caused failure.
        output_name (str)        :
        reason (str)             :
        workflow_step_id (int)   : Workflow step id of step that failed.
    """

    dependent_workflow_step_id: int  # Workflow step id of step that caused failure.
    output_name: str
    reason: str
    workflow_step_id: int  # Workflow step id of step that failed.
