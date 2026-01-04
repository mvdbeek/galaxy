from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_link import ActionLink


T = TypeVar("T", bound="BroadcastNotificationContent")


@_attrs_define
class BroadcastNotificationContent:
    """
    Attributes:
        message (str): The message of the notification (supports Markdown).
        subject (str): The subject of the notification.
        action_links (list[ActionLink] | None | Unset): The optional action links (buttons) to be displayed in the
            notification.
        category (Literal['broadcast'] | Unset):  Default: 'broadcast'.
    """

    message: str
    subject: str
    action_links: list[ActionLink] | None | Unset = UNSET
    category: Literal["broadcast"] | Unset = "broadcast"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        subject = self.subject

        action_links: list[dict[str, Any]] | None | Unset
        if isinstance(self.action_links, Unset):
            action_links = UNSET
        elif isinstance(self.action_links, list):
            action_links = []
            for action_links_type_0_item_data in self.action_links:
                action_links_type_0_item = action_links_type_0_item_data.to_dict()
                action_links.append(action_links_type_0_item)

        else:
            action_links = self.action_links

        category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "subject": subject,
            }
        )
        if action_links is not UNSET:
            field_dict["action_links"] = action_links
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_link import ActionLink

        d = dict(src_dict)
        message = d.pop("message")

        subject = d.pop("subject")

        def _parse_action_links(data: object) -> list[ActionLink] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                action_links_type_0 = []
                _action_links_type_0 = data
                for action_links_type_0_item_data in _action_links_type_0:
                    action_links_type_0_item = ActionLink.from_dict(action_links_type_0_item_data)

                    action_links_type_0.append(action_links_type_0_item)

                return action_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActionLink] | None | Unset, data)

        action_links = _parse_action_links(d.pop("action_links", UNSET))

        category = cast(Literal["broadcast"] | Unset, d.pop("category", UNSET))
        if category != "broadcast" and not isinstance(category, Unset):
            raise ValueError(f"category must match const 'broadcast', got '{category}'")

        broadcast_notification_content = cls(
            message=message,
            subject=subject,
            action_links=action_links,
            category=category,
        )

        broadcast_notification_content.additional_properties = d
        return broadcast_notification_content

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
