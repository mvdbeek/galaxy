from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.page_content_format import PageContentFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="PageDetails")


@_attrs_define
class PageDetails:
    """
    Attributes:
        annotation (None | str): An annotation to provide details or to help understand the purpose and usage of this
            item.
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
        content (None | str | Unset): Text contents of the last page revision with embedded directives expanded (type
            dependent on content_format). Default: ''.
        content_editor (None | str | Unset): Raw text contents of the last page revision (type dependent on
            content_format). Default: ''.
        content_format (PageContentFormat | Unset):
        generate_time (None | str | Unset): The version of Galaxy this object was generated with.
        generate_version (None | str | Unset): The version of Galaxy this object was generated with.
    """

    annotation: None | str
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
    content: None | str | Unset = ""
    content_editor: None | str | Unset = ""
    content_format: PageContentFormat | Unset = UNSET
    generate_time: None | str | Unset = UNSET
    generate_version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotation: None | str
        annotation = self.annotation

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

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        content_editor: None | str | Unset
        if isinstance(self.content_editor, Unset):
            content_editor = UNSET
        else:
            content_editor = self.content_editor

        content_format: str | Unset = UNSET
        if not isinstance(self.content_format, Unset):
            content_format = self.content_format.value

        generate_time: None | str | Unset
        if isinstance(self.generate_time, Unset):
            generate_time = UNSET
        else:
            generate_time = self.generate_time

        generate_version: None | str | Unset
        if isinstance(self.generate_version, Unset):
            generate_version = UNSET
        else:
            generate_version = self.generate_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annotation": annotation,
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
        if content is not UNSET:
            field_dict["content"] = content
        if content_editor is not UNSET:
            field_dict["content_editor"] = content_editor
        if content_format is not UNSET:
            field_dict["content_format"] = content_format
        if generate_time is not UNSET:
            field_dict["generate_time"] = generate_time
        if generate_version is not UNSET:
            field_dict["generate_version"] = generate_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_annotation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        annotation = _parse_annotation(d.pop("annotation"))

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

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_content_editor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_editor = _parse_content_editor(d.pop("content_editor", UNSET))

        _content_format = d.pop("content_format", UNSET)
        content_format: PageContentFormat | Unset
        if isinstance(_content_format, Unset):
            content_format = UNSET
        else:
            content_format = PageContentFormat(_content_format)

        def _parse_generate_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generate_time = _parse_generate_time(d.pop("generate_time", UNSET))

        def _parse_generate_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generate_version = _parse_generate_version(d.pop("generate_version", UNSET))

        page_details = cls(
            annotation=annotation,
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
            content=content,
            content_editor=content_editor,
            content_format=content_format,
            generate_time=generate_time,
            generate_version=generate_version,
        )

        page_details.additional_properties = d
        return page_details

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
