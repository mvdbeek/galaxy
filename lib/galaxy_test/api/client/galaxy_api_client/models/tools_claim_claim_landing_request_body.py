from typing import TypeAlias

from .claim_landing_payload import ClaimLandingPayload

__all__ = ["ToolsClaimClaimLandingRequestBody"]

ToolsClaimClaimLandingRequestBody: TypeAlias = ClaimLandingPayload | None
