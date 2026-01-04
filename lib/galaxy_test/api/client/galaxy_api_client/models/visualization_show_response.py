from dataclasses import dataclass

from .annotation import Annotation
from .dbkey import Dbkey
from .plugin import Plugin
from .revisions import Revisions
from .slug import Slug
from .tags import Tags
from .visualization_revision_response import VisualizationRevisionResponse

__all__ = ["VisualizationShowResponse"]


@dataclass
class VisualizationShowResponse:
    """
    VisualizationShowResponse dataclass.

    Args:
        email_hash (str)         : The hash of the email of the user owning this
                                   Visualization.
        id_ (str)                : Encoded ID of the Visualization.
        latest_revision (VisualizationRevisionResponse)
                                 :
        model_class (str)        : The name of the database model class.
        revisions (Revisions)    : A list of encoded IDs of the revisions of this
                                   Visualization.
        title (str)              : The name of the visualization.
        type_ (str)              : The type of the visualization.
        url (str)                : The URL of the visualization.
        user_id (str)            : The ID of the user owning this Visualization.
        username (str)           : The name of the user owning this Visualization.
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        dbkey (Optional[Dbkey])  : The database key of the visualization.
        plugin (Optional[Plugin]): The plugin of this Visualization.
        slug (Optional[Slug])    : The slug of the visualization.
        tags (Optional[Tags])    : A list of tags to add to this item.
    """

    email_hash: str  # The hash of the email of the user owning this Visualization.
    id_: str  # Encoded ID of the Visualization.
    latest_revision: VisualizationRevisionResponse
    model_class: str  # The name of the database model class.
    revisions: Revisions  # A list of encoded IDs of the revisions of this Visualization.
    title: str  # The name of the visualization.
    type_: str  # The type of the visualization.
    url: str  # The URL of the visualization.
    user_id: str  # The ID of the user owning this Visualization.
    username: str  # The name of the user owning this Visualization.
    annotation: Annotation | None = None  # The annotation of this Visualization.
    dbkey: Dbkey | None = "?"  # The database key of the visualization.
    plugin: Plugin | None = None  # The plugin of this Visualization.
    slug: Slug | None = None  # The slug of the visualization.
    tags: Tags | None = None  # A list of tags to add to this item.
