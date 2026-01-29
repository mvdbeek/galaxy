from dataclasses import dataclass

__all__ = ["UpdateInstanceSecretPayload"]


@dataclass
class UpdateInstanceSecretPayload:
    """
    UpdateInstanceSecretPayload dataclass

    Args:
        secret_name (str)        :
        secret_value (str)       :
    """

    secret_name: str
    secret_value: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "secret_name": "secret_name",
            "secret_value": "secret_value",
        }
        key_transform_with_dump = {
            "secret_name": "secret_name",
            "secret_value": "secret_value",
        }
