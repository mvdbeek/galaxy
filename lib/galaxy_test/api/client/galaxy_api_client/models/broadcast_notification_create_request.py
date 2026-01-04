from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.notification_variant import NotificationVariant
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.broadcast_notification_content import BroadcastNotificationContent


T = TypeVar("T", bound="BroadcastNotificationCreateRequest")


@_attrs_define
class BroadcastNotificationCreateRequest:
    """A notification create request specific for broadcasting.

    Attributes:
        content (BroadcastNotificationContent):
        source (str): The source of the notification. Represents the agent that created the notification. E.g. 'galaxy'
            or 'admin'.
        variant (NotificationVariant): The notification variant communicates the intent or relevance of the
            notification.
        category (Literal['broadcast'] | Unset):  Default: 'broadcast'.
        expiration_time (datetime.datetime | None | Unset): The time when the notification should expire. By default it
            will expire after 6 months. Expired notifications will be permanently deleted.
        publication_time (datetime.datetime | None | Unset): The time when the notification should be published.
            Notifications can be created and then scheduled to be published at a later time.
    """

    content: BroadcastNotificationContent
    source: str
    variant: NotificationVariant
    category: Literal["broadcast"] | Unset = "broadcast"
    expiration_time: datetime.datetime | None | Unset = UNSET
    publication_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content.to_dict()

        source = self.source

        variant = self.variant.value

        category = self.category

        expiration_time: None | str | Unset
        if isinstance(self.expiration_time, Unset):
            expiration_time = UNSET
        elif isinstance(self.expiration_time, datetime.datetime):
            expiration_time = self.expiration_time.isoformat()
        else:
            expiration_time = self.expiration_time

        publication_time: None | str | Unset
        if isinstance(self.publication_time, Unset):
            publication_time = UNSET
        elif isinstance(self.publication_time, datetime.datetime):
            publication_time = self.publication_time.isoformat()
        else:
            publication_time = self.publication_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "source": source,
                "variant": variant,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time
        if publication_time is not UNSET:
            field_dict["publication_time"] = publication_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_notification_content import BroadcastNotificationContent

        d = dict(src_dict)
        content = BroadcastNotificationContent.from_dict(d.pop("content"))

        source = d.pop("source")

        variant = NotificationVariant(d.pop("variant"))

        category = cast(Literal["broadcast"] | Unset, d.pop("category", UNSET))
        if category != "broadcast" and not isinstance(category, Unset):
            raise ValueError(f"category must match const 'broadcast', got '{category}'")

        def _parse_expiration_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_time_type_0 = isoparse(data)

                return expiration_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration_time = _parse_expiration_time(d.pop("expiration_time", UNSET))

        def _parse_publication_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publication_time_type_0 = isoparse(data)

                return publication_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        publication_time = _parse_publication_time(d.pop("publication_time", UNSET))

        broadcast_notification_create_request = cls(
            content=content,
            source=source,
            variant=variant,
            category=category,
            expiration_time=expiration_time,
            publication_time=publication_time,
        )

        broadcast_notification_create_request.additional_properties = d
        return broadcast_notification_create_request

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
