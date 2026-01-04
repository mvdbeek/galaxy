from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.notification_variant import NotificationVariant
from ..models.personal_notification_category import PersonalNotificationCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_notification_content import MessageNotificationContent
    from ..models.new_shared_item_notification_content import NewSharedItemNotificationContent


T = TypeVar("T", bound="UserNotificationResponse")


@_attrs_define
class UserNotificationResponse:
    """A notification response specific to the user.

    Attributes:
        category (PersonalNotificationCategory): These notification categories can be opt-out by the user and will be
            displayed in the notification preferences.
        content (MessageNotificationContent | NewSharedItemNotificationContent): The content of the notification. The
            structure depends on the category.
        create_time (datetime.datetime): The time when the notification was created.
        deleted (bool): Whether the notification is marked as deleted by the user. Deleted notifications don't show up
            in the notification list.
        id (str): The encoded ID of the notification. Example: 0123456789ABCDEF.
        publication_time (datetime.datetime): The time when the notification was published. Notifications can be created
            and then published at a later time.
        source (str): The source of the notification. Represents the agent that created the notification. E.g. 'galaxy'
            or 'admin'.
        update_time (datetime.datetime): The time when the notification was last updated.
        variant (NotificationVariant): The notification variant communicates the intent or relevance of the
            notification.
        expiration_time (datetime.datetime | None | Unset): The time when the notification will expire. If not set, the
            notification will never expire. Expired notifications will be permanently deleted.
        seen_time (datetime.datetime | None | Unset): The time when the notification was seen by the user. If not set,
            the notification was not seen yet.
    """

    category: PersonalNotificationCategory
    content: MessageNotificationContent | NewSharedItemNotificationContent
    create_time: datetime.datetime
    deleted: bool
    id: str
    publication_time: datetime.datetime
    source: str
    update_time: datetime.datetime
    variant: NotificationVariant
    expiration_time: datetime.datetime | None | Unset = UNSET
    seen_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.message_notification_content import MessageNotificationContent

        category = self.category.value

        content: dict[str, Any]
        if isinstance(self.content, MessageNotificationContent):
            content = self.content.to_dict()
        else:
            content = self.content.to_dict()

        create_time = self.create_time.isoformat()

        deleted = self.deleted

        id = self.id

        publication_time = self.publication_time.isoformat()

        source = self.source

        update_time = self.update_time.isoformat()

        variant = self.variant.value

        expiration_time: None | str | Unset
        if isinstance(self.expiration_time, Unset):
            expiration_time = UNSET
        elif isinstance(self.expiration_time, datetime.datetime):
            expiration_time = self.expiration_time.isoformat()
        else:
            expiration_time = self.expiration_time

        seen_time: None | str | Unset
        if isinstance(self.seen_time, Unset):
            seen_time = UNSET
        elif isinstance(self.seen_time, datetime.datetime):
            seen_time = self.seen_time.isoformat()
        else:
            seen_time = self.seen_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "content": content,
                "create_time": create_time,
                "deleted": deleted,
                "id": id,
                "publication_time": publication_time,
                "source": source,
                "update_time": update_time,
                "variant": variant,
            }
        )
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time
        if seen_time is not UNSET:
            field_dict["seen_time"] = seen_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_notification_content import MessageNotificationContent
        from ..models.new_shared_item_notification_content import NewSharedItemNotificationContent

        d = dict(src_dict)
        category = PersonalNotificationCategory(d.pop("category"))

        def _parse_content(data: object) -> MessageNotificationContent | NewSharedItemNotificationContent:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = MessageNotificationContent.from_dict(data)

                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            content_type_1 = NewSharedItemNotificationContent.from_dict(data)

            return content_type_1

        content = _parse_content(d.pop("content"))

        create_time = isoparse(d.pop("create_time"))

        deleted = d.pop("deleted")

        id = d.pop("id")

        publication_time = isoparse(d.pop("publication_time"))

        source = d.pop("source")

        update_time = isoparse(d.pop("update_time"))

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

        def _parse_seen_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                seen_time_type_0 = isoparse(data)

                return seen_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        seen_time = _parse_seen_time(d.pop("seen_time", UNSET))

        user_notification_response = cls(
            category=category,
            content=content,
            create_time=create_time,
            deleted=deleted,
            id=id,
            publication_time=publication_time,
            source=source,
            update_time=update_time,
            variant=variant,
            expiration_time=expiration_time,
            seen_time=seen_time,
        )

        user_notification_response.additional_properties = d
        return user_notification_response

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
