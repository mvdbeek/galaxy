from dataclasses import dataclass

__all__ = ["ToolRequestJobReference"]


@dataclass
class ToolRequestJobReference:
    """
    ToolRequestJobReference dataclass

    Args:
        id_ (str)                : Maps from 'id'
        src (str)                :
    """

    id_: str  # Maps from 'id'
    src: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "src": "src",
        }
        key_transform_with_dump = {
            "id_": "id",
            "src": "src",
        }
