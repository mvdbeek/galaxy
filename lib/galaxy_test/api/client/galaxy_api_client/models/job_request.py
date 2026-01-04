from dataclasses import dataclass

from .history_id import HistoryId
from .inputs import Inputs
from .rerun_remap_job_id import RerunRemapJobId
from .tool_id import ToolId
from .tool_uuid import ToolUuid
from .tool_version import ToolVersion
from .use_cached_jobs import UseCachedJobs

__all__ = ["JobRequest"]


@dataclass
class JobRequest:
    """
    JobRequest dataclass.

    Args:
        history_id (Optional[HistoryId])
                                 : The encoded ID of the history associated with this item.
        inputs (Optional[Inputs]): TODO
        rerun_remap_job_id (Optional[RerunRemapJobId])
                                 : TODO
        send_email_notification (Optional[bool])
                                 : TODO
        strict (Optional[bool])  : Turn on strict validation of the inputs that drops
                                   support for some inconsistent legacy behavior.
        tool_id (Optional[ToolId]): The unique name of the tool associated with this step.
        tool_uuid (Optional[ToolUuid])
                                 : The universal unique identifier of the tool associated
                                   with this step. Takes precedence over tool_id if set.
        tool_version (Optional[ToolVersion])
                                 : The version of the tool associated with this step.
        use_cached_jobs (Optional[UseCachedJobs])
                                 :
    """

    history_id: HistoryId | None = None  # The encoded ID of the history associated with this item.
    inputs: Inputs | None = None  # TODO
    rerun_remap_job_id: RerunRemapJobId | None = None  # TODO
    send_email_notification: bool | None = False  # TODO
    strict: bool | None = (
        True  # Turn on strict validation of the inputs that drops support for some inconsistent legacy behavior.
    )
    tool_id: ToolId | None = None  # The unique name of the tool associated with this step.
    tool_uuid: ToolUuid | None = (
        None  # The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.
    )
    tool_version: ToolVersion | None = None  # The version of the tool associated with this step.
    use_cached_jobs: UseCachedJobs | None = None
