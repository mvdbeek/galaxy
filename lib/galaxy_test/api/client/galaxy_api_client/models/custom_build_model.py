from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomBuildModel")


@_attrs_define
class CustomBuildModel:
    """
    Attributes:
        id (str): The ID of the custom build.
        len_ (str): The primary id of the len file. Example: 0123456789ABCDEF.
        name (str): The name of the custom build.
        count (None | str | Unset): The number of chromosomes/contigs.
        fasta (None | str | Unset): The primary id of the fasta file from a history.
        linecount (None | str | Unset): The primary id of a linecount dataset.
    """

    id: str
    len_: str
    name: str
    count: None | str | Unset = UNSET
    fasta: None | str | Unset = UNSET
    linecount: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        len_ = self.len_

        name = self.name

        count: None | str | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        fasta: None | str | Unset
        if isinstance(self.fasta, Unset):
            fasta = UNSET
        else:
            fasta = self.fasta

        linecount: None | str | Unset
        if isinstance(self.linecount, Unset):
            linecount = UNSET
        else:
            linecount = self.linecount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "len": len_,
                "name": name,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if fasta is not UNSET:
            field_dict["fasta"] = fasta
        if linecount is not UNSET:
            field_dict["linecount"] = linecount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        len_ = d.pop("len")

        name = d.pop("name")

        def _parse_count(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        def _parse_fasta(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fasta = _parse_fasta(d.pop("fasta", UNSET))

        def _parse_linecount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linecount = _parse_linecount(d.pop("linecount", UNSET))

        custom_build_model = cls(
            id=id,
            len_=len_,
            name=name,
            count=count,
            fasta=fasta,
            linecount=linecount,
        )

        custom_build_model.additional_properties = d
        return custom_build_model

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
