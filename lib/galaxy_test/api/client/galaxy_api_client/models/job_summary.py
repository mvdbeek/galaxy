from dataclasses import dataclass
from datetime import datetime

from .command_line import CommandLine
from .exit_code import ExitCode
from .external_id import ExternalId
from .galaxy_version import GalaxyVersion
from .handler import Handler
from .history_id import HistoryId
from .job_runner_name import JobRunnerName
from .job_state import JobState
from .user_email_7 import UserEmail7
from .user_id import UserId

__all__ = ["JobSummary"]


@dataclass
class JobSummary:
    """
    Basic information about a job.

    Args:
        create_time (datetime)   : The time and date this item was created.
        id_ (str)                :
        model_class (str)        : The name of the database model class.
        state (JobState)         :
        tool_id (str)            : Identifier of the tool that generated this job.
        update_time (datetime)   : The last time and date this item was updated.
        command_line (Optional[CommandLine])
                                 : The command line produced by the job. Users can see this
                                   value if allowed in the configuration, administrator can
                                   always see this value.
        exit_code (Optional[ExitCode])
                                 : The exit code returned by the tool. Can be unset if the
                                   job is not completed yet.
        external_id (Optional[ExternalId])
                                 : The job id used by the external job runner (Condor,
                                   Pulsar, etc.). Only administrator can see this value.
        galaxy_version (Optional[GalaxyVersion])
                                 : The (major) version of Galaxy used to create this job.
        handler (Optional[Handler])
                                 : The job handler process assigned to handle this job. Only
                                   administrator can see this value.
        history_id (Optional[HistoryId])
                                 : The encoded ID of the history associated with this item.
        job_runner_name (Optional[JobRunnerName])
                                 : Name of the job runner plugin that handles this job. Only
                                   administrator can see this value.
        user_email (Optional[UserEmail7])
                                 : The email of the user that owns this job. Only the owner
                                   of the job and administrators can see this value.
        user_id (Optional[UserId]): User ID of user that ran this job
    """

    create_time: datetime  # The time and date this item was created.
    id_: str
    model_class: str  # The name of the database model class.
    state: JobState
    tool_id: str  # Identifier of the tool that generated this job.
    update_time: datetime  # The last time and date this item was updated.
    command_line: CommandLine | None = (
        None  # The command line produced by the job. Users can see this value if allowed in the configuration, administrator can always see this value.
    )
    exit_code: ExitCode | None = (
        None  # The exit code returned by the tool. Can be unset if the job is not completed yet.
    )
    external_id: ExternalId | None = (
        None  # The job id used by the external job runner (Condor, Pulsar, etc.). Only administrator can see this value.
    )
    galaxy_version: GalaxyVersion | None = None  # The (major) version of Galaxy used to create this job.
    handler: Handler | None = (
        None  # The job handler process assigned to handle this job. Only administrator can see this value.
    )
    history_id: HistoryId | None = None  # The encoded ID of the history associated with this item.
    job_runner_name: JobRunnerName | None = (
        None  # Name of the job runner plugin that handles this job. Only administrator can see this value.
    )
    user_email: UserEmail7 | None = (
        None  # The email of the user that owns this job. Only the owner of the job and administrators can see this value.
    )
    user_id: UserId | None = None  # User ID of user that ran this job
