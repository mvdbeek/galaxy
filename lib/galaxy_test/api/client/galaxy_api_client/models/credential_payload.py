from dataclasses import dataclass

from .value import Value

__all__ = ["CredentialPayload"]


@dataclass
class CredentialPayload:
    """
    CredentialPayload dataclass.

    Args:
        name (str)               : The name of the credential (variable or secret).
        value (Optional[Value])  : TODO
    """

    name: str  # The name of the credential (variable or secret).
    value: Value | None = False  # TODO
