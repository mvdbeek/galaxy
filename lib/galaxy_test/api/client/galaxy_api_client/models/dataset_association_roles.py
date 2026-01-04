from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetAssociationRoles")


@_attrs_define
class DatasetAssociationRoles:
    """
    Attributes:
        access_dataset_roles (list[list[str]] | Unset): A list of roles that can access the dataset. The user has to
            **have all these roles** in order to access this dataset. Users without access permission **cannot** have other
            permissions on this dataset. If there are no access roles set on the dataset it is considered **unrestricted**.
        manage_dataset_roles (list[list[str]] | Unset): A list of roles that can manage permissions on the dataset.
            Users with **any** of these roles can manage permissions of this dataset. If you remove yourself you will lose
            the ability to manage this dataset unless you are an admin.
        modify_item_roles (list[list[str]] | Unset): A list of roles that can modify the library item. This is a library
            related permission. User with **any** of these roles can modify name, metadata, and other information about this
            library item.
    """

    access_dataset_roles: list[list[str]] | Unset = UNSET
    manage_dataset_roles: list[list[str]] | Unset = UNSET
    modify_item_roles: list[list[str]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_dataset_roles: list[list[str]] | Unset = UNSET
        if not isinstance(self.access_dataset_roles, Unset):
            access_dataset_roles = []
            for access_dataset_roles_item_data in self.access_dataset_roles:
                access_dataset_roles_item = access_dataset_roles_item_data

                access_dataset_roles.append(access_dataset_roles_item)

        manage_dataset_roles: list[list[str]] | Unset = UNSET
        if not isinstance(self.manage_dataset_roles, Unset):
            manage_dataset_roles = []
            for manage_dataset_roles_item_data in self.manage_dataset_roles:
                manage_dataset_roles_item = manage_dataset_roles_item_data

                manage_dataset_roles.append(manage_dataset_roles_item)

        modify_item_roles: list[list[str]] | Unset = UNSET
        if not isinstance(self.modify_item_roles, Unset):
            modify_item_roles = []
            for modify_item_roles_item_data in self.modify_item_roles:
                modify_item_roles_item = modify_item_roles_item_data

                modify_item_roles.append(modify_item_roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_dataset_roles is not UNSET:
            field_dict["access_dataset_roles"] = access_dataset_roles
        if manage_dataset_roles is not UNSET:
            field_dict["manage_dataset_roles"] = manage_dataset_roles
        if modify_item_roles is not UNSET:
            field_dict["modify_item_roles"] = modify_item_roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _access_dataset_roles = d.pop("access_dataset_roles", UNSET)
        access_dataset_roles: list[list[str]] | Unset = UNSET
        if _access_dataset_roles is not UNSET:
            access_dataset_roles = []
            for access_dataset_roles_item_data in _access_dataset_roles:
                access_dataset_roles_item = cast(list[str], access_dataset_roles_item_data)

                access_dataset_roles.append(access_dataset_roles_item)

        _manage_dataset_roles = d.pop("manage_dataset_roles", UNSET)
        manage_dataset_roles: list[list[str]] | Unset = UNSET
        if _manage_dataset_roles is not UNSET:
            manage_dataset_roles = []
            for manage_dataset_roles_item_data in _manage_dataset_roles:
                manage_dataset_roles_item = cast(list[str], manage_dataset_roles_item_data)

                manage_dataset_roles.append(manage_dataset_roles_item)

        _modify_item_roles = d.pop("modify_item_roles", UNSET)
        modify_item_roles: list[list[str]] | Unset = UNSET
        if _modify_item_roles is not UNSET:
            modify_item_roles = []
            for modify_item_roles_item_data in _modify_item_roles:
                modify_item_roles_item = cast(list[str], modify_item_roles_item_data)

                modify_item_roles.append(modify_item_roles_item)

        dataset_association_roles = cls(
            access_dataset_roles=access_dataset_roles,
            manage_dataset_roles=manage_dataset_roles,
            modify_item_roles=modify_item_roles,
        )

        dataset_association_roles.additional_properties = d
        return dataset_association_roles

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
