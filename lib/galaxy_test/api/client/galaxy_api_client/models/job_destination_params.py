from dataclasses import dataclass

from .handler import Handler
from .runner import Runner
from .runner_job_id import RunnerJobId

__all__ = ["JobDestinationParams"]


@dataclass
class JobDestinationParams:
    """
    JobDestinationParams dataclass.

    Args:
        handler (Optional[Handler])
                                 : The job handler process assigned to handle this job. Only
                                   administrator can see this value.
        runner (Optional[Runner]): Job runner class
        runner_job_id (Optional[RunnerJobId])
                                 : ID assigned to submitted job by external job running
                                   system
    """

    handler: Handler | None = (
        None  # The job handler process assigned to handle this job. Only administrator can see this value.
    )
    runner: Runner | None = None  # Job runner class
    runner_job_id: RunnerJobId | None = None  # ID assigned to submitted job by external job running system
