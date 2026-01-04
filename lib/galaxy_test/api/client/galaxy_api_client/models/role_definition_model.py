from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role_definition_model_role_type import RoleDefinitionModelRoleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleDefinitionModel")


@_attrs_define
class RoleDefinitionModel:
    """
    Attributes:
        description (str): Description of the role
        name (str): Name of the role
        group_ids (list[str] | None | Unset):
        role_type (RoleDefinitionModelRoleType | Unset):  Default: RoleDefinitionModelRoleType.ADMIN.
        user_ids (list[str] | None | Unset):
    """

    description: str
    name: str
    group_ids: list[str] | None | Unset = UNSET
    role_type: RoleDefinitionModelRoleType | Unset = RoleDefinitionModelRoleType.ADMIN
    user_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        group_ids: list[str] | None | Unset
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        role_type: str | Unset = UNSET
        if not isinstance(self.role_type, Unset):
            role_type = self.role_type.value

        user_ids: list[str] | None | Unset
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = self.user_ids

        else:
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
            }
        )
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if role_type is not UNSET:
            field_dict["role_type"] = role_type
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        def _parse_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        _role_type = d.pop("role_type", UNSET)
        role_type: RoleDefinitionModelRoleType | Unset
        if isinstance(_role_type, Unset):
            role_type = UNSET
        else:
            role_type = RoleDefinitionModelRoleType(_role_type)

        def _parse_user_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = cast(list[str], data)

                return user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        user_ids = _parse_user_ids(d.pop("user_ids", UNSET))

        role_definition_model = cls(
            description=description,
            name=name,
            group_ids=group_ids,
            role_type=role_type,
            user_ids=user_ids,
        )

        role_definition_model.additional_properties = d
        return role_definition_model

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
