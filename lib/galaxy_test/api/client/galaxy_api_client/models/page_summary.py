from dataclasses import dataclass
from datetime import datetime

from .revision_ids import RevisionIds
from .tags import Tags

__all__ = ["PageSummary"]


@dataclass
class PageSummary:
    """
    PageSummary dataclass.

    Args:
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
    """

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
