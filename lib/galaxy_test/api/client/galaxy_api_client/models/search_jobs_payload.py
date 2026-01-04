from dataclasses import dataclass

from .history_id import HistoryId
from .inputs import Inputs
from .state import State

__all__ = ["SearchJobsPayload"]


@dataclass
class SearchJobsPayload:
    """
    SearchJobsPayload dataclass.

    Args:
        inputs (Inputs)          : The inputs of the job.
        tool_id (str)            : The tool ID related to the job.
        history_id (Optional[HistoryId])
                                 : The encoded ID of the history associated with this item.
        state (Optional[State])  : Current state of the job.
    """

    inputs: Inputs  # The inputs of the job.
    tool_id: str  # The tool ID related to the job.
    history_id: HistoryId | None = None  # The encoded ID of the history associated with this item.
    state: State | None = None  # Current state of the job.
