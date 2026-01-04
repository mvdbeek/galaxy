from dataclasses import dataclass

from .service_credential_payload import ServiceCredentialPayload

__all__ = ["CreateSourceCredentialsPayload"]


@dataclass
class CreateSourceCredentialsPayload:
    """
    CreateSourceCredentialsPayload dataclass.

    Args:
        service_credential (ServiceCredentialPayload)
                                 :
        source_id (str)          : The ID of the source (e.g., tool ID).
        source_type (str)        : The type of source requiring credentials.
        source_version (str)     : The version of the source.
    """

    service_credential: ServiceCredentialPayload
    source_id: str  # The ID of the source (e.g., tool ID).
    source_type: str  # The type of source requiring credentials.
    source_version: str  # The version of the source.
