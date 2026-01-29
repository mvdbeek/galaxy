from dataclasses import dataclass
from datetime import datetime

from .job_import_history_response_exit_code import JobImportHistoryResponseExitCode
from .job_import_history_response_galaxy_version import JobImportHistoryResponseGalaxyVersion
from .job_import_history_response_history_id import JobImportHistoryResponseHistoryId
from .job_state import JobState

__all__ = ["JobImportHistoryResponse"]


@dataclass
class JobImportHistoryResponse:
    """
    JobImportHistoryResponse dataclass

    Args:
        create_time (datetime)   : The time and date this item was created.
        id_ (str)                : Maps from 'id'
        message (str)            : Text message containing information about the history
                                   import.
        model_class (str)        : The name of the database model class.
        state (JobState)         :
        tool_id (str)            : Identifier of the tool that generated this job.
        update_time (datetime)   : The last time and date this item was updated.
        exit_code (JobImportHistoryResponseExitCode | None)
                                 : The exit code returned by the tool. Can be unset if the
                                   job is not completed yet.
        galaxy_version (JobImportHistoryResponseGalaxyVersion | None)
                                 : The (major) version of Galaxy used to create this job.
        history_id (JobImportHistoryResponseHistoryId | None)
                                 : The encoded ID of the history associated with this item.
    """

    create_time: datetime  # The time and date this item was created.
    id_: str  # Maps from 'id'
    message: str  # Text message containing information about the history import.
    model_class: str  # The name of the database model class.
    state: JobState
    tool_id: str  # Identifier of the tool that generated this job.
    update_time: datetime  # The last time and date this item was updated.
    exit_code: JobImportHistoryResponseExitCode | None = (
        None  # The exit code returned by the tool. Can be unset if the job is not completed yet.
    )
    galaxy_version: JobImportHistoryResponseGalaxyVersion | None = (
        None  # The (major) version of Galaxy used to create this job.
    )
    history_id: JobImportHistoryResponseHistoryId | None = (
        None  # The encoded ID of the history associated with this item.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "create_time": "create_time",
            "exit_code": "exit_code",
            "galaxy_version": "galaxy_version",
            "history_id": "history_id",
            "id": "id_",
            "message": "message",
            "model_class": "model_class",
            "state": "state",
            "tool_id": "tool_id",
            "update_time": "update_time",
        }
        key_transform_with_dump = {
            "create_time": "create_time",
            "exit_code": "exit_code",
            "galaxy_version": "galaxy_version",
            "history_id": "history_id",
            "id_": "id",
            "message": "message",
            "model_class": "model_class",
            "state": "state",
            "tool_id": "tool_id",
            "update_time": "update_time",
        }
