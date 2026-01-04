from dataclasses import dataclass

from .client_secret import ClientSecret
from .origin import Origin
from .request_state import RequestState

__all__ = ["CreateFileLandingPayload"]


@dataclass
class CreateFileLandingPayload:
    """
    CreateFileLandingPayload dataclass.

    Args:
        request_state (RequestState)
                                 :
        client_secret (Optional[ClientSecret])
                                 :
        origin (Optional[Origin]): The origin of the landing request.
        public (Optional[bool])  :
    """

    request_state: RequestState
    client_secret: ClientSecret | None = None
    origin: Origin | None = None  # The origin of the landing request.
    public: bool | None = False
