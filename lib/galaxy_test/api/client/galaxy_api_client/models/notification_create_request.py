from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.notification_create_data import NotificationCreateData
    from ..models.notification_recipients_request import NotificationRecipientsRequest


T = TypeVar("T", bound="NotificationCreateRequest")


@_attrs_define
class NotificationCreateRequest:
    """
    Attributes:
        notification (NotificationCreateData): Basic common fields for all notification create requests.
        recipients (NotificationRecipientsRequest):
    """

    notification: NotificationCreateData
    recipients: NotificationRecipientsRequest
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification = self.notification.to_dict()

        recipients = self.recipients.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notification": notification,
                "recipients": recipients,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_create_data import NotificationCreateData
        from ..models.notification_recipients_request import NotificationRecipientsRequest

        d = dict(src_dict)
        notification = NotificationCreateData.from_dict(d.pop("notification"))

        recipients = NotificationRecipientsRequest.from_dict(d.pop("recipients"))

        notification_create_request = cls(
            notification=notification,
            recipients=recipients,
        )

        notification_create_request.additional_properties = d
        return notification_create_request

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
