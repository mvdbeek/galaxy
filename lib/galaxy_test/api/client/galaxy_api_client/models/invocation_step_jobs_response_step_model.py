from dataclasses import dataclass

from .invocation_step_jobs_response_step_model_states import InvocationStepJobsResponseStepModelStates
from .job_state import JobState

__all__ = ["InvocationStepJobsResponseStepModel"]


@dataclass
class InvocationStepJobsResponseStepModel:
    """
    InvocationStepJobsResponseStepModel dataclass

    Args:
        id_ (str)                : The encoded ID of the workflow invocation. (maps from
                                   'id')
        model_ (str)             : Maps from 'model'
        populated_state (JobState):
        states (InvocationStepJobsResponseStepModelStates)
                                 : The states of all the jobs related to the Invocation.
    """

    id_: str  # The encoded ID of the workflow invocation. (maps from 'id')
    model_: str  # Maps from 'model'
    populated_state: JobState
    states: InvocationStepJobsResponseStepModelStates  # The states of all the jobs related to the Invocation.

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
