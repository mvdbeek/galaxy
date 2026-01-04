from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationRecipientsRequest")


@_attrs_define
class NotificationRecipientsRequest:
    """
    Attributes:
        group_ids (list[str] | Unset): The list of encoded group IDs of the groups that should receive the notification.
        role_ids (list[str] | Unset): The list of encoded role IDs of the roles that should receive the notification.
        user_ids (list[str] | Unset): The list of encoded user IDs of the users that should receive the notification.
    """

    group_ids: list[str] | Unset = UNSET
    role_ids: list[str] | Unset = UNSET
    user_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        role_ids: list[str] | Unset = UNSET
        if not isinstance(self.role_ids, Unset):
            role_ids = self.role_ids

        user_ids: list[str] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if role_ids is not UNSET:
            field_dict["role_ids"] = role_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_ids = cast(list[str], d.pop("group_ids", UNSET))

        role_ids = cast(list[str], d.pop("role_ids", UNSET))

        user_ids = cast(list[str], d.pop("user_ids", UNSET))

        notification_recipients_request = cls(
            group_ids=group_ids,
            role_ids=role_ids,
            user_ids=user_ids,
        )

        notification_recipients_request.additional_properties = d
        return notification_recipients_request

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
