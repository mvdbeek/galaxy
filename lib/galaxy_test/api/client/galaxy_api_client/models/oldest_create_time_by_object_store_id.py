from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="OldestCreateTimeByObjectStoreId")


@_attrs_define
class OldestCreateTimeByObjectStoreId:
    """Represents the oldest creation time of a set of datasets stored in a specific object store.

    Attributes:
        object_store_id (str): The ID of the object store.
        oldest_create_time (datetime.datetime): The oldest creation time of a set of datasets stored in this object
            store.
    """

    object_store_id: str
    oldest_create_time: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_store_id = self.object_store_id

        oldest_create_time = self.oldest_create_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_store_id": object_store_id,
                "oldest_create_time": oldest_create_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_store_id = d.pop("object_store_id")

        oldest_create_time = isoparse(d.pop("oldest_create_time"))

        oldest_create_time_by_object_store_id = cls(
            object_store_id=object_store_id,
            oldest_create_time=oldest_create_time,
        )

        oldest_create_time_by_object_store_id.additional_properties = d
        return oldest_create_time_by_object_store_id

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
