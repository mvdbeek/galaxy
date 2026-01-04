from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserObjectstoreUsage")


@_attrs_define
class UserObjectstoreUsage:
    """
    Attributes:
        object_store_id (str):
        total_disk_usage (float):
    """

    object_store_id: str
    total_disk_usage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_store_id = self.object_store_id

        total_disk_usage = self.total_disk_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_store_id": object_store_id,
                "total_disk_usage": total_disk_usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_store_id = d.pop("object_store_id")

        total_disk_usage = d.pop("total_disk_usage")

        user_objectstore_usage = cls(
            object_store_id=object_store_id,
            total_disk_usage=total_disk_usage,
        )

        user_objectstore_usage.additional_properties = d
        return user_objectstore_usage

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
