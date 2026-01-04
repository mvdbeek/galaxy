from dataclasses import dataclass
from datetime import datetime

from .annotation import Annotation
from .content import Content
from .content_editor import ContentEditor
from .generate_time import GenerateTime
from .generate_version import GenerateVersion
from .page_content_format import PageContentFormat
from .revision_ids import RevisionIds
from .tags import Tags

__all__ = ["PageDetails"]


@dataclass
class PageDetails:
    """
    PageDetails dataclass.

    Args:
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        author_deleted (bool)    : Whether the author of this Page has been deleted.
        create_time (datetime)   : The time and date this item was created.
        deleted (bool)           : Whether this Page has been deleted.
        email_hash (str)         : The encoded email of the user.
        id_ (str)                : Encoded ID of the Page.
        importable (bool)        : Whether this Page can be imported.
        latest_revision_id (str) : The encoded ID of the last revision of this Page.
        model_class (str)        : The name of the database model class.
        published (bool)         : Whether this Page has been published.
        revision_ids (RevisionIds): The history with the encoded ID of each revision of the
                                    Page.
        slug (str)               : The identifying slug for the page URL, must be unique.
        tags (Tags)              : The collection of tags associated with an item.
        title (str)              : The name of the page.
        update_time (datetime)   : The last time and date this item was updated.
        username (str)           : The name of the user owning this Page.
        content (Optional[Content])
                                 : Text contents of the last page revision with embedded
                                   directives expanded (type dependent on content_format).
        content_editor (Optional[ContentEditor])
                                 : Raw text contents of the last page revision (type
                                   dependent on content_format).
        content_format (Optional[PageContentFormat])
                                 :
        generate_time (Optional[GenerateTime])
                                 : The version of Galaxy this object was generated with.
        generate_version (Optional[GenerateVersion])
                                 : The version of Galaxy this object was generated with.
    """

    annotation: Annotation | None  # The annotation of this Visualization.
    author_deleted: bool  # Whether the author of this Page has been deleted.
    create_time: datetime  # The time and date this item was created.
    deleted: bool  # Whether this Page has been deleted.
    email_hash: str  # The encoded email of the user.
    id_: str  # Encoded ID of the Page.
    importable: bool  # Whether this Page can be imported.
    latest_revision_id: str  # The encoded ID of the last revision of this Page.
    model_class: str  # The name of the database model class.
    published: bool  # Whether this Page has been published.
    revision_ids: RevisionIds  # The history with the encoded ID of each revision of the Page.
    slug: str  # The identifying slug for the page URL, must be unique.
    tags: Tags  # The collection of tags associated with an item.
    title: str  # The name of the page.
    update_time: datetime  # The last time and date this item was updated.
    username: str  # The name of the user owning this Page.
    content: Content | None = (
        ""  # Text contents of the last page revision with embedded directives expanded (type dependent on content_format).
    )
    content_editor: ContentEditor | None = (
        ""  # Raw text contents of the last page revision (type dependent on content_format).
    )
    content_format: PageContentFormat | None = None
    generate_time: GenerateTime | None = None  # The version of Galaxy this object was generated with.
    generate_version: GenerateVersion | None = None  # The version of Galaxy this object was generated with.
