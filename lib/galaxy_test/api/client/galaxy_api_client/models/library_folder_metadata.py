from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LibraryFolderMetadata")


@_attrs_define
class LibraryFolderMetadata:
    """
    Attributes:
        can_add_library_item (bool):
        can_modify_folder (bool):
        folder_description (str):
        folder_name (str):
        full_path (list[list[str]]):
        parent_library_id (str):  Example: 0123456789ABCDEF.
        total_rows (int):
    """

    can_add_library_item: bool
    can_modify_folder: bool
    folder_description: str
    folder_name: str
    full_path: list[list[str]]
    parent_library_id: str
    total_rows: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_add_library_item = self.can_add_library_item

        can_modify_folder = self.can_modify_folder

        folder_description = self.folder_description

        folder_name = self.folder_name

        full_path = []
        for full_path_item_data in self.full_path:
            full_path_item = []
            for full_path_item_item_data in full_path_item_data:
                full_path_item_item: str
                full_path_item_item = full_path_item_item_data
                full_path_item.append(full_path_item_item)

            full_path.append(full_path_item)

        parent_library_id = self.parent_library_id

        total_rows = self.total_rows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "can_add_library_item": can_add_library_item,
                "can_modify_folder": can_modify_folder,
                "folder_description": folder_description,
                "folder_name": folder_name,
                "full_path": full_path,
                "parent_library_id": parent_library_id,
                "total_rows": total_rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_add_library_item = d.pop("can_add_library_item")

        can_modify_folder = d.pop("can_modify_folder")

        folder_description = d.pop("folder_description")

        folder_name = d.pop("folder_name")

        full_path = []
        _full_path = d.pop("full_path")
        for full_path_item_data in _full_path:
            full_path_item = []
            _full_path_item = full_path_item_data
            for full_path_item_item_data in _full_path_item:

                def _parse_full_path_item_item(data: object) -> str:
                    return cast(str, data)

                full_path_item_item = _parse_full_path_item_item(full_path_item_item_data)

                full_path_item.append(full_path_item_item)

            full_path.append(full_path_item)

        parent_library_id = d.pop("parent_library_id")

        total_rows = d.pop("total_rows")

        library_folder_metadata = cls(
            can_add_library_item=can_add_library_item,
            can_modify_folder=can_modify_folder,
            folder_description=folder_description,
            folder_name=folder_name,
            full_path=full_path,
            parent_library_id=parent_library_id,
            total_rows=total_rows,
        )

        library_folder_metadata.additional_properties = d
        return library_folder_metadata

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
