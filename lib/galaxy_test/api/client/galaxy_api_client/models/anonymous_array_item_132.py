from typing import TypeAlias

from .invocation_step_jobs_response_collection_jobs_model import InvocationStepJobsResponseCollectionJobsModel
from .invocation_step_jobs_response_job_model import InvocationStepJobsResponseJobModel
from .invocation_step_jobs_response_step_model import InvocationStepJobsResponseStepModel

__all__ = ["AnonymousArrayItem132"]

AnonymousArrayItem132: TypeAlias = (
    InvocationStepJobsResponseStepModel
    | InvocationStepJobsResponseJobModel
    | InvocationStepJobsResponseCollectionJobsModel
)
