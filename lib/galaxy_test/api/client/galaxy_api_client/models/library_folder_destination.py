from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LibraryFolderDestination")


@_attrs_define
class LibraryFolderDestination:
    """
    Attributes:
        library_folder_id (str):  Example: 0123456789ABCDEF.
        type_ (Literal['library_folder']):
    """

    library_folder_id: str
    type_: Literal["library_folder"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        library_folder_id = self.library_folder_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "library_folder_id": library_folder_id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        library_folder_id = d.pop("library_folder_id")

        type_ = cast(Literal["library_folder"], d.pop("type"))
        if type_ != "library_folder":
            raise ValueError(f"type must match const 'library_folder', got '{type_}'")

        library_folder_destination = cls(
            library_folder_id=library_folder_id,
            type_=type_,
        )

        library_folder_destination.additional_properties = d
        return library_folder_destination

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
