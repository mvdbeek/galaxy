from dataclasses import dataclass

from .job_request_history_id import JobRequestHistoryId
from .job_request_inputs import JobRequestInputs
from .job_request_rerun_remap_job_id import JobRequestRerunRemapJobId
from .job_request_tool_id import JobRequestToolId
from .job_request_tool_uuid import JobRequestToolUuid
from .job_request_tool_version import JobRequestToolVersion
from .job_request_use_cached_jobs import JobRequestUseCachedJobs

__all__ = ["JobRequest"]


@dataclass
class JobRequest:
    """
    JobRequest dataclass

    Args:
        history_id (JobRequestHistoryId | None)
                                 : TODO
        inputs (JobRequestInputs | None)
                                 : TODO
        rerun_remap_job_id (JobRequestRerunRemapJobId | None)
                                 : TODO
        send_email_notification (bool | None)
                                 : TODO
        strict (bool | None)     : Turn on strict validation of the inputs that drops
                                   support for some inconsistent legacy behavior.
        tool_id (JobRequestToolId | None)
                                 : TODO
        tool_uuid (JobRequestToolUuid | None)
                                 : TODO
        tool_version (JobRequestToolVersion | None)
                                 : TODO
        use_cached_jobs (JobRequestUseCachedJobs | None)
                                 :
    """

    history_id: JobRequestHistoryId | None = None  # TODO
    inputs: JobRequestInputs | None = None  # TODO
    rerun_remap_job_id: JobRequestRerunRemapJobId | None = None  # TODO
    send_email_notification: bool | None = False  # TODO
    strict: bool | None = (
        True  # Turn on strict validation of the inputs that drops support for some inconsistent legacy behavior.
    )
    tool_id: JobRequestToolId | None = None  # TODO
    tool_uuid: JobRequestToolUuid | None = None  # TODO
    tool_version: JobRequestToolVersion | None = None  # TODO
    use_cached_jobs: JobRequestUseCachedJobs | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "history_id": "history_id",
            "inputs": "inputs",
            "rerun_remap_job_id": "rerun_remap_job_id",
            "send_email_notification": "send_email_notification",
            "strict": "strict",
            "tool_id": "tool_id",
            "tool_uuid": "tool_uuid",
            "tool_version": "tool_version",
            "use_cached_jobs": "use_cached_jobs",
        }
        key_transform_with_dump = {
            "history_id": "history_id",
            "inputs": "inputs",
            "rerun_remap_job_id": "rerun_remap_job_id",
            "send_email_notification": "send_email_notification",
            "strict": "strict",
            "tool_id": "tool_id",
            "tool_uuid": "tool_uuid",
            "tool_version": "tool_version",
            "use_cached_jobs": "use_cached_jobs",
        }
