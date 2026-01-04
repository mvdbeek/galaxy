from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.broadcast_notification_response import BroadcastNotificationResponse
    from ..models.user_notification_response import UserNotificationResponse


T = TypeVar("T", bound="NotificationStatusSummary")


@_attrs_define
class NotificationStatusSummary:
    """A summary of the notification status for a user. Contains only updates since a particular timestamp.

    Attributes:
        broadcasts (list[BroadcastNotificationResponse]): The list of updated broadcasts.
        notifications (list[UserNotificationResponse]): The list of updated notifications for the user.
        total_unread_count (int): The total number of unread notifications for the user.
    """

    broadcasts: list[BroadcastNotificationResponse]
    notifications: list[UserNotificationResponse]
    total_unread_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        broadcasts = []
        for broadcasts_item_data in self.broadcasts:
            broadcasts_item = broadcasts_item_data.to_dict()
            broadcasts.append(broadcasts_item)

        notifications = []
        for notifications_item_data in self.notifications:
            notifications_item = notifications_item_data.to_dict()
            notifications.append(notifications_item)

        total_unread_count = self.total_unread_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "broadcasts": broadcasts,
                "notifications": notifications,
                "total_unread_count": total_unread_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_notification_response import BroadcastNotificationResponse
        from ..models.user_notification_response import UserNotificationResponse

        d = dict(src_dict)
        broadcasts = []
        _broadcasts = d.pop("broadcasts")
        for broadcasts_item_data in _broadcasts:
            broadcasts_item = BroadcastNotificationResponse.from_dict(broadcasts_item_data)

            broadcasts.append(broadcasts_item)

        notifications = []
        _notifications = d.pop("notifications")
        for notifications_item_data in _notifications:
            notifications_item = UserNotificationResponse.from_dict(notifications_item_data)

            notifications.append(notifications_item)

        total_unread_count = d.pop("total_unread_count")

        notification_status_summary = cls(
            broadcasts=broadcasts,
            notifications=notifications,
            total_unread_count=total_unread_count,
        )

        notification_status_summary.additional_properties = d
        return notification_status_summary

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
