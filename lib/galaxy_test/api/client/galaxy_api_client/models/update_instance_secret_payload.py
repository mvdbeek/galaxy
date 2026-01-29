from dataclasses import dataclass

__all__ = ["UpdateInstanceSecretPayload"]


@dataclass
class UpdateInstanceSecretPayload:
    """
    UpdateInstanceSecretPayload dataclass.

    Args:
        secret_name (str)        :
        secret_value (str)       :
    """

    secret_name: str
    secret_value: str
