from dataclasses import dataclass
from datetime import datetime

from .exit_code import ExitCode
from .galaxy_version import GalaxyVersion
from .history_id import HistoryId
from .job_state import JobState

__all__ = ["JobImportHistoryResponse"]


@dataclass
class JobImportHistoryResponse:
    """
    JobImportHistoryResponse dataclass.

    Args:
        create_time (datetime)   : The time and date this item was created.
        id_ (str)                :
        message (str)            : Text message containing information about the history
                                   import.
        model_class (str)        : The name of the database model class.
        state (JobState)         :
        tool_id (str)            : Identifier of the tool that generated this job.
        update_time (datetime)   : The last time and date this item was updated.
        exit_code (Optional[ExitCode])
                                 : The exit code returned by the tool. Can be unset if the
                                   job is not completed yet.
        galaxy_version (Optional[GalaxyVersion])
                                 : The (major) version of Galaxy used to create this job.
        history_id (Optional[HistoryId])
                                 : The encoded ID of the history associated with this item.
    """

    create_time: datetime  # The time and date this item was created.
    id_: str
    message: str  # Text message containing information about the history import.
    model_class: str  # The name of the database model class.
    state: JobState
    tool_id: str  # Identifier of the tool that generated this job.
    update_time: datetime  # The last time and date this item was updated.
    exit_code: ExitCode | None = (
        None  # The exit code returned by the tool. Can be unset if the job is not completed yet.
    )
    galaxy_version: GalaxyVersion | None = None  # The (major) version of Galaxy used to create this job.
    history_id: HistoryId | None = None  # The encoded ID of the history associated with this item.
