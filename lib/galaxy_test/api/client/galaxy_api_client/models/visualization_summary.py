from dataclasses import dataclass

from .annotation import Annotation
from .create_time import CreateTime
from .dbkey import Dbkey
from .tags import Tags
from .update_time import UpdateTime

__all__ = ["VisualizationSummary"]


@dataclass
class VisualizationSummary:
    """
    VisualizationSummary dataclass.

    Args:
        create_time (Optional[CreateTime])
                                 : The time and date this item was created.
        deleted (bool)           : Whether this Visualization has been deleted.
        id_ (str)                : Encoded ID of the Visualization.
        importable (bool)        : Whether this Visualization can be imported.
        published (bool)         : Whether this Visualization has been published.
        tags (Tags)              : A list of tags to add to this item.
        title (str)              : The name of the visualization.
        type_ (str)              : The type of the visualization.
        update_time (Optional[UpdateTime])
                                 : The last time and date this item was updated.
        username (str)           : The name of the user owning this Visualization.
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        dbkey (Optional[Dbkey])  : The database key of the visualization.
    """

    create_time: CreateTime | None  # The time and date this item was created.
    deleted: bool  # Whether this Visualization has been deleted.
    id_: str  # Encoded ID of the Visualization.
    importable: bool  # Whether this Visualization can be imported.
    published: bool  # Whether this Visualization has been published.
    tags: Tags  # A list of tags to add to this item.
    title: str  # The name of the visualization.
    type_: str  # The type of the visualization.
    update_time: UpdateTime | None  # The last time and date this item was updated.
    username: str  # The name of the user owning this Visualization.
    annotation: Annotation | None = None  # The annotation of this Visualization.
    dbkey: Dbkey | None = "?"  # The database key of the visualization.
