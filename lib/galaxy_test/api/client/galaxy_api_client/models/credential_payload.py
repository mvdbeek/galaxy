from dataclasses import dataclass

from .credential_payload_value import CredentialPayloadValue

__all__ = ["CredentialPayload"]


@dataclass
class CredentialPayload:
    """
    CredentialPayload dataclass

    Args:
        name (str)               : The name of the credential (variable or secret).
        value (CredentialPayloadValue | None)
                                 : The value of the credential.
    """

    name: str  # The name of the credential (variable or secret).
    value: CredentialPayloadValue | None = None  # The value of the credential.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "name": "name",
            "value": "value",
        }
        key_transform_with_dump = {
            "name": "name",
            "value": "value",
        }
