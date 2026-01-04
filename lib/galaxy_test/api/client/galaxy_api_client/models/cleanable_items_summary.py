from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CleanableItemsSummary")


@_attrs_define
class CleanableItemsSummary:
    """
    Attributes:
        total_items (int): The total number of items that could be purged.
        total_size (int): The total size in bytes that can be recovered by purging all the items.
    """

    total_items: int
    total_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_items = self.total_items

        total_size = self.total_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_items": total_items,
                "total_size": total_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_items = d.pop("total_items")

        total_size = d.pop("total_size")

        cleanable_items_summary = cls(
            total_items=total_items,
            total_size=total_size,
        )

        cleanable_items_summary.additional_properties = d
        return cleanable_items_summary

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
