from dataclasses import dataclass

from .client_secret import ClientSecret
from .data_landing_request_state import DataLandingRequestState
from .origin import Origin

__all__ = ["CreateDataLandingPayload"]


@dataclass
class CreateDataLandingPayload:
    """
    CreateDataLandingPayload dataclass.

    Args:
        request_state (DataLandingRequestState)
                                 :
        client_secret (Optional[ClientSecret])
                                 :
        origin (Optional[Origin]): The origin of the landing request.
        public (Optional[bool])  :
    """

    request_state: DataLandingRequestState
    client_secret: ClientSecret | None = None
    origin: Origin | None = None  # The origin of the landing request.
    public: bool | None = False
