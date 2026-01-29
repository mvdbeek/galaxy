from dataclasses import dataclass

from .config__3 import Config3
from .visualization_update_payload_dbkey import VisualizationUpdatePayloadDbkey
from .visualization_update_payload_deleted import VisualizationUpdatePayloadDeleted
from .visualization_update_payload_title import VisualizationUpdatePayloadTitle

__all__ = ["VisualizationUpdatePayload"]


@dataclass
class VisualizationUpdatePayload:
    """
    VisualizationUpdatePayload dataclass

    Args:
        config_ (Config3 | None) : The config of the visualization. (maps from 'config')
        dbkey (VisualizationUpdatePayloadDbkey | None)
                                 : The database key of the visualization.
        deleted (VisualizationUpdatePayloadDeleted | None)
                                 : Whether this Visualization has been deleted.
        title (VisualizationUpdatePayloadTitle | None)
                                 : The name of the visualization.
    """

    config_: Config3 | None = None  # The config of the visualization. (maps from 'config')
    dbkey: VisualizationUpdatePayloadDbkey | None = None  # The database key of the visualization.
    deleted: VisualizationUpdatePayloadDeleted | None = False  # Whether this Visualization has been deleted.
    title: VisualizationUpdatePayloadTitle | None = None  # The name of the visualization.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "config": "config_",
            "dbkey": "dbkey",
            "deleted": "deleted",
            "title": "title",
        }
        key_transform_with_dump = {
            "config_": "config",
            "dbkey": "dbkey",
            "deleted": "deleted",
            "title": "title",
        }
