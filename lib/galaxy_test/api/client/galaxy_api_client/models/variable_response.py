from dataclasses import dataclass

from .variable_response_value import VariableResponseValue

__all__ = ["VariableResponse"]


@dataclass
class VariableResponse:
    """
    VariableResponse dataclass

    Args:
        name (str)               : The name of the credential.
        value (VariableResponseValue | None)
                                 : The value of the variable (for variables, not secrets).
    """

    name: str  # The name of the credential.
    value: VariableResponseValue | None = None  # The value of the variable (for variables, not secrets).

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
