from dataclasses import dataclass

__all__ = ["InvocationCancellationReviewFailedResponse"]


@dataclass
class InvocationCancellationReviewFailedResponse:
    """
    InvocationCancellationReviewFailedResponse dataclass.

    Args:
        reason (str)             :
        workflow_step_id (int)   : Workflow step id of paused step that did not pass review.
    """

    reason: str
    workflow_step_id: int  # Workflow step id of paused step that did not pass review.
