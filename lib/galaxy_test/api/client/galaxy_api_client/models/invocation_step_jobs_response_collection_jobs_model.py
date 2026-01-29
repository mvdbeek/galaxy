from dataclasses import dataclass

from .invocation_step_jobs_response_collection_jobs_model_states import (
    InvocationStepJobsResponseCollectionJobsModelStates,
)
from .job_state import JobState

__all__ = ["InvocationStepJobsResponseCollectionJobsModel"]


@dataclass
class InvocationStepJobsResponseCollectionJobsModel:
    """
    InvocationStepJobsResponseCollectionJobsModel dataclass.

    Args:
        id_ (str)                : The encoded ID of the collection job.
        model_ (str)             :
        populated_state (JobState):
        states (InvocationStepJobsResponseCollectionJobsModelStates)
                                 : The states of all the jobs related to the Invocation.
    """

    id_: str  # The encoded ID of the collection job.
    model_: str
    populated_state: JobState
    states: InvocationStepJobsResponseCollectionJobsModelStates  # The states of all the jobs related to the Invocation.
