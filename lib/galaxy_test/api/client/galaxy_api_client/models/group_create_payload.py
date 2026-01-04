from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupCreatePayload")


@_attrs_define
class GroupCreatePayload:
    """Payload schema for creating a group.

    Attributes:
        name (str):
        role_ids (list[str] | Unset):
        user_ids (list[str] | Unset):
    """

    name: str
    role_ids: list[str] | Unset = UNSET
    user_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        role_ids: list[str] | Unset = UNSET
        if not isinstance(self.role_ids, Unset):
            role_ids = self.role_ids

        user_ids: list[str] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if role_ids is not UNSET:
            field_dict["role_ids"] = role_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        role_ids = cast(list[str], d.pop("role_ids", UNSET))

        user_ids = cast(list[str], d.pop("user_ids", UNSET))

        group_create_payload = cls(
            name=name,
            role_ids=role_ids,
            user_ids=user_ids,
        )

        group_create_payload.additional_properties = d
        return group_create_payload

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
