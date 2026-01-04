from dataclasses import dataclass

__all__ = ["VisualizationUpdateResponse"]


@dataclass
class VisualizationUpdateResponse:
    """
    VisualizationUpdateResponse dataclass.

    Args:
        id_ (str)                : Encoded ID of the Visualization.
        revision (str)           : Encoded ID of the Visualization Revision.
    """

    id_: str  # Encoded ID of the Visualization.
    revision: str  # Encoded ID of the Visualization Revision.
