from dataclasses import dataclass

from .config_ import Config_
from .dbkey import Dbkey
from .deleted import Deleted
from .title import Title

__all__ = ["VisualizationUpdatePayload"]


@dataclass
class VisualizationUpdatePayload:
    """
    VisualizationUpdatePayload dataclass.

    Args:
        config_ (Optional[Config_])
                                 : The config of the visualization.
        dbkey (Optional[Dbkey])  : The database key of the visualization.
        deleted (Optional[Deleted])
                                 : Whether this Visualization has been deleted.
        title (Optional[Title])  : The name of the visualization.
    """

    config_: Config_ | None = None  # The config of the visualization.
    dbkey: Dbkey | None = "?"  # The database key of the visualization.
    deleted: Deleted | None = False  # Whether this Visualization has been deleted.
    title: Title | None = "Untitled Visualization"  # The name of the visualization.
