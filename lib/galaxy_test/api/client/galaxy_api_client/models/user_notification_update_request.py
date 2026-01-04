from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserNotificationUpdateRequest")


@_attrs_define
class UserNotificationUpdateRequest:
    """A notification update request specific to the user.

    Attributes:
        deleted (bool | None | Unset): Whether the notification should be marked as deleted by the user. If not set, the
            notification will not be changed.
        seen (bool | None | Unset): Whether the notification should be marked as seen by the user. If not set, the
            notification will not be changed.
    """

    deleted: bool | None | Unset = UNSET
    seen: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted: bool | None | Unset
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        else:
            deleted = self.deleted

        seen: bool | None | Unset
        if isinstance(self.seen, Unset):
            seen = UNSET
        else:
            seen = self.seen

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if seen is not UNSET:
            field_dict["seen"] = seen

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        def _parse_seen(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        seen = _parse_seen(d.pop("seen", UNSET))

        user_notification_update_request = cls(
            deleted=deleted,
            seen=seen,
        )

        user_notification_update_request.additional_properties = d
        return user_notification_update_request

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
