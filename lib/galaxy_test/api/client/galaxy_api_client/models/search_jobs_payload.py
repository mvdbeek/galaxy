from dataclasses import dataclass

from .search_jobs_payload_history_id import SearchJobsPayloadHistoryId
from .search_jobs_payload_inputs import SearchJobsPayloadInputs
from .search_jobs_payload_state import SearchJobsPayloadState

__all__ = ["SearchJobsPayload"]


@dataclass
class SearchJobsPayload:
    """
    SearchJobsPayload dataclass

    Args:
        inputs (SearchJobsPayloadInputs)
                                 : The inputs of the job.
        tool_id (str)            : The tool ID related to the job.
        history_id (SearchJobsPayloadHistoryId | None)
                                 : The encoded ID of the history associated with this job.
        state (SearchJobsPayloadState | None)
                                 : Current state of the job.
    """

    inputs: SearchJobsPayloadInputs  # The inputs of the job.
    tool_id: str  # The tool ID related to the job.
    history_id: SearchJobsPayloadHistoryId | None = None  # The encoded ID of the history associated with this job.
    state: SearchJobsPayloadState | None = None  # Current state of the job.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "history_id": "history_id",
            "inputs": "inputs",
            "state": "state",
            "tool_id": "tool_id",
        }
        key_transform_with_dump = {
            "history_id": "history_id",
            "inputs": "inputs",
            "state": "state",
            "tool_id": "tool_id",
        }
