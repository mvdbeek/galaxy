from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FillIdentifiers")


@_attrs_define
class FillIdentifiers:
    """
    Attributes:
        deduplication_index_from (int | Unset):  Default: 1.
        deduplication_pattern (str | Unset):  Default: '_{#}'.
        fill_inner_list_identifiers (bool | Unset):  Default: False.
    """

    deduplication_index_from: int | Unset = 1
    deduplication_pattern: str | Unset = "_{#}"
    fill_inner_list_identifiers: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deduplication_index_from = self.deduplication_index_from

        deduplication_pattern = self.deduplication_pattern

        fill_inner_list_identifiers = self.fill_inner_list_identifiers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deduplication_index_from is not UNSET:
            field_dict["deduplication_index_from"] = deduplication_index_from
        if deduplication_pattern is not UNSET:
            field_dict["deduplication_pattern"] = deduplication_pattern
        if fill_inner_list_identifiers is not UNSET:
            field_dict["fill_inner_list_identifiers"] = fill_inner_list_identifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deduplication_index_from = d.pop("deduplication_index_from", UNSET)

        deduplication_pattern = d.pop("deduplication_pattern", UNSET)

        fill_inner_list_identifiers = d.pop("fill_inner_list_identifiers", UNSET)

        fill_identifiers = cls(
            deduplication_index_from=deduplication_index_from,
            deduplication_pattern=deduplication_pattern,
            fill_inner_list_identifiers=fill_inner_list_identifiers,
        )

        fill_identifiers.additional_properties = d
        return fill_identifiers

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
