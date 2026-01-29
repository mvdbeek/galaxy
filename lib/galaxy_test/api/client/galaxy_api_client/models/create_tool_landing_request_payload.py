from dataclasses import dataclass

from .create_tool_landing_request_payload_client_secret import CreateToolLandingRequestPayloadClientSecret
from .create_tool_landing_request_payload_origin import CreateToolLandingRequestPayloadOrigin
from .create_tool_landing_request_payload_request_state import CreateToolLandingRequestPayloadRequestState
from .create_tool_landing_request_payload_tool_version import CreateToolLandingRequestPayloadToolVersion

__all__ = ["CreateToolLandingRequestPayload"]


@dataclass
class CreateToolLandingRequestPayload:
    """
    CreateToolLandingRequestPayload dataclass

    Args:
        tool_id (str)            :
        client_secret (CreateToolLandingRequestPayloadClientSecret | None)
                                 :
        origin (CreateToolLandingRequestPayloadOrigin | None)
                                 : The origin of the landing request.
        public (bool | None)     :
        request_state (CreateToolLandingRequestPayloadRequestState | None)
                                 :
        tool_version (CreateToolLandingRequestPayloadToolVersion | None)
                                 :
    """

    tool_id: str
    client_secret: CreateToolLandingRequestPayloadClientSecret | None = None
    origin: CreateToolLandingRequestPayloadOrigin | None = None  # The origin of the landing request.
    public: bool | None = False
    request_state: CreateToolLandingRequestPayloadRequestState | None = None
    tool_version: CreateToolLandingRequestPayloadToolVersion | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "client_secret": "client_secret",
            "origin": "origin",
            "public": "public",
            "request_state": "request_state",
            "tool_id": "tool_id",
            "tool_version": "tool_version",
        }
        key_transform_with_dump = {
            "client_secret": "client_secret",
            "origin": "origin",
            "public": "public",
            "request_state": "request_state",
            "tool_id": "tool_id",
            "tool_version": "tool_version",
        }
