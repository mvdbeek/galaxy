from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompositeFileInfo")


@_attrs_define
class CompositeFileInfo:
    """
    Attributes:
        description (None | str): Summary description of the purpouse of this file
        is_binary (bool): Whether this file is a binary file
        mimetype (None | str): The MIME type of this file
        name (str): The name of this composite file
        optional (bool):
        space_to_tab (bool):
        substitute_name_with_metadata (None | str):
        to_posix_lines (bool):
    """

    description: None | str
    is_binary: bool
    mimetype: None | str
    name: str
    optional: bool
    space_to_tab: bool
    substitute_name_with_metadata: None | str
    to_posix_lines: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str
        description = self.description

        is_binary = self.is_binary

        mimetype: None | str
        mimetype = self.mimetype

        name = self.name

        optional = self.optional

        space_to_tab = self.space_to_tab

        substitute_name_with_metadata: None | str
        substitute_name_with_metadata = self.substitute_name_with_metadata

        to_posix_lines = self.to_posix_lines

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "is_binary": is_binary,
                "mimetype": mimetype,
                "name": name,
                "optional": optional,
                "space_to_tab": space_to_tab,
                "substitute_name_with_metadata": substitute_name_with_metadata,
                "to_posix_lines": to_posix_lines,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        is_binary = d.pop("is_binary")

        def _parse_mimetype(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mimetype = _parse_mimetype(d.pop("mimetype"))

        name = d.pop("name")

        optional = d.pop("optional")

        space_to_tab = d.pop("space_to_tab")

        def _parse_substitute_name_with_metadata(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        substitute_name_with_metadata = _parse_substitute_name_with_metadata(d.pop("substitute_name_with_metadata"))

        to_posix_lines = d.pop("to_posix_lines")

        composite_file_info = cls(
            description=description,
            is_binary=is_binary,
            mimetype=mimetype,
            name=name,
            optional=optional,
            space_to_tab=space_to_tab,
            substitute_name_with_metadata=substitute_name_with_metadata,
            to_posix_lines=to_posix_lines,
        )

        composite_file_info.additional_properties = d
        return composite_file_info

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
