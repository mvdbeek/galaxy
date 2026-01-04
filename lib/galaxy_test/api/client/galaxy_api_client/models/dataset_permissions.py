from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetPermissions")


@_attrs_define
class DatasetPermissions:
    """Role-based permissions for accessing and managing a dataset.

    Attributes:
        access (list[str] | Unset): The set of roles (encoded IDs) that can access this dataset.
        manage (list[str] | Unset): The set of roles (encoded IDs) that can manage this dataset.
    """

    access: list[str] | Unset = UNSET
    manage: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access: list[str] | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access

        manage: list[str] | Unset = UNSET
        if not isinstance(self.manage, Unset):
            manage = self.manage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if manage is not UNSET:
            field_dict["manage"] = manage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access = cast(list[str], d.pop("access", UNSET))

        manage = cast(list[str], d.pop("manage", UNSET))

        dataset_permissions = cls(
            access=access,
            manage=manage,
        )

        dataset_permissions.additional_properties = d
        return dataset_permissions

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
