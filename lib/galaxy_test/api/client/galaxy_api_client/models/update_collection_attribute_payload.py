from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateCollectionAttributePayload")


@_attrs_define
class UpdateCollectionAttributePayload:
    """Contains attributes that can be updated for all elements in a dataset collection.

    Attributes:
        dbkey (str): TODO
    """

    dbkey: str

    def to_dict(self) -> dict[str, Any]:
        dbkey = self.dbkey

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dbkey": dbkey,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dbkey = d.pop("dbkey")

        update_collection_attribute_payload = cls(
            dbkey=dbkey,
        )

        return update_collection_attribute_payload
