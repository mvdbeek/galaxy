from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="PageSummary")


@_attrs_define
class PageSummary:
    """
    Attributes:
        author_deleted (bool): Whether the author of this Page has been deleted.
        create_time (datetime.datetime): The time and date this item was created.
        deleted (bool): Whether this Page has been deleted.
        email_hash (str): The encoded email of the user.
        id (str): Encoded ID of the Page. Example: 0123456789ABCDEF.
        importable (bool): Whether this Page can be imported.
        latest_revision_id (str): The encoded ID of the last revision of this Page. Example: 0123456789ABCDEF.
        model_class (Literal['Page']): The name of the database model class.
        published (bool): Whether this Page has been published.
        revision_ids (list[str]): The history with the encoded ID of each revision of the Page.
        slug (str): The identifying slug for the page URL, must be unique.
        tags (list[str]): The collection of tags associated with an item.
        title (str): The name of the page.
        update_time (datetime.datetime): The last time and date this item was updated.
        username (str): The name of the user owning this Page.
    """

    author_deleted: bool
    create_time: datetime.datetime
    deleted: bool
    email_hash: str
    id: str
    importable: bool
    latest_revision_id: str
    model_class: Literal["Page"]
    published: bool
    revision_ids: list[str]
    slug: str
    tags: list[str]
    title: str
    update_time: datetime.datetime
    username: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_deleted = self.author_deleted

        create_time = self.create_time.isoformat()

        deleted = self.deleted

        email_hash = self.email_hash

        id = self.id

        importable = self.importable

        latest_revision_id = self.latest_revision_id

        model_class = self.model_class

        published = self.published

        revision_ids = self.revision_ids

        slug = self.slug

        tags = self.tags

        title = self.title

        update_time = self.update_time.isoformat()

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author_deleted": author_deleted,
                "create_time": create_time,
                "deleted": deleted,
                "email_hash": email_hash,
                "id": id,
                "importable": importable,
                "latest_revision_id": latest_revision_id,
                "model_class": model_class,
                "published": published,
                "revision_ids": revision_ids,
                "slug": slug,
                "tags": tags,
                "title": title,
                "update_time": update_time,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author_deleted = d.pop("author_deleted")

        create_time = isoparse(d.pop("create_time"))

        deleted = d.pop("deleted")

        email_hash = d.pop("email_hash")

        id = d.pop("id")

        importable = d.pop("importable")

        latest_revision_id = d.pop("latest_revision_id")

        model_class = cast(Literal["Page"], d.pop("model_class"))
        if model_class != "Page":
            raise ValueError(f"model_class must match const 'Page', got '{model_class}'")

        published = d.pop("published")

        revision_ids = cast(list[str], d.pop("revision_ids"))

        slug = d.pop("slug")

        tags = cast(list[str], d.pop("tags"))

        title = d.pop("title")

        update_time = isoparse(d.pop("update_time"))

        username = d.pop("username")

        page_summary = cls(
            author_deleted=author_deleted,
            create_time=create_time,
            deleted=deleted,
            email_hash=email_hash,
            id=id,
            importable=importable,
            latest_revision_id=latest_revision_id,
            model_class=model_class,
            published=published,
            revision_ids=revision_ids,
            slug=slug,
            tags=tags,
            title=title,
            update_time=update_time,
            username=username,
        )

        page_summary.additional_properties = d
        return page_summary

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
