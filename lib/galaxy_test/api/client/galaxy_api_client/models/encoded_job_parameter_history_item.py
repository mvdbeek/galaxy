from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_item_source_type import DataItemSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EncodedJobParameterHistoryItem")


@_attrs_define
class EncodedJobParameterHistoryItem:
    """
    Attributes:
        id (str):  Example: 0123456789ABCDEF.
        name (str):
        src (DataItemSourceType):
        hid (int | None | Unset):
    """

    id: str
    name: str
    src: DataItemSourceType
    hid: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        src = self.src.value

        hid: int | None | Unset
        if isinstance(self.hid, Unset):
            hid = UNSET
        else:
            hid = self.hid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "src": src,
            }
        )
        if hid is not UNSET:
            field_dict["hid"] = hid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        src = DataItemSourceType(d.pop("src"))

        def _parse_hid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hid = _parse_hid(d.pop("hid", UNSET))

        encoded_job_parameter_history_item = cls(
            id=id,
            name=name,
            src=src,
            hid=hid,
        )

        encoded_job_parameter_history_item.additional_properties = d
        return encoded_job_parameter_history_item

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
