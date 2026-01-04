from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HistoryActiveContentCounts")


@_attrs_define
class HistoryActiveContentCounts:
    """Contains the number of active, deleted or hidden items in a History.

    Attributes:
        active (int): Number of active datasets.
        deleted (int): Number of deleted datasets.
        hidden (int): Number of hidden datasets.
    """

    active: int
    deleted: int
    hidden: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        deleted = self.deleted

        hidden = self.hidden

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "deleted": deleted,
                "hidden": hidden,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        deleted = d.pop("deleted")

        hidden = d.pop("hidden")

        history_active_content_counts = cls(
            active=active,
            deleted=deleted,
            hidden=hidden,
        )

        history_active_content_counts.additional_properties = d
        return history_active_content_counts

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
