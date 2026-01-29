from dataclasses import dataclass

__all__ = ["VisualizationCreateResponse"]


@dataclass
class VisualizationCreateResponse:
    """
    VisualizationCreateResponse dataclass

    Args:
        id_ (str)                : Encoded ID of the Visualization. (maps from 'id')
    """

    id_: str  # Encoded ID of the Visualization. (maps from 'id')

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
        }
        key_transform_with_dump = {
            "id_": "id",
        }
