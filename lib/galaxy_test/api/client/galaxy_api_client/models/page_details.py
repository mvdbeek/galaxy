from dataclasses import dataclass
from datetime import datetime

from .page_content_format import PageContentFormat
from .page_details_annotation import PageDetailsAnnotation
from .page_details_content import PageDetailsContent
from .page_details_content_editor import PageDetailsContentEditor
from .page_details_generate_time import PageDetailsGenerateTime
from .page_details_generate_version import PageDetailsGenerateVersion

__all__ = ["PageDetails"]


@dataclass
class PageDetails:
    """
    PageDetails dataclass

    Args:
        annotation (PageDetailsAnnotation)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        author_deleted (bool)    : Whether the author of this Page has been deleted.
        create_time (datetime)   : The time and date this item was created.
        deleted (bool)           : Whether this Page has been deleted.
        email_hash (str)         : The encoded email of the user.
        id_ (str)                : Encoded ID of the Page. (maps from 'id')
        importable (bool)        : Whether this Page can be imported.
        latest_revision_id (str) : The encoded ID of the last revision of this Page.
        model_class (str)        : The name of the database model class.
        published (bool)         : Whether this Page has been published.
        revision_ids (List[str]) : The history with the encoded ID of each revision of the
                                   Page.
        slug (str)               : The identifying slug for the page URL, must be unique.
        tags (List[str])         : The collection of tags associated with an item.
        title (str)              : The name of the page.
        update_time (datetime)   : The last time and date this item was updated.
        username (str)           : The name of the user owning this Page.
        content (PageDetailsContent | None)
                                 : Text contents of the last page revision with embedded
                                   directives expanded (type dependent on content_format).
        content_editor (PageDetailsContentEditor | None)
                                 : Raw text contents of the last page revision (type
                                   dependent on content_format).
        content_format (PageContentFormat | None)
                                 :
        generate_time (PageDetailsGenerateTime | None)
                                 : The version of Galaxy this object was generated with.
        generate_version (PageDetailsGenerateVersion | None)
                                 : The version of Galaxy this object was generated with.
    """

    annotation: PageDetailsAnnotation  # An annotation to provide details or to help understand the purpose and usage of this item.
    author_deleted: bool  # Whether the author of this Page has been deleted.
    create_time: datetime  # The time and date this item was created.
    deleted: bool  # Whether this Page has been deleted.
    email_hash: str  # The encoded email of the user.
    id_: str  # Encoded ID of the Page. (maps from 'id')
    importable: bool  # Whether this Page can be imported.
    latest_revision_id: str  # The encoded ID of the last revision of this Page.
    model_class: str  # The name of the database model class.
    published: bool  # Whether this Page has been published.
    revision_ids: list[str]  # The history with the encoded ID of each revision of the Page.
    slug: str  # The identifying slug for the page URL, must be unique.
    tags: list[str]  # The collection of tags associated with an item.
    title: str  # The name of the page.
    update_time: datetime  # The last time and date this item was updated.
    username: str  # The name of the user owning this Page.
    content: PageDetailsContent | None = (
        ""  # Text contents of the last page revision with embedded directives expanded (type dependent on content_format).
    )
    content_editor: PageDetailsContentEditor | None = (
        ""  # Raw text contents of the last page revision (type dependent on content_format).
    )
    content_format: PageContentFormat | None = None
    generate_time: PageDetailsGenerateTime | None = None  # The version of Galaxy this object was generated with.
    generate_version: PageDetailsGenerateVersion | None = None  # The version of Galaxy this object was generated with.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "author_deleted": "author_deleted",
            "content": "content",
            "content_editor": "content_editor",
            "content_format": "content_format",
            "create_time": "create_time",
            "deleted": "deleted",
            "email_hash": "email_hash",
            "generate_time": "generate_time",
            "generate_version": "generate_version",
            "id": "id_",
            "importable": "importable",
            "latest_revision_id": "latest_revision_id",
            "model_class": "model_class",
            "published": "published",
            "revision_ids": "revision_ids",
            "slug": "slug",
            "tags": "tags",
            "title": "title",
            "update_time": "update_time",
            "username": "username",
        }
        key_transform_with_dump = {
            "annotation": "annotation",
            "author_deleted": "author_deleted",
            "content": "content",
            "content_editor": "content_editor",
            "content_format": "content_format",
            "create_time": "create_time",
            "deleted": "deleted",
            "email_hash": "email_hash",
            "generate_time": "generate_time",
            "generate_version": "generate_version",
            "id_": "id",
            "importable": "importable",
            "latest_revision_id": "latest_revision_id",
            "model_class": "model_class",
            "published": "published",
            "revision_ids": "revision_ids",
            "slug": "slug",
            "tags": "tags",
            "title": "title",
            "update_time": "update_time",
            "username": "username",
        }
