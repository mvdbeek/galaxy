from dataclasses import dataclass

from .annotation import Annotation
from .config_ import Config_
from .dbkey import Dbkey
from .slug import Slug
from .title import Title

__all__ = ["VisualizationCreatePayload"]


@dataclass
class VisualizationCreatePayload:
    """
    VisualizationCreatePayload dataclass.

    Args:
        type_ (str)              : The type of the visualization.
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        config_ (Optional[Config_])
                                 : The config of the visualization.
        dbkey (Optional[Dbkey])  : The database key of the visualization.
        slug (Optional[Slug])    : The slug of the visualization.
        title (Optional[Title])  : The name of the visualization.
    """

    type_: str  # The type of the visualization.
    annotation: Annotation | None = None  # The annotation of this Visualization.
    config_: Config_ | None = None  # The config of the visualization.
    dbkey: Dbkey | None = "?"  # The database key of the visualization.
    slug: Slug | None = None  # The slug of the visualization.
    title: Title | None = "Untitled Visualization"  # The name of the visualization.
