from dataclasses import dataclass

__all__ = ["DatatypeConverter"]


@dataclass
class DatatypeConverter:
    """
    DatatypeConverter dataclass

    Args:
        source (str)             : Source type for conversion
        target (str)             : Target type for conversion
        tool_id (str)            : The converter tool identifier
    """

    source: str  # Source type for conversion
    target: str  # Target type for conversion
    tool_id: str  # The converter tool identifier

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "source": "source",
            "target": "target",
            "tool_id": "tool_id",
        }
        key_transform_with_dump = {
            "source": "source",
            "target": "target",
            "tool_id": "tool_id",
        }
