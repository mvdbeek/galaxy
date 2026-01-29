from dataclasses import dataclass

from .value import Value

__all__ = ["VariableResponse"]


@dataclass
class VariableResponse:
    """
    VariableResponse dataclass.

    Args:
        name (str)               : The name of the credential.
        value (Optional[Value])  : TODO
    """

    name: str  # The name of the credential.
    value: Value | None = False  # TODO
