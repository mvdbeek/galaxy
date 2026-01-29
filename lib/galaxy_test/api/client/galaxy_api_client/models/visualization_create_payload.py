from dataclasses import dataclass

from .config__2 import Config2
from .visualization_create_payload_annotation import VisualizationCreatePayloadAnnotation
from .visualization_create_payload_dbkey import VisualizationCreatePayloadDbkey
from .visualization_create_payload_slug import VisualizationCreatePayloadSlug
from .visualization_create_payload_title import VisualizationCreatePayloadTitle

__all__ = ["VisualizationCreatePayload"]


@dataclass
class VisualizationCreatePayload:
    """
    VisualizationCreatePayload dataclass

    Args:
        type_ (str)              : The type of the visualization. (maps from 'type')
        annotation (VisualizationCreatePayloadAnnotation | None)
                                 : The annotation of the visualization.
        config_ (Config2 | None) : The config of the visualization. (maps from 'config')
        dbkey (VisualizationCreatePayloadDbkey | None)
                                 : The database key of the visualization.
        slug (VisualizationCreatePayloadSlug | None)
                                 : The slug of the visualization.
        title (VisualizationCreatePayloadTitle | None)
                                 : The name of the visualization.
    """

    type_: str  # The type of the visualization. (maps from 'type')
    annotation: VisualizationCreatePayloadAnnotation | None = None  # The annotation of the visualization.
    config_: Config2 | None = None  # The config of the visualization. (maps from 'config')
    dbkey: VisualizationCreatePayloadDbkey | None = None  # The database key of the visualization.
    slug: VisualizationCreatePayloadSlug | None = None  # The slug of the visualization.
    title: VisualizationCreatePayloadTitle | None = "Untitled Visualization"  # The name of the visualization.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "config": "config_",
            "dbkey": "dbkey",
            "slug": "slug",
            "title": "title",
            "type": "type_",
        }
        key_transform_with_dump = {
            "annotation": "annotation",
            "config_": "config",
            "dbkey": "dbkey",
            "slug": "slug",
            "title": "title",
            "type_": "type",
        }
