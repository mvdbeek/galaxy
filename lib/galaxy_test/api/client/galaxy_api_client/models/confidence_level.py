from enum import Enum, unique

__all__ = ["ConfidenceLevel"]


@unique
class ConfidenceLevel(str, Enum):
    """
    Confidence levels for agent responses.

    Args:
        low (str)                : Value for LOW
        medium (str)             : Value for MEDIUM
        high (str)               : Value for HIGH
    """

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
