from dataclasses import dataclass

__all__ = ["SecretResponse"]


@dataclass
class SecretResponse:
    """
    SecretResponse dataclass.

    Args:
        is_set (bool)            : Whether the secret has been set (value is not exposed).
        name (str)               : The name of the credential.
    """

    is_set: bool  # Whether the secret has been set (value is not exposed).
    name: str  # The name of the credential.
