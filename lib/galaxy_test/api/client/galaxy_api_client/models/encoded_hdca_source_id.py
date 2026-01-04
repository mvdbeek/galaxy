from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EncodedHdcaSourceId")


@_attrs_define
class EncodedHdcaSourceId:
    """
    Attributes:
        id (str):  Example: 0123456789ABCDEF.
        src (Literal['hdca']): The source of this dataset, which in the case of the model can only be `hdca`.
    """

    id: str
    src: Literal["hdca"]
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

        src = cast(Literal["hdca"], d.pop("src"))
        if src != "hdca":
            raise ValueError(f"src must match const 'hdca', got '{src}'")

        encoded_hdca_source_id = cls(
            id=id,
            src=src,
        )

        encoded_hdca_source_id.additional_properties = d
        return encoded_hdca_source_id

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
