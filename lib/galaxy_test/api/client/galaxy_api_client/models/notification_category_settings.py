from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_channel_settings import NotificationChannelSettings


T = TypeVar("T", bound="NotificationCategorySettings")


@_attrs_define
class NotificationCategorySettings:
    """The settings for a notification category.

    Attributes:
        channels (NotificationChannelSettings | Unset): The settings for each channel of a notification category.
        enabled (bool | Unset): Whether the user wants to receive notifications for this category. Default: True.
    """

    channels: NotificationChannelSettings | Unset = UNSET
    enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels.to_dict()

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_channel_settings import NotificationChannelSettings

        d = dict(src_dict)
        _channels = d.pop("channels", UNSET)
        channels: NotificationChannelSettings | Unset
        if isinstance(_channels, Unset):
            channels = UNSET
        else:
            channels = NotificationChannelSettings.from_dict(_channels)

        enabled = d.pop("enabled", UNSET)

        notification_category_settings = cls(
            channels=channels,
            enabled=enabled,
        )

        notification_category_settings.additional_properties = d
        return notification_category_settings

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
