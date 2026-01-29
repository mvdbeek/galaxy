from dataclasses import dataclass
from datetime import datetime

from .job_state import JobState
from .job_summary_command_line import JobSummaryCommandLine
from .job_summary_exit_code import JobSummaryExitCode
from .job_summary_external_id import JobSummaryExternalId
from .job_summary_galaxy_version import JobSummaryGalaxyVersion
from .job_summary_handler import JobSummaryHandler
from .job_summary_history_id import JobSummaryHistoryId
from .job_summary_job_runner_name import JobSummaryJobRunnerName
from .job_summary_user_email import JobSummaryUserEmail
from .job_summary_user_id import JobSummaryUserId

__all__ = ["JobSummary"]


@dataclass
class JobSummary:
    """
    Basic information about a job.

    Args:
        create_time (datetime)   : The time and date this item was created.
        id_ (str)                : Maps from 'id'
        model_class (str)        : The name of the database model class.
        state (JobState)         :
        tool_id (str)            : Identifier of the tool that generated this job.
        update_time (datetime)   : The last time and date this item was updated.
        command_line (JobSummaryCommandLine | None)
                                 : The command line produced by the job. Users can see this
                                   value if allowed in the configuration, administrator can
                                   always see this value.
        exit_code (JobSummaryExitCode | None)
                                 : The exit code returned by the tool. Can be unset if the
                                   job is not completed yet.
        external_id (JobSummaryExternalId | None)
                                 : The job id used by the external job runner (Condor,
                                   Pulsar, etc.). Only administrator can see this value.
        galaxy_version (JobSummaryGalaxyVersion | None)
                                 : The (major) version of Galaxy used to create this job.
        handler (JobSummaryHandler | None)
                                 : The job handler process assigned to handle this job. Only
                                   administrator can see this value.
        history_id (JobSummaryHistoryId | None)
                                 : The encoded ID of the history associated with this item.
        job_runner_name (JobSummaryJobRunnerName | None)
                                 : Name of the job runner plugin that handles this job. Only
                                   administrator can see this value.
        user_email (JobSummaryUserEmail | None)
                                 : The email of the user that owns this job. Only the owner
                                   of the job and administrators can see this value.
        user_id (JobSummaryUserId | None)
                                 : The encoded ID of the user that owns this job.
    """

    create_time: datetime  # The time and date this item was created.
    id_: str  # Maps from 'id'
    model_class: str  # The name of the database model class.
    state: JobState
    tool_id: str  # Identifier of the tool that generated this job.
    update_time: datetime  # The last time and date this item was updated.
    command_line: JobSummaryCommandLine | None = (
        None  # The command line produced by the job. Users can see this value if allowed in the configuration, administrator can always see this value.
    )
    exit_code: JobSummaryExitCode | None = (
        None  # The exit code returned by the tool. Can be unset if the job is not completed yet.
    )
    external_id: JobSummaryExternalId | None = (
        None  # The job id used by the external job runner (Condor, Pulsar, etc.). Only administrator can see this value.
    )
    galaxy_version: JobSummaryGalaxyVersion | None = None  # The (major) version of Galaxy used to create this job.
    handler: JobSummaryHandler | None = (
        None  # The job handler process assigned to handle this job. Only administrator can see this value.
    )
    history_id: JobSummaryHistoryId | None = None  # The encoded ID of the history associated with this item.
    job_runner_name: JobSummaryJobRunnerName | None = (
        None  # Name of the job runner plugin that handles this job. Only administrator can see this value.
    )
    user_email: JobSummaryUserEmail | None = (
        None  # The email of the user that owns this job. Only the owner of the job and administrators can see this value.
    )
    user_id: JobSummaryUserId | None = None  # The encoded ID of the user that owns this job.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "command_line": "command_line",
            "create_time": "create_time",
            "exit_code": "exit_code",
            "external_id": "external_id",
            "galaxy_version": "galaxy_version",
            "handler": "handler",
            "history_id": "history_id",
            "id": "id_",
            "job_runner_name": "job_runner_name",
            "model_class": "model_class",
            "state": "state",
            "tool_id": "tool_id",
            "update_time": "update_time",
            "user_email": "user_email",
            "user_id": "user_id",
        }
        key_transform_with_dump = {
            "command_line": "command_line",
            "create_time": "create_time",
            "exit_code": "exit_code",
            "external_id": "external_id",
            "galaxy_version": "galaxy_version",
            "handler": "handler",
            "history_id": "history_id",
            "id_": "id",
            "job_runner_name": "job_runner_name",
            "model_class": "model_class",
            "state": "state",
            "tool_id": "tool_id",
            "update_time": "update_time",
            "user_email": "user_email",
            "user_id": "user_id",
        }
