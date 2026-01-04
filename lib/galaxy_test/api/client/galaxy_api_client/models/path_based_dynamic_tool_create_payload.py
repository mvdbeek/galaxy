from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PathBasedDynamicToolCreatePayload")


@_attrs_define
class PathBasedDynamicToolCreatePayload:
    """
    Attributes:
        path (str):
        src (Literal['from_path']):
        active (bool | None | Unset):
        hidden (bool | None | Unset):
        tool_directory (None | str | Unset):
    """

    path: str
    src: Literal["from_path"]
    active: bool | None | Unset = UNSET
    hidden: bool | None | Unset = UNSET
    tool_directory: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        src = self.src

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        hidden: bool | None | Unset
        if isinstance(self.hidden, Unset):
            hidden = UNSET
        else:
            hidden = self.hidden

        tool_directory: None | str | Unset
        if isinstance(self.tool_directory, Unset):
            tool_directory = UNSET
        else:
            tool_directory = self.tool_directory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "src": src,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if tool_directory is not UNSET:
            field_dict["tool_directory"] = tool_directory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        src = cast(Literal["from_path"], d.pop("src"))
        if src != "from_path":
            raise ValueError(f"src must match const 'from_path', got '{src}'")

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_hidden(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hidden = _parse_hidden(d.pop("hidden", UNSET))

        def _parse_tool_directory(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_directory = _parse_tool_directory(d.pop("tool_directory", UNSET))

        path_based_dynamic_tool_create_payload = cls(
            path=path,
            src=src,
            active=active,
            hidden=hidden,
            tool_directory=tool_directory,
        )

        path_based_dynamic_tool_create_payload.additional_properties = d
        return path_based_dynamic_tool_create_payload

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
