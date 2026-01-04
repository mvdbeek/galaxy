from dataclasses import dataclass

from .landing_request_state import LandingRequestState
from .origin import Origin
from .request_state import RequestState
from .tool_version import ToolVersion

__all__ = ["ToolLandingRequest"]


@dataclass
class ToolLandingRequest:
    """
    ToolLandingRequest dataclass.

    Args:
        state (LandingRequestState)
                                 :
        tool_id (str)            :
        uuid_ (str)              : Universal unique identifier for this dataset.
        origin (Optional[Origin]): The origin of the landing request.
        request_state (Optional[RequestState])
                                 :
        tool_version (Optional[ToolVersion])
                                 : The version of the tool associated with this step.
    """

    state: LandingRequestState
    tool_id: str
    uuid_: str  # Universal unique identifier for this dataset.
    origin: Origin | None = None  # The origin of the landing request.
    request_state: RequestState | None = None
    tool_version: ToolVersion | None = None  # The version of the tool associated with this step.
