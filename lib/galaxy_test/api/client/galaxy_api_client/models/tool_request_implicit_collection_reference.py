from dataclasses import dataclass

__all__ = ["ToolRequestImplicitCollectionReference"]


@dataclass
class ToolRequestImplicitCollectionReference:
    """
    ToolRequestImplicitCollectionReference dataclass

    Args:
        id_ (str)                : Maps from 'id'
        output_name (str)        :
        src (str)                :
    """

    id_: str  # Maps from 'id'
    output_name: str
    src: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "output_name": "output_name",
            "src": "src",
        }
        key_transform_with_dump = {
            "id_": "id",
            "output_name": "output_name",
            "src": "src",
        }
