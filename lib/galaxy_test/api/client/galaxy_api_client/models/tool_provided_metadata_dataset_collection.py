from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ToolProvidedMetadataDatasetCollection")


@_attrs_define
class ToolProvidedMetadataDatasetCollection:
    """
    Attributes:
        assign_primary_output (bool):
        directory (None | str):
        discover_via (Literal['tool_provided_metadata']):
        format_ (None | str):
        match_relative_path (bool):
        recurse (bool):
        visible (bool):
    """

    assign_primary_output: bool
    directory: None | str
    discover_via: Literal["tool_provided_metadata"]
    format_: None | str
    match_relative_path: bool
    recurse: bool
    visible: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assign_primary_output = self.assign_primary_output

        directory: None | str
        directory = self.directory

        discover_via = self.discover_via

        format_: None | str
        format_ = self.format_

        match_relative_path = self.match_relative_path

        recurse = self.recurse

        visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assign_primary_output": assign_primary_output,
                "directory": directory,
                "discover_via": discover_via,
                "format": format_,
                "match_relative_path": match_relative_path,
                "recurse": recurse,
                "visible": visible,
            }
        )

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

        discover_via = cast(Literal["tool_provided_metadata"], d.pop("discover_via"))
        if discover_via != "tool_provided_metadata":
            raise ValueError(f"discover_via must match const 'tool_provided_metadata', got '{discover_via}'")

        def _parse_format_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        format_ = _parse_format_(d.pop("format"))

        match_relative_path = d.pop("match_relative_path")

        recurse = d.pop("recurse")

        visible = d.pop("visible")

        tool_provided_metadata_dataset_collection = cls(
            assign_primary_output=assign_primary_output,
            directory=directory,
            discover_via=discover_via,
            format_=format_,
            match_relative_path=match_relative_path,
            recurse=recurse,
            visible=visible,
        )

        tool_provided_metadata_dataset_collection.additional_properties = d
        return tool_provided_metadata_dataset_collection

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
