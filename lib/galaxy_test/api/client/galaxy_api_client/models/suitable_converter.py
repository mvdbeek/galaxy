from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SuitableConverter")


@_attrs_define
class SuitableConverter:
    """
    Attributes:
        name (str): The name of the converter.
        original_type (str): The type to convert from.
        target_type (str): The type to convert to.
        tool_id (str): The ID of the tool that can perform the type conversion.
    """

    name: str
    original_type: str
    target_type: str
    tool_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        original_type = self.original_type

        target_type = self.target_type

        tool_id = self.tool_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "original_type": original_type,
                "target_type": target_type,
                "tool_id": tool_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        original_type = d.pop("original_type")

        target_type = d.pop("target_type")

        tool_id = d.pop("tool_id")

        suitable_converter = cls(
            name=name,
            original_type=original_type,
            target_type=target_type,
            tool_id=tool_id,
        )

        suitable_converter.additional_properties = d
        return suitable_converter

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
