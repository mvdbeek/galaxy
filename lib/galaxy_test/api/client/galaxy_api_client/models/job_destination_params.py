from dataclasses import dataclass

from .job_destination_params_handler import JobDestinationParamsHandler
from .job_destination_params_runner import JobDestinationParamsRunner
from .job_destination_params_runner_job_id import JobDestinationParamsRunnerJobId

__all__ = ["JobDestinationParams"]


@dataclass
class JobDestinationParams:
    """
    JobDestinationParams dataclass

    Args:
        handler (JobDestinationParamsHandler | None)
                                 : Name of the process that handled the job. (maps from
                                   'Handler')
        runner (JobDestinationParamsRunner | None)
                                 : Job runner class (maps from 'Runner')
        runner_job_id (JobDestinationParamsRunnerJobId | None)
                                 : ID assigned to submitted job by external job running
                                   system (maps from 'Runner Job ID')
    """

    handler: JobDestinationParamsHandler | None = (
        None  # Name of the process that handled the job. (maps from 'Handler')
    )
    runner: JobDestinationParamsRunner | None = None  # Job runner class (maps from 'Runner')
    runner_job_id: JobDestinationParamsRunnerJobId | None = (
        None  # ID assigned to submitted job by external job running system (maps from 'Runner Job ID')
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "Handler": "handler",
            "Runner": "runner",
            "Runner Job ID": "runner_job_id",
        }
        key_transform_with_dump = {
            "handler": "Handler",
            "runner": "Runner",
            "runner_job_id": "Runner Job ID",
        }
