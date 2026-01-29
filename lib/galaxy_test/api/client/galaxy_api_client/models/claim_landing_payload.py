from dataclasses import dataclass

from .claim_landing_payload_client_secret import ClaimLandingPayloadClientSecret

__all__ = ["ClaimLandingPayload"]


@dataclass
class ClaimLandingPayload:
    """
    ClaimLandingPayload dataclass

    Args:
        client_secret (ClaimLandingPayloadClientSecret | None)
                                 :
    """

    client_secret: ClaimLandingPayloadClientSecret | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "client_secret": "client_secret",
        }
        key_transform_with_dump = {
            "client_secret": "client_secret",
        }
