from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_build_len_type import CustomBuildLenType

T = TypeVar("T", bound="CustomBuildCreationPayload")


@_attrs_define
class CustomBuildCreationPayload:
    """
    Attributes:
        lentype (CustomBuildLenType):
        lenvalue (str): The content of the length file.
        name (str): The name of the custom build.
    """

    lentype: CustomBuildLenType
    lenvalue: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lentype = self.lentype.value

        lenvalue = self.lenvalue

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "len|type": lentype,
                "len|value": lenvalue,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lentype = CustomBuildLenType(d.pop("len|type"))

        lenvalue = d.pop("len|value")

        name = d.pop("name")

        custom_build_creation_payload = cls(
            lentype=lentype,
            lenvalue=lenvalue,
            name=name,
        )

        custom_build_creation_payload.additional_properties = d
        return custom_build_creation_payload

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
