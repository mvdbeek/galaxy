from dataclasses import dataclass
from datetime import datetime

__all__ = ["PageSummary"]


@dataclass
class PageSummary:
    """
    PageSummary dataclass

    Args:
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
    """

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

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "author_deleted": "author_deleted",
            "create_time": "create_time",
            "deleted": "deleted",
            "email_hash": "email_hash",
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
            "author_deleted": "author_deleted",
            "create_time": "create_time",
            "deleted": "deleted",
            "email_hash": "email_hash",
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
