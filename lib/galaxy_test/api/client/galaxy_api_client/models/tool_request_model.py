from dataclasses import dataclass

from .request import Request
from .state_message import StateMessage
from .tool_request_state import ToolRequestState

__all__ = ["ToolRequestModel"]


@dataclass
class ToolRequestModel:
    """
    ToolRequestModel dataclass.

    Args:
        id_ (str)                : Encoded ID of the role
        request (Request)        :
        state (ToolRequestState) :
        state_message (Optional[StateMessage])
                                 :
    """

    id_: str  # Encoded ID of the role
    request: Request
    state: ToolRequestState
    state_message: StateMessage | None
