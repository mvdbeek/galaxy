from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_pattern_dataset_collection_description_sort_comp import (
    FilePatternDatasetCollectionDescriptionSortComp,
)
from ..models.file_pattern_dataset_collection_description_sort_key import FilePatternDatasetCollectionDescriptionSortKey
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilePatternDatasetCollectionDescription")


@_attrs_define
class FilePatternDatasetCollectionDescription:
    """
    Attributes:
        assign_primary_output (bool):
        directory (None | str):
        discover_via (Literal['pattern']):
        format_ (None | str):
        match_relative_path (bool):
        pattern (str):
        recurse (bool):
        sort_comp (FilePatternDatasetCollectionDescriptionSortComp):
        sort_key (FilePatternDatasetCollectionDescriptionSortKey):
        visible (bool):
        sort_reverse (bool | Unset):  Default: False.
    """

    assign_primary_output: bool
    directory: None | str
    discover_via: Literal["pattern"]
    format_: None | str
    match_relative_path: bool
    pattern: str
    recurse: bool
    sort_comp: FilePatternDatasetCollectionDescriptionSortComp
    sort_key: FilePatternDatasetCollectionDescriptionSortKey
    visible: bool
    sort_reverse: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assign_primary_output = self.assign_primary_output

        directory: None | str
        directory = self.directory

        discover_via = self.discover_via

        format_: None | str
        format_ = self.format_

        match_relative_path = self.match_relative_path

        pattern = self.pattern

        recurse = self.recurse

        sort_comp = self.sort_comp.value

        sort_key = self.sort_key.value

        visible = self.visible

        sort_reverse = self.sort_reverse

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assign_primary_output": assign_primary_output,
                "directory": directory,
                "discover_via": discover_via,
                "format": format_,
                "match_relative_path": match_relative_path,
                "pattern": pattern,
                "recurse": recurse,
                "sort_comp": sort_comp,
                "sort_key": sort_key,
                "visible": visible,
            }
        )
        if sort_reverse is not UNSET:
            field_dict["sort_reverse"] = sort_reverse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assign_primary_output = d.pop("assign_primary_output")

        def _parse_directory(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        directory = _parse_directory(d.pop("directory"))

        discover_via = cast(Literal["pattern"], d.pop("discover_via"))
        if discover_via != "pattern":
            raise ValueError(f"discover_via must match const 'pattern', got '{discover_via}'")

        def _parse_format_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        format_ = _parse_format_(d.pop("format"))

        match_relative_path = d.pop("match_relative_path")

        pattern = d.pop("pattern")

        recurse = d.pop("recurse")

        sort_comp = FilePatternDatasetCollectionDescriptionSortComp(d.pop("sort_comp"))

        sort_key = FilePatternDatasetCollectionDescriptionSortKey(d.pop("sort_key"))

        visible = d.pop("visible")

        sort_reverse = d.pop("sort_reverse", UNSET)

        file_pattern_dataset_collection_description = cls(
            assign_primary_output=assign_primary_output,
            directory=directory,
            discover_via=discover_via,
            format_=format_,
            match_relative_path=match_relative_path,
            pattern=pattern,
            recurse=recurse,
            sort_comp=sort_comp,
            sort_key=sort_key,
            visible=visible,
            sort_reverse=sort_reverse,
        )

        file_pattern_dataset_collection_description.additional_properties = d
        return file_pattern_dataset_collection_description

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
