from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="XrefItem")


@_attrs_define
class XrefItem:
    """
    Attributes:
        access_time (datetime.datetime): Date and time the external reference was accessed
        ids (list[str]): List of reference identifiers
        name (str): Name of external reference
        namespace (str): External resource vendor prefix
    """

    access_time: datetime.datetime
    ids: list[str]
    name: str
    namespace: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_time = self.access_time.isoformat()

        ids = self.ids

        name = self.name

        namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_time": access_time,
                "ids": ids,
                "name": name,
                "namespace": namespace,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_time = isoparse(d.pop("access_time"))

        ids = cast(list[str], d.pop("ids"))

        name = d.pop("name")

        namespace = d.pop("namespace")

        xref_item = cls(
            access_time=access_time,
            ids=ids,
            name=name,
            namespace=namespace,
        )

        xref_item.additional_properties = d
        return xref_item

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
