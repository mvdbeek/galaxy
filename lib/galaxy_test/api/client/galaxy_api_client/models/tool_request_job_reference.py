from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ToolRequestJobReference")


@_attrs_define
class ToolRequestJobReference:
    """
    Attributes:
        id (str):  Example: 0123456789ABCDEF.
        src (Literal['job']):
    """

    id: str
    src: Literal["job"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        src = self.src

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "src": src,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        src = cast(Literal["job"], d.pop("src"))
        if src != "job":
            raise ValueError(f"src must match const 'job', got '{src}'")

        tool_request_job_reference = cls(
            id=id,
            src=src,
        )

        tool_request_job_reference.additional_properties = d
        return tool_request_job_reference

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
