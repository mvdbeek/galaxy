from dataclasses import dataclass
from datetime import datetime

from .encoded_job_details_command_line import EncodedJobDetailsCommandLine
from .encoded_job_details_command_version import EncodedJobDetailsCommandVersion
from .encoded_job_details_copied_from_job_id import EncodedJobDetailsCopiedFromJobId
from .encoded_job_details_exit_code import EncodedJobDetailsExitCode
from .encoded_job_details_external_id import EncodedJobDetailsExternalId
from .encoded_job_details_galaxy_version import EncodedJobDetailsGalaxyVersion
from .encoded_job_details_handler import EncodedJobDetailsHandler
from .encoded_job_details_history_id import EncodedJobDetailsHistoryId
from .encoded_job_details_inputs import EncodedJobDetailsInputs
from .encoded_job_details_job_runner_name import EncodedJobDetailsJobRunnerName
from .encoded_job_details_output_collections import EncodedJobDetailsOutputCollections
from .encoded_job_details_outputs import EncodedJobDetailsOutputs
from .encoded_job_details_params import EncodedJobDetailsParams
from .encoded_job_details_user_email import EncodedJobDetailsUserEmail
from .encoded_job_details_user_id import EncodedJobDetailsUserId
from .job_state import JobState

__all__ = ["EncodedJobDetails"]


@dataclass
class EncodedJobDetails:
    """
    EncodedJobDetails dataclass

    Args:
        create_time (datetime)   : The time and date this item was created.
        id_ (str)                : Maps from 'id'
        model_class (str)        : The name of the database model class.
        params (EncodedJobDetailsParams)
                                 : Object containing all the parameters of the tool
                                   associated with this job. The specific parameters depend
                                   on the tool itself.
        state (JobState)         :
        tool_id (str)            : Identifier of the tool that generated this job.
        update_time (datetime)   : The last time and date this item was updated.
        command_line (EncodedJobDetailsCommandLine | None)
                                 : The command line produced by the job. Users can see this
                                   value if allowed in the configuration, administrator can
                                   always see this value.
        command_version (EncodedJobDetailsCommandVersion | None)
                                 : Tool version indicated during job execution.
        copied_from_job_id (EncodedJobDetailsCopiedFromJobId | None)
                                 : Reference to cached job if job execution was cached.
        exit_code (EncodedJobDetailsExitCode | None)
                                 : The exit code returned by the tool. Can be unset if the
                                   job is not completed yet.
        external_id (EncodedJobDetailsExternalId | None)
                                 : The job id used by the external job runner (Condor,
                                   Pulsar, etc.). Only administrator can see this value.
        galaxy_version (EncodedJobDetailsGalaxyVersion | None)
                                 : The (major) version of Galaxy used to create this job.
        handler (EncodedJobDetailsHandler | None)
                                 : The job handler process assigned to handle this job. Only
                                   administrator can see this value.
        history_id (EncodedJobDetailsHistoryId | None)
                                 : The encoded ID of the history associated with this item.
        inputs (EncodedJobDetailsInputs | None)
                                 : Dictionary mapping all the tool inputs (by name) to the
                                   corresponding data references.
        job_runner_name (EncodedJobDetailsJobRunnerName | None)
                                 : Name of the job runner plugin that handles this job. Only
                                   administrator can see this value.
        output_collections (EncodedJobDetailsOutputCollections | None)
                                 :
        outputs (EncodedJobDetailsOutputs | None)
                                 : Dictionary mapping all the tool outputs (by name) to the
                                   corresponding data references.
        user_email (EncodedJobDetailsUserEmail | None)
                                 : The email of the user that owns this job. Only the owner
                                   of the job and administrators can see this value.
        user_id (EncodedJobDetailsUserId | None)
                                 : User ID of user that ran this job
    """

    create_time: datetime  # The time and date this item was created.
    id_: str  # Maps from 'id'
    model_class: str  # The name of the database model class.
    params: EncodedJobDetailsParams  # Object containing all the parameters of the tool associated with this job. The specific parameters depend on the tool itself.
    state: JobState
    tool_id: str  # Identifier of the tool that generated this job.
    update_time: datetime  # The last time and date this item was updated.
    command_line: EncodedJobDetailsCommandLine | None = (
        None  # The command line produced by the job. Users can see this value if allowed in the configuration, administrator can always see this value.
    )
    command_version: EncodedJobDetailsCommandVersion | None = None  # Tool version indicated during job execution.
    copied_from_job_id: EncodedJobDetailsCopiedFromJobId | None = (
        None  # Reference to cached job if job execution was cached.
    )
    exit_code: EncodedJobDetailsExitCode | None = (
        None  # The exit code returned by the tool. Can be unset if the job is not completed yet.
    )
    external_id: EncodedJobDetailsExternalId | None = (
        None  # The job id used by the external job runner (Condor, Pulsar, etc.). Only administrator can see this value.
    )
    galaxy_version: EncodedJobDetailsGalaxyVersion | None = (
        None  # The (major) version of Galaxy used to create this job.
    )
    handler: EncodedJobDetailsHandler | None = (
        None  # The job handler process assigned to handle this job. Only administrator can see this value.
    )
    history_id: EncodedJobDetailsHistoryId | None = None  # The encoded ID of the history associated with this item.
    inputs: EncodedJobDetailsInputs | None = (
        None  # Dictionary mapping all the tool inputs (by name) to the corresponding data references.
    )
    job_runner_name: EncodedJobDetailsJobRunnerName | None = (
        None  # Name of the job runner plugin that handles this job. Only administrator can see this value.
    )
    output_collections: EncodedJobDetailsOutputCollections | None = None
    outputs: EncodedJobDetailsOutputs | None = (
        None  # Dictionary mapping all the tool outputs (by name) to the corresponding data references.
    )
    user_email: EncodedJobDetailsUserEmail | None = (
        None  # The email of the user that owns this job. Only the owner of the job and administrators can see this value.
    )
    user_id: EncodedJobDetailsUserId | None = None  # User ID of user that ran this job

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "command_line": "command_line",
            "command_version": "command_version",
            "copied_from_job_id": "copied_from_job_id",
            "create_time": "create_time",
            "exit_code": "exit_code",
            "external_id": "external_id",
            "galaxy_version": "galaxy_version",
            "handler": "handler",
            "history_id": "history_id",
            "id": "id_",
            "inputs": "inputs",
            "job_runner_name": "job_runner_name",
            "model_class": "model_class",
            "output_collections": "output_collections",
            "outputs": "outputs",
            "params": "params",
            "state": "state",
            "tool_id": "tool_id",
            "update_time": "update_time",
            "user_email": "user_email",
            "user_id": "user_id",
        }
        key_transform_with_dump = {
            "command_line": "command_line",
            "command_version": "command_version",
            "copied_from_job_id": "copied_from_job_id",
            "create_time": "create_time",
            "exit_code": "exit_code",
            "external_id": "external_id",
            "galaxy_version": "galaxy_version",
            "handler": "handler",
            "history_id": "history_id",
            "id_": "id",
            "inputs": "inputs",
            "job_runner_name": "job_runner_name",
            "model_class": "model_class",
            "output_collections": "output_collections",
            "outputs": "outputs",
            "params": "params",
            "state": "state",
            "tool_id": "tool_id",
            "update_time": "update_time",
            "user_email": "user_email",
            "user_id": "user_id",
        }
