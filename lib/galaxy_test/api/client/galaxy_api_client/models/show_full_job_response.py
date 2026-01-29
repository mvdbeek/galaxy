from dataclasses import dataclass
from datetime import datetime

from .command_line import CommandLine
from .command_version import CommandVersion
from .copied_from_job_id import CopiedFromJobId
from .dependencies import Dependencies
from .exit_code import ExitCode
from .external_id import ExternalId
from .galaxy_version import GalaxyVersion
from .handler import Handler
from .history_id import HistoryId
from .inputs import Inputs
from .job_messages import JobMessages
from .job_metrics import JobMetrics
from .job_runner_name import JobRunnerName
from .job_state import JobState
from .job_stderr import JobStderr
from .job_stdout import JobStdout
from .outputs import Outputs
from .params import Params
from .show_full_job_response_output_collections import ShowFullJobResponseOutputCollections
from .stderr import Stderr
from .stdout import Stdout
from .tool_stderr import ToolStderr
from .tool_stdout import ToolStdout
from .user_email_7 import UserEmail7
from .user_id import UserId

__all__ = ["ShowFullJobResponse"]


@dataclass
class ShowFullJobResponse:
    """
    ShowFullJobResponse dataclass.

    Args:
        create_time (datetime)   : The time and date this item was created.
        id_ (str)                :
        model_class (str)        : The name of the database model class.
        params (Params)          : Object containing all the parameters of the tool
                                   associated with this job. The specific parameters depend
                                   on the tool itself.
        state (JobState)         :
        tool_id (str)            : Identifier of the tool that generated this job.
        update_time (datetime)   : The last time and date this item was updated.
        command_line (Optional[CommandLine])
                                 : The command line produced by the job. Users can see this
                                   value if allowed in the configuration, administrator can
                                   always see this value.
        command_version (Optional[CommandVersion])
                                 : Tool version indicated during job execution.
        copied_from_job_id (Optional[CopiedFromJobId])
                                 : Reference to cached job if job execution was cached.
        dependencies (Optional[Dependencies])
                                 : The dependencies of the job.
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
        inputs (Optional[Inputs]): Dictionary mapping all the tool inputs (by name) to the
                                   corresponding data references.
        job_messages (Optional[JobMessages])
                                 : List with additional information and possible reasons for
                                   a failed job.
        job_metrics (Optional[JobMetrics])
                                 : Collections of metrics provided by `JobInstrumenter`
                                   plugins on a particular job. Only administrators can see
                                   these metrics.
        job_runner_name (Optional[JobRunnerName])
                                 : Name of the job runner plugin that handles this job. Only
                                   administrator can see this value.
        job_stderr (Optional[JobStderr])
                                 : The captured standard error of the job execution.
        job_stdout (Optional[JobStdout])
                                 : The captured standard output of the job execution.
        output_collections (Optional[ShowFullJobResponseOutputCollections])
                                 :
        outputs (Optional[Outputs])
                                 : Dictionary mapping all the tool outputs (by name) to the
                                   corresponding data references.
        stderr (Optional[Stderr]): Combined tool and job standard error streams.
        stdout (Optional[Stdout]): Combined tool and job standard output streams.
        tool_stderr (Optional[ToolStderr])
                                 : The captured standard error of the tool executed by the
                                   job.
        tool_stdout (Optional[ToolStdout])
                                 : The captured standard output of the tool executed by the
                                   job.
        user_email (Optional[UserEmail7])
                                 : The email of the user that owns this job. Only the owner
                                   of the job and administrators can see this value.
        user_id (Optional[UserId]): User ID of user that ran this job
    """

    create_time: datetime  # The time and date this item was created.
    id_: str
    model_class: str  # The name of the database model class.
    params: Params  # Object containing all the parameters of the tool associated with this job. The specific parameters depend on the tool itself.
    state: JobState
    tool_id: str  # Identifier of the tool that generated this job.
    update_time: datetime  # The last time and date this item was updated.
    command_line: CommandLine | None = (
        None  # The command line produced by the job. Users can see this value if allowed in the configuration, administrator can always see this value.
    )
    command_version: CommandVersion | None = None  # Tool version indicated during job execution.
    copied_from_job_id: CopiedFromJobId | None = None  # Reference to cached job if job execution was cached.
    dependencies: Dependencies | None = None  # The dependencies of the job.
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
    inputs: Inputs | None = (
        None  # Dictionary mapping all the tool inputs (by name) to the corresponding data references.
    )
    job_messages: JobMessages | None = None  # List with additional information and possible reasons for a failed job.
    job_metrics: JobMetrics | None = (
        None  # Collections of metrics provided by `JobInstrumenter` plugins on a particular job. Only administrators can see these metrics.
    )
    job_runner_name: JobRunnerName | None = (
        None  # Name of the job runner plugin that handles this job. Only administrator can see this value.
    )
    job_stderr: JobStderr | None = None  # The captured standard error of the job execution.
    job_stdout: JobStdout | None = None  # The captured standard output of the job execution.
    output_collections: ShowFullJobResponseOutputCollections | None = None
    outputs: Outputs | None = (
        None  # Dictionary mapping all the tool outputs (by name) to the corresponding data references.
    )
    stderr: Stderr | None = None  # Combined tool and job standard error streams.
    stdout: Stdout | None = None  # Combined tool and job standard output streams.
    tool_stderr: ToolStderr | None = None  # The captured standard error of the tool executed by the job.
    tool_stdout: ToolStdout | None = None  # The captured standard output of the tool executed by the job.
    user_email: UserEmail7 | None = (
        None  # The email of the user that owns this job. Only the owner of the job and administrators can see this value.
    )
    user_id: UserId | None = None  # User ID of user that ran this job
