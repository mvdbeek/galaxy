from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.notification_variant import NotificationVariant
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.broadcast_notification_content import BroadcastNotificationContent


T = TypeVar("T", bound="NotificationBroadcastUpdateRequest")


@_attrs_define
class NotificationBroadcastUpdateRequest:
    """A notification update request specific for broadcasting.

    Attributes:
        content (BroadcastNotificationContent | None | Unset): The content of the broadcast notification. Broadcast
            notifications are displayed prominently to all users and can contain action links to redirect the user to a
            specific page.
        expiration_time (datetime.datetime | None | Unset): The time when the notification should expire. By default it
            will expire after 6 months. Expired notifications will be permanently deleted.
        publication_time (datetime.datetime | None | Unset): The time when the notification should be published.
            Notifications can be created and then scheduled to be published at a later time.
        source (None | str | Unset): The source of the notification. Represents the agent that created the notification.
        variant (None | NotificationVariant | Unset): The variant of the notification. Used to express the importance of
            the notification.
    """

    content: BroadcastNotificationContent | None | Unset = UNSET
    expiration_time: datetime.datetime | None | Unset = UNSET
    publication_time: datetime.datetime | None | Unset = UNSET
    source: None | str | Unset = UNSET
    variant: None | NotificationVariant | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.broadcast_notification_content import BroadcastNotificationContent

        content: dict[str, Any] | None | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, BroadcastNotificationContent):
            content = self.content.to_dict()
        else:
            content = self.content

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

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        variant: None | str | Unset
        if isinstance(self.variant, Unset):
            variant = UNSET
        elif isinstance(self.variant, NotificationVariant):
            variant = self.variant.value
        else:
            variant = self.variant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time
        if publication_time is not UNSET:
            field_dict["publication_time"] = publication_time
        if source is not UNSET:
            field_dict["source"] = source
        if variant is not UNSET:
            field_dict["variant"] = variant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_notification_content import BroadcastNotificationContent

        d = dict(src_dict)

        def _parse_content(data: object) -> BroadcastNotificationContent | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = BroadcastNotificationContent.from_dict(data)

                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BroadcastNotificationContent | None | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

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

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_variant(data: object) -> None | NotificationVariant | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variant_type_0 = NotificationVariant(data)

                return variant_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NotificationVariant | Unset, data)

        variant = _parse_variant(d.pop("variant", UNSET))

        notification_broadcast_update_request = cls(
            content=content,
            expiration_time=expiration_time,
            publication_time=publication_time,
            source=source,
            variant=variant,
        )

        notification_broadcast_update_request.additional_properties = d
        return notification_broadcast_update_request

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
