from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.page_content_format import PageContentFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePagePayload")


@_attrs_define
class CreatePagePayload:
    """
    Attributes:
        slug (str): The identifying slug for the page URL, must be unique.
        title (str): The name of the page.
        annotation (None | str | Unset): Annotation that will be attached to the page.
        content (None | str | Unset): Text contents of the last page revision with embedded directives expanded (type
            dependent on content_format). Default: ''.
        content_format (PageContentFormat | Unset):
        invocation_id (None | str | Unset): Encoded ID used by workflow generated reports.
    """

    slug: str
    title: str
    annotation: None | str | Unset = UNSET
    content: None | str | Unset = ""
    content_format: PageContentFormat | Unset = UNSET
    invocation_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        title = self.title

        annotation: None | str | Unset
        if isinstance(self.annotation, Unset):
            annotation = UNSET
        else:
            annotation = self.annotation

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        content_format: str | Unset = UNSET
        if not isinstance(self.content_format, Unset):
            content_format = self.content_format.value

        invocation_id: None | str | Unset
        if isinstance(self.invocation_id, Unset):
            invocation_id = UNSET
        else:
            invocation_id = self.invocation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "title": title,
            }
        )
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if content is not UNSET:
            field_dict["content"] = content
        if content_format is not UNSET:
            field_dict["content_format"] = content_format
        if invocation_id is not UNSET:
            field_dict["invocation_id"] = invocation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        title = d.pop("title")

        def _parse_annotation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annotation = _parse_annotation(d.pop("annotation", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        _content_format = d.pop("content_format", UNSET)
        content_format: PageContentFormat | Unset
        if isinstance(_content_format, Unset):
            content_format = UNSET
        else:
            content_format = PageContentFormat(_content_format)

        def _parse_invocation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invocation_id = _parse_invocation_id(d.pop("invocation_id", UNSET))

        create_page_payload = cls(
            slug=slug,
            title=title,
            annotation=annotation,
            content=content,
            content_format=content_format,
            invocation_id=invocation_id,
        )

        create_page_payload.additional_properties = d
        return create_page_payload

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
