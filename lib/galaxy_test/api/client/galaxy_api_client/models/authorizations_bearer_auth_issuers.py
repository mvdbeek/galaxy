from typing import TypeAlias

__all__ = ["AuthorizationsBearerAuthIssuers"]

AuthorizationsBearerAuthIssuers: TypeAlias = list[str] | None
"""Alias for If authorizations contain `BearerAuth` this is an optional list of issuers that may authorize access to this object. The caller must provide a token from one of these issuers. If this is empty or missing it assumed the caller knows which token to send via other means. It is strongly recommended that the caller validate that it is appropriate to send the requested token to the DRS server to mitigate attacks by malicious DRS servers requesting credentials they should not have."""
