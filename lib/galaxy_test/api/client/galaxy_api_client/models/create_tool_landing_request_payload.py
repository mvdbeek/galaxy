from dataclasses import dataclass

from .client_secret import ClientSecret
from .origin import Origin
from .request_state import RequestState
from .tool_version import ToolVersion

__all__ = ["CreateToolLandingRequestPayload"]


@dataclass
class CreateToolLandingRequestPayload:
    """
    CreateToolLandingRequestPayload dataclass.

    Args:
        tool_id (str)            :
        client_secret (Optional[ClientSecret])
                                 :
        origin (Optional[Origin]): The origin of the landing request.
        public (Optional[bool])  :
        request_state (Optional[RequestState])
                                 :
        tool_version (Optional[ToolVersion])
                                 : The version of the tool associated with this step.
    """

    tool_id: str
    client_secret: ClientSecret | None = None
    origin: Origin | None = None  # The origin of the landing request.
    public: bool | None = False
    request_state: RequestState | None = None
    tool_version: ToolVersion | None = None  # The version of the tool associated with this step.
