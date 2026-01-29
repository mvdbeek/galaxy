from dataclasses import dataclass

from .landing_request_state import LandingRequestState
from .tool_landing_request_origin import ToolLandingRequestOrigin
from .tool_landing_request_request_state import ToolLandingRequestRequestState
from .tool_landing_request_tool_version import ToolLandingRequestToolVersion

__all__ = ["ToolLandingRequest"]


@dataclass
class ToolLandingRequest:
    """
    ToolLandingRequest dataclass

    Args:
        state (LandingRequestState)
                                 :
        tool_id (str)            :
        uuid_ (str)              : Universal unique identifier for this dataset. (maps from
                                   'uuid')
        origin (ToolLandingRequestOrigin | None)
                                 :
        request_state (ToolLandingRequestRequestState | None)
                                 :
        tool_version (ToolLandingRequestToolVersion | None)
                                 :
    """

    state: LandingRequestState
    tool_id: str
    uuid_: str  # Universal unique identifier for this dataset. (maps from 'uuid')
    origin: ToolLandingRequestOrigin | None = None
    request_state: ToolLandingRequestRequestState | None = None
    tool_version: ToolLandingRequestToolVersion | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "origin": "origin",
            "request_state": "request_state",
            "state": "state",
            "tool_id": "tool_id",
            "tool_version": "tool_version",
            "uuid": "uuid_",
        }
        key_transform_with_dump = {
            "origin": "origin",
            "request_state": "request_state",
            "state": "state",
            "tool_id": "tool_id",
            "tool_version": "tool_version",
            "uuid_": "uuid",
        }
