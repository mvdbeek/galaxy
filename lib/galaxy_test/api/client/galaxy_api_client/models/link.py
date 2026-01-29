from dataclasses import dataclass

__all__ = ["Link"]


@dataclass
class Link:
    """
    Link dataclass

    Args:
        name (str)               :
    """

    name: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "name": "name",
        }
        key_transform_with_dump = {
            "name": "name",
        }
