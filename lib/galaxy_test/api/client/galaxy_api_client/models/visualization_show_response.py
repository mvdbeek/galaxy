from dataclasses import dataclass

from .visualization_revision_response import VisualizationRevisionResponse
from .visualization_show_response_annotation import VisualizationShowResponseAnnotation
from .visualization_show_response_dbkey import VisualizationShowResponseDbkey
from .visualization_show_response_plugin import VisualizationShowResponsePlugin
from .visualization_show_response_slug import VisualizationShowResponseSlug
from .visualization_show_response_tags import VisualizationShowResponseTags

__all__ = ["VisualizationShowResponse"]


@dataclass
class VisualizationShowResponse:
    """
    VisualizationShowResponse dataclass

    Args:
        email_hash (str)         : The hash of the email of the user owning this
                                   Visualization.
        id_ (str)                : Encoded ID of the Visualization. (maps from 'id')
        latest_revision (VisualizationRevisionResponse)
                                 :
        model_class (str)        : The name of the database model class.
        revisions (List[str])    : A list of encoded IDs of the revisions of this
                                   Visualization.
        title (str)              : The name of the visualization.
        type_ (str)              : The type of the visualization. (maps from 'type')
        url (str)                : The URL of the visualization.
        user_id (str)            : The ID of the user owning this Visualization.
        username (str)           : The name of the user owning this Visualization.
        annotation (VisualizationShowResponseAnnotation | None)
                                 : The annotation of this Visualization.
        dbkey (VisualizationShowResponseDbkey | None)
                                 : The database key of the visualization.
        plugin (VisualizationShowResponsePlugin | None)
                                 : The plugin of this Visualization.
        slug (VisualizationShowResponseSlug | None)
                                 : The slug of the visualization.
        tags (VisualizationShowResponseTags | None)
                                 : A list of tags to add to this item.
    """

    email_hash: str  # The hash of the email of the user owning this Visualization.
    id_: str  # Encoded ID of the Visualization. (maps from 'id')
    latest_revision: VisualizationRevisionResponse
    model_class: str  # The name of the database model class.
    revisions: list[str]  # A list of encoded IDs of the revisions of this Visualization.
    title: str  # The name of the visualization.
    type_: str  # The type of the visualization. (maps from 'type')
    url: str  # The URL of the visualization.
    user_id: str  # The ID of the user owning this Visualization.
    username: str  # The name of the user owning this Visualization.
    annotation: VisualizationShowResponseAnnotation | None = None  # The annotation of this Visualization.
    dbkey: VisualizationShowResponseDbkey | None = None  # The database key of the visualization.
    plugin: VisualizationShowResponsePlugin | None = None  # The plugin of this Visualization.
    slug: VisualizationShowResponseSlug | None = None  # The slug of the visualization.
    tags: VisualizationShowResponseTags | None = None  # A list of tags to add to this item.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "dbkey": "dbkey",
            "email_hash": "email_hash",
            "id": "id_",
            "latest_revision": "latest_revision",
            "model_class": "model_class",
            "plugin": "plugin",
            "revisions": "revisions",
            "slug": "slug",
            "tags": "tags",
            "title": "title",
            "type": "type_",
            "url": "url",
            "user_id": "user_id",
            "username": "username",
        }
        key_transform_with_dump = {
            "annotation": "annotation",
            "dbkey": "dbkey",
            "email_hash": "email_hash",
            "id_": "id",
            "latest_revision": "latest_revision",
            "model_class": "model_class",
            "plugin": "plugin",
            "revisions": "revisions",
            "slug": "slug",
            "tags": "tags",
            "title": "title",
            "type_": "type",
            "url": "url",
            "user_id": "user_id",
            "username": "username",
        }
