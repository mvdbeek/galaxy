from dataclasses import dataclass

__all__ = ["DatatypeVisualizationMapping"]


@dataclass
class DatatypeVisualizationMapping:
    """
    DatatypeVisualizationMapping dataclass

    Args:
        datatype (str)           : The datatype extension this visualization applies to
        visualization (str)      : The visualization plugin to use
    """

    datatype: str  # The datatype extension this visualization applies to
    visualization: str  # The visualization plugin to use

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "datatype": "datatype",
            "visualization": "visualization",
        }
        key_transform_with_dump = {
            "datatype": "datatype",
            "visualization": "visualization",
        }
