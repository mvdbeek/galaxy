from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolReportForDataset")


@_attrs_define
class ToolReportForDataset:
    """
    Attributes:
        content (None | str | Unset): Text contents of the last page revision with embedded directives expanded (type
            dependent on content_format). Default: ''.
        generate_time (None | str | Unset): The version of Galaxy this object was generated with.
        generate_version (None | str | Unset): The version of Galaxy this object was generated with.
    """

    content: None | str | Unset = ""
    generate_time: None | str | Unset = UNSET
    generate_version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

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
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if generate_time is not UNSET:
            field_dict["generate_time"] = generate_time
        if generate_version is not UNSET:
            field_dict["generate_version"] = generate_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

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

        tool_report_for_dataset = cls(
            content=content,
            generate_time=generate_time,
            generate_version=generate_version,
        )

        tool_report_for_dataset.additional_properties = d
        return tool_report_for_dataset

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
