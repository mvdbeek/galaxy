from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DatasetInheritanceChainEntry")


@_attrs_define
class DatasetInheritanceChainEntry:
    """
    Attributes:
        dep (str): Name of the source of the referenced dataset at this point of the inheritance chain.
        id (str): ID of the referenced dataset Example: 0123456789ABCDEF.
        name (str): Name of the referenced dataset
        user_id (str): ID of the user who owns the referenced dataset. Example: 0123456789ABCDEF.
    """

    dep: str
    id: str
    name: str
    user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dep = self.dep

        id = self.id

        name = self.name

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dep": dep,
                "id": id,
                "name": name,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dep = d.pop("dep")

        id = d.pop("id")

        name = d.pop("name")

        user_id = d.pop("user_id")

        dataset_inheritance_chain_entry = cls(
            dep=dep,
            id=id,
            name=name,
            user_id=user_id,
        )

        dataset_inheritance_chain_entry.additional_properties = d
        return dataset_inheritance_chain_entry

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
