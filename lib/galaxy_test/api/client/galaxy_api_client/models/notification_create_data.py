from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.mandatory_notification_category import MandatoryNotificationCategory
from ..models.notification_variant import NotificationVariant
from ..models.personal_notification_category import PersonalNotificationCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.broadcast_notification_content import BroadcastNotificationContent
    from ..models.message_notification_content import MessageNotificationContent
    from ..models.new_shared_item_notification_content import NewSharedItemNotificationContent


T = TypeVar("T", bound="NotificationCreateData")


@_attrs_define
class NotificationCreateData:
    """Basic common fields for all notification create requests.

    Attributes:
        category (MandatoryNotificationCategory | PersonalNotificationCategory): The category of the notification.
            Represents the type of the notification. E.g. 'message' or 'new_shared_item'.
        content (BroadcastNotificationContent | MessageNotificationContent | NewSharedItemNotificationContent): The
            content of the notification. The structure depends on the category.
        source (str): The source of the notification. Represents the agent that created the notification. E.g. 'galaxy'
            or 'admin'.
        variant (NotificationVariant): The notification variant communicates the intent or relevance of the
            notification.
        expiration_time (datetime.datetime | None | Unset): The time when the notification should expire. By default it
            will expire after 6 months. Expired notifications will be permanently deleted.
        publication_time (datetime.datetime | None | Unset): The time when the notification should be published.
            Notifications can be created and then scheduled to be published at a later time.
    """

    category: MandatoryNotificationCategory | PersonalNotificationCategory
    content: BroadcastNotificationContent | MessageNotificationContent | NewSharedItemNotificationContent
    source: str
    variant: NotificationVariant
    expiration_time: datetime.datetime | None | Unset = UNSET
    publication_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.message_notification_content import MessageNotificationContent
        from ..models.new_shared_item_notification_content import NewSharedItemNotificationContent

        category: str
        if isinstance(self.category, MandatoryNotificationCategory):
            category = self.category.value
        else:
            category = self.category.value

        content: dict[str, Any]
        if isinstance(self.content, MessageNotificationContent):
            content = self.content.to_dict()
        elif isinstance(self.content, NewSharedItemNotificationContent):
            content = self.content.to_dict()
        else:
            content = self.content.to_dict()

        source = self.source

        variant = self.variant.value

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
                "category": category,
                "content": content,
                "source": source,
                "variant": variant,
            }
        )
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time
        if publication_time is not UNSET:
            field_dict["publication_time"] = publication_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.broadcast_notification_content import BroadcastNotificationContent
        from ..models.message_notification_content import MessageNotificationContent
        from ..models.new_shared_item_notification_content import NewSharedItemNotificationContent

        d = dict(src_dict)

        def _parse_category(data: object) -> MandatoryNotificationCategory | PersonalNotificationCategory:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_0 = MandatoryNotificationCategory(data)

                return category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            category_type_1 = PersonalNotificationCategory(data)

            return category_type_1

        category = _parse_category(d.pop("category"))

        def _parse_content(
            data: object,
        ) -> BroadcastNotificationContent | MessageNotificationContent | NewSharedItemNotificationContent:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = MessageNotificationContent.from_dict(data)

                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = NewSharedItemNotificationContent.from_dict(data)

                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            content_type_2 = BroadcastNotificationContent.from_dict(data)

            return content_type_2

        content = _parse_content(d.pop("content"))

        source = d.pop("source")

        variant = NotificationVariant(d.pop("variant"))

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

        notification_create_data = cls(
            category=category,
            content=content,
            source=source,
            variant=variant,
            expiration_time=expiration_time,
            publication_time=publication_time,
        )

        notification_create_data.additional_properties = d
        return notification_create_data

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
