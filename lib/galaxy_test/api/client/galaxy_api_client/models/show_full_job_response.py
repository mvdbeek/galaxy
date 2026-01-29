from dataclasses import dataclass
from datetime import datetime

from .job_state import JobState
from .show_full_job_response_command_line import ShowFullJobResponseCommandLine
from .show_full_job_response_command_version import ShowFullJobResponseCommandVersion
from .show_full_job_response_copied_from_job_id import ShowFullJobResponseCopiedFromJobId
from .show_full_job_response_dependencies import ShowFullJobResponseDependencies
from .show_full_job_response_exit_code import ShowFullJobResponseExitCode
from .show_full_job_response_external_id import ShowFullJobResponseExternalId
from .show_full_job_response_galaxy_version import ShowFullJobResponseGalaxyVersion
from .show_full_job_response_handler import ShowFullJobResponseHandler
from .show_full_job_response_history_id import ShowFullJobResponseHistoryId
from .show_full_job_response_inputs import ShowFullJobResponseInputs
from .show_full_job_response_job_messages import ShowFullJobResponseJobMessages
from .show_full_job_response_job_metrics import ShowFullJobResponseJobMetrics
from .show_full_job_response_job_runner_name import ShowFullJobResponseJobRunnerName
from .show_full_job_response_job_stderr import ShowFullJobResponseJobStderr
from .show_full_job_response_job_stdout import ShowFullJobResponseJobStdout
from .show_full_job_response_output_collections import ShowFullJobResponseOutputCollections
from .show_full_job_response_outputs import ShowFullJobResponseOutputs
from .show_full_job_response_params import ShowFullJobResponseParams
from .show_full_job_response_stderr import ShowFullJobResponseStderr
from .show_full_job_response_stdout import ShowFullJobResponseStdout
from .show_full_job_response_tool_stderr import ShowFullJobResponseToolStderr
from .show_full_job_response_tool_stdout import ShowFullJobResponseToolStdout
from .show_full_job_response_user_email import ShowFullJobResponseUserEmail
from .show_full_job_response_user_id import ShowFullJobResponseUserId

__all__ = ["ShowFullJobResponse"]


