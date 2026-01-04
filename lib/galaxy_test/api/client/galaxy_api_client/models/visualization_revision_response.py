from dataclasses import dataclass

from .config_ import Config_
from .dbkey import Dbkey

__all__ = ["VisualizationRevisionResponse"]


@dataclass
class VisualizationRevisionResponse:
    """
    VisualizationRevisionResponse dataclass.

    Args:
        config_ (Config_)        : The config of the visualization revision.
        id_ (str)                : Encoded ID of the Visualization Revision.
        model_class (str)        : The name of the database model class.
        title (str)              : The name of the visualization revision.
        visualization_id (str)   : Encoded ID of the Visualization.
        dbkey (Optional[Dbkey])  : The database key of the visualization.
    """

    config_: Config_  # The config of the visualization revision.
    id_: str  # Encoded ID of the Visualization Revision.
    model_class: str  # The name of the database model class.
    title: str  # The name of the visualization revision.
    visualization_id: str  # Encoded ID of the Visualization.
    dbkey: Dbkey | None = "?"  # The database key of the visualization.
