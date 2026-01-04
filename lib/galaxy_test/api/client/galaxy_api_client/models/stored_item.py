from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="StoredItem")


@_attrs_define
class StoredItem:
    """
    Attributes:
        id (str):  Example: 0123456789ABCDEF.
        name (str):
        size (int):
        type_ (Literal['dataset'] | Literal['history']):
        update_time (datetime.datetime): The last time and date this item was updated.
    """

    id: str
    name: str
    size: int
    type_: Literal["dataset"] | Literal["history"]
    update_time: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        size = self.size

        type_: Literal["dataset"] | Literal["history"]
        type_ = self.type_

        update_time = self.update_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "size": size,
                "type": type_,
                "update_time": update_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        size = d.pop("size")

        def _parse_type_(data: object) -> Literal["dataset"] | Literal["history"]:
            type_type_0 = cast(Literal["history"], data)
            if type_type_0 != "history":
                raise ValueError(f"type_type_0 must match const 'history', got '{type_type_0}'")
            return type_type_0
            type_type_1 = cast(Literal["dataset"], data)
            if type_type_1 != "dataset":
                raise ValueError(f"type_type_1 must match const 'dataset', got '{type_type_1}'")
            return type_type_1

        type_ = _parse_type_(d.pop("type"))

        update_time = isoparse(d.pop("update_time"))

        stored_item = cls(
            id=id,
            name=name,
            size=size,
            type_=type_,
            update_time=update_time,
        )

        stored_item.additional_properties = d
        return stored_item

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
