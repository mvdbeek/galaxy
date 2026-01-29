from dataclasses import dataclass

from .invocation_step_jobs_response_job_model_states import InvocationStepJobsResponseJobModelStates
from .job_state import JobState

__all__ = ["InvocationStepJobsResponseJobModel"]


@dataclass
class InvocationStepJobsResponseJobModel:
    """
    InvocationStepJobsResponseJobModel dataclass.

    Args:
        id_ (str)                : The encoded ID of the job.
        model_ (str)             :
        populated_state (JobState):
        states (InvocationStepJobsResponseJobModelStates)
                                 : The states of all the jobs related to the Invocation.
    """

    id_: str  # The encoded ID of the job.
    model_: str
    populated_state: JobState
    states: InvocationStepJobsResponseJobModelStates  # The states of all the jobs related to the Invocation.
