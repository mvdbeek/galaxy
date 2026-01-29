from dataclasses import dataclass
from datetime import datetime

from .job_base_model_exit_code import JobBaseModelExitCode
from .job_base_model_galaxy_version import JobBaseModelGalaxyVersion
from .job_base_model_history_id import JobBaseModelHistoryId
from .job_state import JobState

__all__ = ["JobBaseModel"]


@dataclass
class JobBaseModel:
    """
    JobBaseModel dataclass

    Args:
        create_time (datetime)   : The time and date this item was created.
        id_ (str)                : Maps from 'id'
        model_class (str)        : The name of the database model class.
        state (JobState)         :
        tool_id (str)            : Identifier of the tool that generated this job.
        update_time (datetime)   : The last time and date this item was updated.
        exit_code (JobBaseModelExitCode | None)
                                 : The exit code returned by the tool. Can be unset if the
                                   job is not completed yet.
        galaxy_version (JobBaseModelGalaxyVersion | None)
                                 : The (major) version of Galaxy used to create this job.
        history_id (JobBaseModelHistoryId | None)
                                 : The encoded ID of the history associated with this item.
    """

    create_time: datetime  # The time and date this item was created.
    id_: str  # Maps from 'id'
    model_class: str  # The name of the database model class.
    state: JobState
    tool_id: str  # Identifier of the tool that generated this job.
    update_time: datetime  # The last time and date this item was updated.
    exit_code: JobBaseModelExitCode | None = (
        None  # The exit code returned by the tool. Can be unset if the job is not completed yet.
    )
    galaxy_version: JobBaseModelGalaxyVersion | None = None  # The (major) version of Galaxy used to create this job.
    history_id: JobBaseModelHistoryId | None = None  # The encoded ID of the history associated with this item.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "create_time": "create_time",
            "exit_code": "exit_code",
            "galaxy_version": "galaxy_version",
            "history_id": "history_id",
            "id": "id_",
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
            "model_class": "model_class",
            "state": "state",
            "tool_id": "tool_id",
            "update_time": "update_time",
        }
