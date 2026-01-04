from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.src import Src
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtraFiles")


@_attrs_define
class ExtraFiles:
    """
    Attributes:
        src (Src):
        fuzzy_root (bool | None | Unset): Prevent Galaxy from checking for a single file in a directory and re-
            interpreting the archive Default: True.
        items_from (None | str | Unset):
    """

    src: Src
    fuzzy_root: bool | None | Unset = True
    items_from: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src = self.src.value

        fuzzy_root: bool | None | Unset
        if isinstance(self.fuzzy_root, Unset):
            fuzzy_root = UNSET
        else:
            fuzzy_root = self.fuzzy_root

        items_from: None | str | Unset
        if isinstance(self.items_from, Unset):
            items_from = UNSET
        else:
            items_from = self.items_from

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src": src,
            }
        )
        if fuzzy_root is not UNSET:
            field_dict["fuzzy_root"] = fuzzy_root
        if items_from is not UNSET:
            field_dict["items_from"] = items_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        src = Src(d.pop("src"))

        def _parse_fuzzy_root(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        fuzzy_root = _parse_fuzzy_root(d.pop("fuzzy_root", UNSET))

        def _parse_items_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        items_from = _parse_items_from(d.pop("items_from", UNSET))

        extra_files = cls(
            src=src,
            fuzzy_root=fuzzy_root,
            items_from=items_from,
        )

        extra_files.additional_properties = d
        return extra_files

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
