from dataclasses import dataclass

from .credential_payload import CredentialPayload

__all__ = ["ServiceCredentialGroupPayload"]


@dataclass
class ServiceCredentialGroupPayload:
    """
    ServiceCredentialGroupPayload dataclass.

    Args:
        name (str)               : The name of the credential group (minimum 3 characters).
        secrets (List[CredentialPayload])
                                 : List of secrets for this credential group.
        variables (List[CredentialPayload])
                                 : List of variables for this credential group.
    """

    name: str  # The name of the credential group (minimum 3 characters).
    secrets: list[CredentialPayload]  # List of secrets for this credential group.
    variables: list[CredentialPayload]  # List of variables for this credential group.
