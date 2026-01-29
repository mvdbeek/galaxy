from dataclasses import dataclass

from .visualization_summary_annotation import VisualizationSummaryAnnotation
from .visualization_summary_create_time import VisualizationSummaryCreateTime
from .visualization_summary_dbkey import VisualizationSummaryDbkey
from .visualization_summary_tags import VisualizationSummaryTags
from .visualization_summary_update_time import VisualizationSummaryUpdateTime

__all__ = ["VisualizationSummary"]


@dataclass
class VisualizationSummary:
    """
    VisualizationSummary dataclass

    Args:
        create_time (VisualizationSummaryCreateTime)
                                 : The time and date this item was created.
        deleted (bool)           : Whether this Visualization has been deleted.
        id_ (str)                : Encoded ID of the Visualization. (maps from 'id')
        importable (bool)        : Whether this Visualization can be imported.
        published (bool)         : Whether this Visualization has been published.
        tags (VisualizationSummaryTags)
                                 : A list of tags to add to this item.
        title (str)              : The name of the visualization.
        type_ (str)              : The type of the visualization. (maps from 'type')
        update_time (VisualizationSummaryUpdateTime)
                                 : The last time and date this item was updated.
        username (str)           : The name of the user owning this Visualization.
        annotation (VisualizationSummaryAnnotation | None)
                                 : The annotation of this Visualization.
        dbkey (VisualizationSummaryDbkey | None)
                                 : The database key of the visualization.
    """

    create_time: VisualizationSummaryCreateTime  # The time and date this item was created.
    deleted: bool  # Whether this Visualization has been deleted.
    id_: str  # Encoded ID of the Visualization. (maps from 'id')
    importable: bool  # Whether this Visualization can be imported.
    published: bool  # Whether this Visualization has been published.
    tags: VisualizationSummaryTags  # A list of tags to add to this item.
    title: str  # The name of the visualization.
    type_: str  # The type of the visualization. (maps from 'type')
    update_time: VisualizationSummaryUpdateTime  # The last time and date this item was updated.
    username: str  # The name of the user owning this Visualization.
    annotation: VisualizationSummaryAnnotation | None = None  # The annotation of this Visualization.
    dbkey: VisualizationSummaryDbkey | None = None  # The database key of the visualization.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "create_time": "create_time",
            "dbkey": "dbkey",
            "deleted": "deleted",
            "id": "id_",
            "importable": "importable",
            "published": "published",
            "tags": "tags",
            "title": "title",
            "type": "type_",
            "update_time": "update_time",
            "username": "username",
        }
        key_transform_with_dump = {
            "annotation": "annotation",
            "create_time": "create_time",
            "dbkey": "dbkey",
            "deleted": "deleted",
            "id_": "id",
            "importable": "importable",
            "published": "published",
            "tags": "tags",
            "title": "title",
            "type_": "type",
            "update_time": "update_time",
            "username": "username",
        }
