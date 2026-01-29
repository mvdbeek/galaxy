from dataclasses import dataclass

from .service_credential_group_payload import ServiceCredentialGroupPayload

__all__ = ["ServiceCredentialPayload"]


@dataclass
class ServiceCredentialPayload:
    """
    ServiceCredentialPayload dataclass

    Args:
        group (ServiceCredentialGroupPayload)
                                 :
        name (str)               : The name of the service requiring credentials.
        version (str)            : The version of the service.
    """

    group: ServiceCredentialGroupPayload
    name: str  # The name of the service requiring credentials.
    version: str  # The version of the service.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "group": "group",
            "name": "name",
            "version": "version",
        }
        key_transform_with_dump = {
            "group": "group",
            "name": "name",
            "version": "version",
        }