@dataclass
class ShowFullJobResponse:
    """
    ShowFullJobResponse dataclass

    Args:
        create_time (datetime)   : The time and date this item was created.
        id_ (str)                : Maps from 'id'
        model_class (str)        : The name of the database model class.
        params (ShowFullJobResponseParams)
                                 : Object containing all the parameters of the tool
                                   associated with this job. The specific parameters depend
                                   on the tool itself.
        state (JobState)         :
        tool_id (str)            : Identifier of the tool that generated this job.
        update_time (datetime)   : The last time and date this item was updated.
        command_line (ShowFullJobResponseCommandLine | None)
                                 : The command line produced by the job. Users can see this
                                   value if allowed in the configuration, administrator can
                                   always see this value.
        command_version (ShowFullJobResponseCommandVersion | None)
                                 : Tool version indicated during job execution.
        copied_from_job_id (ShowFullJobResponseCopiedFromJobId | None)
                                 : Reference to cached job if job execution was cached.
        dependencies (ShowFullJobResponseDependencies | None)
                                 : The dependencies of the job.
        exit_code (ShowFullJobResponseExitCode | None)
                                 : The exit code returned by the tool. Can be unset if the
                                   job is not completed yet.
        external_id (ShowFullJobResponseExternalId | None)
                                 : The job id used by the external job runner (Condor,
                                   Pulsar, etc.). Only administrator can see this value.
        galaxy_version (ShowFullJobResponseGalaxyVersion | None)
                                 : The (major) version of Galaxy used to create this job.
        handler (ShowFullJobResponseHandler | None)
                                 : The job handler process assigned to handle this job. Only
                                   administrator can see this value.
        history_id (ShowFullJobResponseHistoryId | None)
                                 : The encoded ID of the history associated with this item.
        inputs (ShowFullJobResponseInputs | None)
                                 : Dictionary mapping all the tool inputs (by name) to the
                                   corresponding data references.
        job_messages (ShowFullJobResponseJobMessages | None)
                                 : List with additional information and possible reasons for
                                   a failed job.
        job_metrics (ShowFullJobResponseJobMetrics | None)
                                 : Collections of metrics provided by `JobInstrumenter`
                                   plugins on a particular job. Only administrators can see
                                   these metrics.
        job_runner_name (ShowFullJobResponseJobRunnerName | None)
                                 : Name of the job runner plugin that handles this job. Only
                                   administrator can see this value.
        job_stderr (ShowFullJobResponseJobStderr | None)
                                 : The captured standard error of the job execution.
        job_stdout (ShowFullJobResponseJobStdout | None)
                                 : The captured standard output of the job execution.
        output_collections (ShowFullJobResponseOutputCollections | None)
                                 :
        outputs (ShowFullJobResponseOutputs | None)
                                 : Dictionary mapping all the tool outputs (by name) to the
                                   corresponding data references.
        stderr (ShowFullJobResponseStderr | None)
                                 : Combined tool and job standard error streams.
        stdout (ShowFullJobResponseStdout | None)
                                 : Combined tool and job standard output streams.
        tool_stderr (ShowFullJobResponseToolStderr | None)
                                 : The captured standard error of the tool executed by the
                                   job.
        tool_stdout (ShowFullJobResponseToolStdout | None)
                                 : The captured standard output of the tool executed by the
                                   job.
        user_email (ShowFullJobResponseUserEmail | None)
                                 : The email of the user that owns this job. Only the owner
                                   of the job and administrators can see this value.
        user_id (ShowFullJobResponseUserId | None)
                                 : User ID of user that ran this job
    """

    create_time: datetime  # The time and date this item was created.
    id_: str  # Maps from 'id'
    model_class: str  # The name of the database model class.
    params: ShowFullJobResponseParams  # Object containing all the parameters of the tool associated with this job. The specific parameters depend on the tool itself.
    state: JobState
    tool_id: str  # Identifier of the tool that generated this job.
    update_time: datetime  # The last time and date this item was updated.
    command_line: ShowFullJobResponseCommandLine | None = (
        None  # The command line produced by the job. Users can see this value if allowed in the configuration, administrator can always see this value.
    )
    command_version: ShowFullJobResponseCommandVersion | None = None  # Tool version indicated during job execution.
    copied_from_job_id: ShowFullJobResponseCopiedFromJobId | None = (
        None  # Reference to cached job if job execution was cached.
    )
    dependencies: ShowFullJobResponseDependencies | None = None  # The dependencies of the job.
    exit_code: ShowFullJobResponseExitCode | None = (
        None  # The exit code returned by the tool. Can be unset if the job is not completed yet.
    )
    external_id: ShowFullJobResponseExternalId | None = (
        None  # The job id used by the external job runner (Condor, Pulsar, etc.). Only administrator can see this value.
    )
    galaxy_version: ShowFullJobResponseGalaxyVersion | None = (
        None  # The (major) version of Galaxy used to create this job.
    )
    handler: ShowFullJobResponseHandler | None = (
        None  # The job handler process assigned to handle this job. Only administrator can see this value.
    )
    history_id: ShowFullJobResponseHistoryId | None = None  # The encoded ID of the history associated with this item.
    inputs: ShowFullJobResponseInputs | None = (
        None  # Dictionary mapping all the tool inputs (by name) to the corresponding data references.
    )
    job_messages: ShowFullJobResponseJobMessages | None = (
        None  # List with additional information and possible reasons for a failed job.
    )
    job_metrics: ShowFullJobResponseJobMetrics | None = (
        None  # Collections of metrics provided by `JobInstrumenter` plugins on a particular job. Only administrators can see these metrics.
    )
    job_runner_name: ShowFullJobResponseJobRunnerName | None = (
        None  # Name of the job runner plugin that handles this job. Only administrator can see this value.
    )
    job_stderr: ShowFullJobResponseJobStderr | None = None  # The captured standard error of the job execution.
    job_stdout: ShowFullJobResponseJobStdout | None = None  # The captured standard output of the job execution.
    output_collections: ShowFullJobResponseOutputCollections | None = None
    outputs: ShowFullJobResponseOutputs | None = (
        None  # Dictionary mapping all the tool outputs (by name) to the corresponding data references.
    )
    stderr: ShowFullJobResponseStderr | None = None  # Combined tool and job standard error streams.
    stdout: ShowFullJobResponseStdout | None = None  # Combined tool and job standard output streams.
    tool_stderr: ShowFullJobResponseToolStderr | None = (
        None  # The captured standard error of the tool executed by the job.
    )
    tool_stdout: ShowFullJobResponseToolStdout | None = (
        None  # The captured standard output of the tool executed by the job.
    )
    user_email: ShowFullJobResponseUserEmail | None = (
        None  # The email of the user that owns this job. Only the owner of the job and administrators can see this value.
    )
    user_id: ShowFullJobResponseUserId | None = None  # User ID of user that ran this job

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "command_line": "command_line",
            "command_version": "command_version",
            "copied_from_job_id": "copied_from_job_id",
            "create_time": "create_time",
            "dependencies": "dependencies",
            "exit_code": "exit_code",
            "external_id": "external_id",
            "galaxy_version": "galaxy_version",
            "handler": "handler",
            "history_id": "history_id",
            "id": "id_",
            "inputs": "inputs",
            "job_messages": "job_messages",
            "job_metrics": "job_metrics",
            "job_runner_name": "job_runner_name",
            "job_stderr": "job_stderr",
            "job_stdout": "job_stdout",
            "model_class": "model_class",
            "output_collections": "output_collections",
            "outputs": "outputs",
            "params": "params",
            "state": "state",
            "stderr": "stderr",
            "stdout": "stdout",
            "tool_id": "tool_id",
            "tool_stderr": "tool_stderr",
            "tool_stdout": "tool_stdout",
            "update_time": "update_time",
            "user_email": "user_email",
            "user_id": "user_id",
        }
        key_transform_with_dump = {
            "command_line": "command_line",
            "command_version": "command_version",
            "copied_from_job_id": "copied_from_job_id",
            "create_time": "create_time",
            "dependencies": "dependencies",
            "exit_code": "exit_code",
            "external_id": "external_id",
            "galaxy_version": "galaxy_version",
            "handler": "handler",
            "history_id": "history_id",
            "id_": "id",
            "inputs": "inputs",
            "job_messages": "job_messages",
            "job_metrics": "job_metrics",
            "job_runner_name": "job_runner_name",
            "job_stderr": "job_stderr",
            "job_stdout": "job_stdout",
            "model_class": "model_class",
            "output_collections": "output_collections",
            "outputs": "outputs",
            "params": "params",
            "state": "state",
            "stderr": "stderr",
            "stdout": "stdout",
            "tool_id": "tool_id",
            "tool_stderr": "tool_stderr",
            "tool_stdout": "tool_stdout",
            "update_time": "update_time",
            "user_email": "user_email",
            "user_id": "user_id",
        }
