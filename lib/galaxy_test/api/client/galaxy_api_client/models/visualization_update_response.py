from dataclasses import dataclass

__all__ = ["VisualizationUpdateResponse"]


@dataclass
class VisualizationUpdateResponse:
    """
    VisualizationUpdateResponse dataclass

    Args:
        id_ (str)                : Encoded ID of the Visualization. (maps from 'id')
        revision (str)           : Encoded ID of the Visualization Revision.
    """

    id_: str  # Encoded ID of the Visualization. (maps from 'id')
    revision: str  # Encoded ID of the Visualization Revision.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "revision": "revision",
        }
        key_transform_with_dump = {
            "id_": "id",
            "revision": "revision",
        }
