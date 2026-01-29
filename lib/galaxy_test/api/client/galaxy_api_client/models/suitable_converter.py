from dataclasses import dataclass

__all__ = ["SuitableConverter"]


@dataclass
class SuitableConverter:
    """
    SuitableConverter dataclass

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

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "name": "name",
            "original_type": "original_type",
            "target_type": "target_type",
            "tool_id": "tool_id",
        }
        key_transform_with_dump = {
            "name": "name",
            "original_type": "original_type",
            "target_type": "target_type",
            "tool_id": "tool_id",
        }
