from dataclasses import dataclass

__all__ = ["VisualizationCreateResponse"]


@dataclass
class VisualizationCreateResponse:
    """
    VisualizationCreateResponse dataclass.

    Args:
        id_ (str)                : Encoded ID of the Visualization.
    """

    id_: str  # Encoded ID of the Visualization.
