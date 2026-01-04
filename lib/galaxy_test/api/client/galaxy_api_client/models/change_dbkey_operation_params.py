from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChangeDbkeyOperationParams")


@_attrs_define
class ChangeDbkeyOperationParams:
    """
    Attributes:
        dbkey (str):
        type_ (Literal['change_dbkey']):
    """

    dbkey: str
    type_: Literal["change_dbkey"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dbkey = self.dbkey

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dbkey": dbkey,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dbkey = d.pop("dbkey")

        type_ = cast(Literal["change_dbkey"], d.pop("type"))
        if type_ != "change_dbkey":
            raise ValueError(f"type must match const 'change_dbkey', got '{type_}'")

        change_dbkey_operation_params = cls(
            dbkey=dbkey,
            type_=type_,
        )

        change_dbkey_operation_params.additional_properties = d
        return change_dbkey_operation_params

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
