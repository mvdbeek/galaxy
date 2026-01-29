from typing import TypeAlias

__all__ = ["AuthorizationsPassportAuthIssuers"]

AuthorizationsPassportAuthIssuers: TypeAlias = list[str] | None
"""Alias for If authorizations contain `PassportAuth` this is a required list of visa issuers (as found in a visa's `iss` claim) that may authorize access to this object. The caller must only provide passports that contain visas from this list. It is strongly recommended that the caller validate that it is appropriate to send the requested passport/visa to the DRS server to mitigate attacks by malicious DRS servers requesting credentials they should not have."""
