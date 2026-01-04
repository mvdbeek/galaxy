from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_notification_update_request import UserNotificationUpdateRequest


T = TypeVar("T", bound="UserNotificationsBatchUpdateRequest")


@_attrs_define
class UserNotificationsBatchUpdateRequest:
    """A batch update request specific for user notifications.

    Attributes:
        changes (UserNotificationUpdateRequest): A notification update request specific to the user.
        notification_ids (list[str]): The list of encoded notification IDs of the notifications that should be updated.
    """

    changes: UserNotificationUpdateRequest
    notification_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changes = self.changes.to_dict()

        notification_ids = self.notification_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changes": changes,
                "notification_ids": notification_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_notification_update_request import UserNotificationUpdateRequest

        d = dict(src_dict)
        changes = UserNotificationUpdateRequest.from_dict(d.pop("changes"))

        notification_ids = cast(list[str], d.pop("notification_ids"))

        user_notifications_batch_update_request = cls(
            changes=changes,
            notification_ids=notification_ids,
        )

        user_notifications_batch_update_request.additional_properties = d
        return user_notifications_batch_update_request

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
