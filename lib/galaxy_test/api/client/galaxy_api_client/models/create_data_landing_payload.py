from dataclasses import dataclass

from .create_data_landing_payload_client_secret import CreateDataLandingPayloadClientSecret
from .create_data_landing_payload_origin import CreateDataLandingPayloadOrigin
from .data_landing_request_state import DataLandingRequestState

__all__ = ["CreateDataLandingPayload"]


@dataclass
class CreateDataLandingPayload:
    """
    CreateDataLandingPayload dataclass

    Args:
        request_state (DataLandingRequestState)
                                 :
        client_secret (CreateDataLandingPayloadClientSecret | None)
                                 :
        origin (CreateDataLandingPayloadOrigin | None)
                                 :
        public (bool | None)     :
    """

    request_state: DataLandingRequestState
    client_secret: CreateDataLandingPayloadClientSecret | None = None
    origin: CreateDataLandingPayloadOrigin | None = None
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
