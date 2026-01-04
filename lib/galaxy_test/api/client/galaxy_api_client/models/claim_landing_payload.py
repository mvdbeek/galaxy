from dataclasses import dataclass

from .client_secret import ClientSecret

__all__ = ["ClaimLandingPayload"]


@dataclass
class ClaimLandingPayload:
    """
    ClaimLandingPayload dataclass.

    Args:
        client_secret (Optional[ClientSecret])
                                 :
    """

    client_secret: ClientSecret | None = None
