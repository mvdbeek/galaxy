from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryDestination")


@_attrs_define
class LibraryDestination:
    """
    Attributes:
        name (str): Must specify a library name
        type_ (Literal['library']):
        description (None | str | Unset): Description for library to create
        synopsis (None | str | Unset): Description for library to create
    """

    name: str
    type_: Literal["library"]
    description: None | str | Unset = UNSET
    synopsis: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        synopsis: None | str | Unset
        if isinstance(self.synopsis, Unset):
            synopsis = UNSET
        else:
            synopsis = self.synopsis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if synopsis is not UNSET:
            field_dict["synopsis"] = synopsis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = cast(Literal["library"], d.pop("type"))
        if type_ != "library":
            raise ValueError(f"type must match const 'library', got '{type_}'")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_synopsis(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        synopsis = _parse_synopsis(d.pop("synopsis", UNSET))

        library_destination = cls(
            name=name,
            type_=type_,
            description=description,
            synopsis=synopsis,
        )

        library_destination.additional_properties = d
        return library_destination

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
