from dataclasses import dataclass

from .create_file_landing_payload_client_secret import CreateFileLandingPayloadClientSecret
from .create_file_landing_payload_origin import CreateFileLandingPayloadOrigin
from .create_file_landing_payload_request_state import CreateFileLandingPayloadRequestState

__all__ = ["CreateFileLandingPayload"]


@dataclass
class CreateFileLandingPayload:
    """
    CreateFileLandingPayload dataclass

    Args:
        request_state (CreateFileLandingPayloadRequestState)
                                 :
        client_secret (CreateFileLandingPayloadClientSecret | None)
                                 :
        origin (CreateFileLandingPayloadOrigin | None)
                                 :
        public (bool | None)     :
    """

    request_state: CreateFileLandingPayloadRequestState
    client_secret: CreateFileLandingPayloadClientSecret | None = None
    origin: CreateFileLandingPayloadOrigin | None = None
    public: bool | None = False

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "client_secret": "client_secret",
            "origin": "origin",
            "public": "public",
            "request_state": "request_state",
        }
        key_transform_with_dump = {
            "client_secret": "client_secret",
            "origin": "origin",
            "public": "public",
            "request_state": "request_state",
        }
