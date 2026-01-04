from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUpdatePayload")


@_attrs_define
class UserUpdatePayload:
    """
    Attributes:
        active (bool | None | Unset): User is active
        preferred_object_store_id (None | str | Unset): The ID of the object store that should be used to store new
            datasets in this history.
        username (None | str | Unset): The name of the user.
    """

    active: bool | None | Unset = UNSET
    preferred_object_store_id: None | str | Unset = UNSET
    username: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        preferred_object_store_id: None | str | Unset
        if isinstance(self.preferred_object_store_id, Unset):
            preferred_object_store_id = UNSET
        else:
            preferred_object_store_id = self.preferred_object_store_id

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if preferred_object_store_id is not UNSET:
            field_dict["preferred_object_store_id"] = preferred_object_store_id
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_preferred_object_store_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_object_store_id = _parse_preferred_object_store_id(d.pop("preferred_object_store_id", UNSET))

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        user_update_payload = cls(
            active=active,
            preferred_object_store_id=preferred_object_store_id,
            username=username,
        )

        user_update_payload.additional_properties = d
        return user_update_payload

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
