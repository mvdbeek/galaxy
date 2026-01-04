from dataclasses import dataclass

from .invocation_jobs_response_states import InvocationJobsResponseStates
from .job_state import JobState

__all__ = ["InvocationJobsResponse"]


@dataclass
class InvocationJobsResponse:
    """
    InvocationJobsResponse dataclass.

    Args:
        id_ (str)                : The encoded ID of the workflow invocation.
        model_ (str)             :
        populated_state (JobState):
        states (InvocationJobsResponseStates)
                                 : The states of all the jobs related to the Invocation.
    """

    id_: str  # The encoded ID of the workflow invocation.
    model_: str
    populated_state: JobState
    states: InvocationJobsResponseStates  # The states of all the jobs related to the Invocation.
