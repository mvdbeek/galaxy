from dataclasses import dataclass

__all__ = ["SuitableConverter"]


@dataclass
class SuitableConverter:
    """
    SuitableConverter dataclass.

    Args:
        name (str)               : The name of the converter.
        original_type (str)      : The type to convert from.
        target_type (str)        : The type to convert to.
        tool_id (str)            : The ID of the tool that can perform the type conversion.
    """

    name: str  # The name of the converter.
    original_type: str  # The type to convert from.
    target_type: str  # The type to convert to.
    tool_id: str  # The ID of the tool that can perform the type conversion.
