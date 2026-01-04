from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SelectCurrentGroupPayload")


@_attrs_define
class SelectCurrentGroupPayload:
    """
    Attributes:
        user_credentials_id (str): The ID of the user credentials to update. Example: 0123456789ABCDEF.
        current_group_id (None | str | Unset): The ID of the group to set as current (None to unset).
    """

    user_credentials_id: str
    current_group_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_credentials_id = self.user_credentials_id

        current_group_id: None | str | Unset
        if isinstance(self.current_group_id, Unset):
            current_group_id = UNSET
        else:
            current_group_id = self.current_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_credentials_id": user_credentials_id,
            }
        )
        if current_group_id is not UNSET:
            field_dict["current_group_id"] = current_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_credentials_id = d.pop("user_credentials_id")

        def _parse_current_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_group_id = _parse_current_group_id(d.pop("current_group_id", UNSET))

        select_current_group_payload = cls(
            user_credentials_id=user_credentials_id,
            current_group_id=current_group_id,
        )

        select_current_group_payload.additional_properties = d
        return select_current_group_payload

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
