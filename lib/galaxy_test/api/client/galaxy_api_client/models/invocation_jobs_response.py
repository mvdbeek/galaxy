from dataclasses import dataclass

from .invocation_jobs_response_states import InvocationJobsResponseStates
from .job_state import JobState

__all__ = ["InvocationJobsResponse"]


@dataclass
class InvocationJobsResponse:
    """
    InvocationJobsResponse dataclass

    Args:
        id_ (str)                : The encoded ID of the workflow invocation. (maps from
                                   'id')
        model_ (str)             : Maps from 'model'
        populated_state (JobState):
        states (InvocationJobsResponseStates)
                                 : The states of all the jobs related to the Invocation.
    """

    id_: str  # The encoded ID of the workflow invocation. (maps from 'id')
    model_: str  # Maps from 'model'
    populated_state: JobState
    states: InvocationJobsResponseStates  # The states of all the jobs related to the Invocation.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "model": "model_",
            "populated_state": "populated_state",
            "states": "states",
        }
        key_transform_with_dump = {
            "id_": "id",
            "model_": "model",
            "populated_state": "populated_state",
            "states": "states",
        }
