from dataclasses import dataclass

__all__ = ["Position"]


@dataclass
class Position:
    """
    Position dataclass

    Args:
        left (float)             :
        top (float)              :
    """

    left: float
    top: float

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "left": "left",
            "top": "top",
        }
        key_transform_with_dump = {
            "left": "left",
            "top": "top",
        }
