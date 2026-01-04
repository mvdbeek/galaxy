from dataclasses import dataclass

__all__ = ["InvocationEvaluationWarningWorkflowOutputNotFoundResponse"]


@dataclass
class InvocationEvaluationWarningWorkflowOutputNotFoundResponse:
    """
    InvocationEvaluationWarningWorkflowOutputNotFoundResponse dataclass.

    Args:
        output_name (str)        : Output that was designated as workflow output but that
                                   has not been found
        reason (str)             :
        workflow_step_id (int)   :
    """

    output_name: str  # Output that was designated as workflow output but that has not been found
    reason: str
    workflow_step_id: int
