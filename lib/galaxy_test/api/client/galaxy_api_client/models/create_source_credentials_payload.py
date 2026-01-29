from dataclasses import dataclass

from .service_credential_payload import ServiceCredentialPayload

__all__ = ["CreateSourceCredentialsPayload"]


@dataclass
class CreateSourceCredentialsPayload:
    """
    CreateSourceCredentialsPayload dataclass

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

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "service_credential": "service_credential",
            "source_id": "source_id",
            "source_type": "source_type",
            "source_version": "source_version",
        }
        key_transform_with_dump = {
            "service_credential": "service_credential",
            "source_id": "source_id",
            "source_type": "source_type",
            "source_version": "source_version",
        }
