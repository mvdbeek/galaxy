from dataclasses import dataclass

from .visualization_revision_response_config import VisualizationRevisionResponseConfig
from .visualization_revision_response_dbkey import VisualizationRevisionResponseDbkey

__all__ = ["VisualizationRevisionResponse"]


@dataclass
class VisualizationRevisionResponse:
    """
    VisualizationRevisionResponse dataclass

    Args:
        config_ (VisualizationRevisionResponseConfig)
                                 : The config of the visualization revision. (maps from
                                   'config')
        id_ (str)                : Encoded ID of the Visualization Revision. (maps from
                                   'id')
        model_class (str)        : The name of the database model class.
        title (str)              : The name of the visualization revision.
        visualization_id (str)   : Encoded ID of the Visualization.
        dbkey (VisualizationRevisionResponseDbkey | None)
                                 : The database key of the visualization.
    """

    config_: VisualizationRevisionResponseConfig  # The config of the visualization revision. (maps from 'config')
    id_: str  # Encoded ID of the Visualization Revision. (maps from 'id')
    model_class: str  # The name of the database model class.
    title: str  # The name of the visualization revision.
    visualization_id: str  # Encoded ID of the Visualization.
    dbkey: VisualizationRevisionResponseDbkey | None = None  # The database key of the visualization.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "config": "config_",
            "dbkey": "dbkey",
            "id": "id_",
            "model_class": "model_class",
            "title": "title",
            "visualization_id": "visualization_id",
        }
        key_transform_with_dump = {
            "config_": "config",
            "dbkey": "dbkey",
            "id_": "id",
            "model_class": "model_class",
            "title": "title",
            "visualization_id": "visualization_id",
        }
