from dataclasses import dataclass

from .authorizations_bearer_auth_issuers import AuthorizationsBearerAuthIssuers
from .authorizations_passport_auth_issuers import AuthorizationsPassportAuthIssuers
from .authorizations_supported_types import AuthorizationsSupportedTypes

__all__ = ["Authorizations"]


@dataclass
class Authorizations:
    """
    Authorizations dataclass

    Args:
        bearer_auth_issuers (AuthorizationsBearerAuthIssuers | None)
                                 : If authorizations contain `BearerAuth` this is an
                                   optional list of issuers that may authorize access to
                                   this object. The caller must provide a token from one of
                                   these issuers. If this is empty or missing it assumed the
                                   caller knows which token to send via other means. It is
                                   strongly recommended that the caller validate that it is
                                   appropriate to send the requested token to the DRS server
                                   to mitigate attacks by malicious DRS servers requesting
                                   credentials they should not have.
        passport_auth_issuers (AuthorizationsPassportAuthIssuers | None)
                                 : If authorizations contain `PassportAuth` this is a
                                   required list of visa issuers (as found in a visa's `iss`
                                   claim) that may authorize access to this object. The
                                   caller must only provide passports that contain visas
                                   from this list. It is strongly recommended that the
                                   caller validate that it is appropriate to send the
                                   requested passport/visa to the DRS server to mitigate
                                   attacks by malicious DRS servers requesting credentials
                                   they should not have.
        supported_types (AuthorizationsSupportedTypes | None)
                                 : An Optional list of support authorization types. More
                                   than one can be supported and tried in sequence. Defaults
                                   to `None` if empty or missing.
    """

    bearer_auth_issuers: AuthorizationsBearerAuthIssuers | None = (
        None  # If authorizations contain `BearerAuth` this is an optional list of issuers that may authorize access to this object. The caller must provide a token from one of these issuers. If this is empty or missing it assumed the caller knows which token to send via other means. It is strongly recommended that the caller validate that it is appropriate to send the requested token to the DRS server to mitigate attacks by malicious DRS servers requesting credentials they should not have.
    )
    passport_auth_issuers: AuthorizationsPassportAuthIssuers | None = (
        None  # If authorizations contain `PassportAuth` this is a required list of visa issuers (as found in a visa's `iss` claim) that may authorize access to this object. The caller must only provide passports that contain visas from this list. It is strongly recommended that the caller validate that it is appropriate to send the requested passport/visa to the DRS server to mitigate attacks by malicious DRS servers requesting credentials they should not have.
    )
    supported_types: AuthorizationsSupportedTypes | None = (
        None  # An Optional list of support authorization types. More than one can be supported and tried in sequence. Defaults to `None` if empty or missing.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "bearer_auth_issuers": "bearer_auth_issuers",
            "passport_auth_issuers": "passport_auth_issuers",
            "supported_types": "supported_types",
        }
        key_transform_with_dump = {
            "bearer_auth_issuers": "bearer_auth_issuers",
            "passport_auth_issuers": "passport_auth_issuers",
            "supported_types": "supported_types",
        }
