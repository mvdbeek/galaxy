from dataclasses import dataclass

from .tool_request_model_request import ToolRequestModelRequest
from .tool_request_model_state_message import ToolRequestModelStateMessage
from .tool_request_state import ToolRequestState

__all__ = ["ToolRequestModel"]


@dataclass
class ToolRequestModel:
    """
    ToolRequestModel dataclass

    Args:
        id_ (str)                : Encoded ID of the role (maps from 'id')
        request (ToolRequestModelRequest)
                                 :
        state (ToolRequestState) :
        state_message (ToolRequestModelStateMessage)
                                 :
    """

    id_: str  # Encoded ID of the role (maps from 'id')
    request: ToolRequestModelRequest
    state: ToolRequestState
    state_message: ToolRequestModelStateMessage

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "request": "request",
            "state": "state",
            "state_message": "state_message",
        }
        key_transform_with_dump = {
            "id_": "id",
            "request": "request",
            "state": "state",
            "state_message": "state_message",
        }
