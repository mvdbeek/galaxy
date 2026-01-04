from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilesSourceSupports")


@_attrs_define
class FilesSourceSupports:
    """
    Attributes:
        pagination (bool | Unset): Whether this file source supports server-side pagination. Default: False.
        search (bool | Unset): Whether this file source supports server-side search. Default: False.
        sorting (bool | Unset): Whether this file source supports server-side sorting. Default: False.
    """

    pagination: bool | Unset = False
    search: bool | Unset = False
    sorting: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination

        search = self.search

        sorting = self.sorting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if search is not UNSET:
            field_dict["search"] = search
        if sorting is not UNSET:
            field_dict["sorting"] = sorting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pagination = d.pop("pagination", UNSET)

        search = d.pop("search", UNSET)

        sorting = d.pop("sorting", UNSET)

        files_source_supports = cls(
            pagination=pagination,
            search=search,
            sorting=sorting,
        )

        files_source_supports.additional_properties = d
        return files_source_supports

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
