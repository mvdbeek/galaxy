from dataclasses import dataclass

from .invocation_step_jobs_response_collection_jobs_model_states import (
    InvocationStepJobsResponseCollectionJobsModelStates,
)
from .job_state import JobState

__all__ = ["InvocationStepJobsResponseCollectionJobsModel"]


@dataclass
class InvocationStepJobsResponseCollectionJobsModel:
    """
    InvocationStepJobsResponseCollectionJobsModel dataclass

    Args:
        id_ (str)                : The encoded ID of the collection job. (maps from 'id')
        model_ (str)             : Maps from 'model'
        populated_state (JobState):
        states (InvocationStepJobsResponseCollectionJobsModelStates)
                                 : The states of all the jobs related to the Invocation.
    """

    id_: str  # The encoded ID of the collection job. (maps from 'id')
    model_: str  # Maps from 'model'
    populated_state: JobState
    states: InvocationStepJobsResponseCollectionJobsModelStates  # The states of all the jobs related to the Invocation.

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
