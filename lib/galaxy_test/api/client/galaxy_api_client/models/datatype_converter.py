from dataclasses import dataclass

__all__ = ["DatatypeConverter"]


@dataclass
class DatatypeConverter:
    """
    DatatypeConverter dataclass.

    Args:
        source (str)             : Source type for conversion
        target (str)             : Target type for conversion
        tool_id (str)            : The converter tool identifier
    """

    source: str  # Source type for conversion
    target: str  # Target type for conversion
    tool_id: str  # The converter tool identifier
