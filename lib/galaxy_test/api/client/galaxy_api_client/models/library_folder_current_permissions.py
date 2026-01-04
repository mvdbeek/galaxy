from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LibraryFolderCurrentPermissions")


@_attrs_define
class LibraryFolderCurrentPermissions:
    """
    Attributes:
        add_library_item_role_list (list[list[str]]): A list containing pairs of role names and corresponding encoded
            IDs which can add items to the Library folder.
        manage_folder_role_list (list[list[str]]): A list containing pairs of role names and corresponding encoded IDs
            which can manage the Library folder.
        modify_folder_role_list (list[list[str]]): A list containing pairs of role names and corresponding encoded IDs
            which can modify the Library folder.
    """

    add_library_item_role_list: list[list[str]]
    manage_folder_role_list: list[list[str]]
    modify_folder_role_list: list[list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_library_item_role_list = []
        for add_library_item_role_list_item_data in self.add_library_item_role_list:
            add_library_item_role_list_item = add_library_item_role_list_item_data

            add_library_item_role_list.append(add_library_item_role_list_item)

        manage_folder_role_list = []
        for manage_folder_role_list_item_data in self.manage_folder_role_list:
            manage_folder_role_list_item = manage_folder_role_list_item_data

            manage_folder_role_list.append(manage_folder_role_list_item)

        modify_folder_role_list = []
        for modify_folder_role_list_item_data in self.modify_folder_role_list:
            modify_folder_role_list_item = modify_folder_role_list_item_data

            modify_folder_role_list.append(modify_folder_role_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "add_library_item_role_list": add_library_item_role_list,
                "manage_folder_role_list": manage_folder_role_list,
                "modify_folder_role_list": modify_folder_role_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        add_library_item_role_list = []
        _add_library_item_role_list = d.pop("add_library_item_role_list")
        for add_library_item_role_list_item_data in _add_library_item_role_list:
            add_library_item_role_list_item = cast(list[str], add_library_item_role_list_item_data)

            add_library_item_role_list.append(add_library_item_role_list_item)

        manage_folder_role_list = []
        _manage_folder_role_list = d.pop("manage_folder_role_list")
        for manage_folder_role_list_item_data in _manage_folder_role_list:
            manage_folder_role_list_item = cast(list[str], manage_folder_role_list_item_data)

            manage_folder_role_list.append(manage_folder_role_list_item)

        modify_folder_role_list = []
        _modify_folder_role_list = d.pop("modify_folder_role_list")
        for modify_folder_role_list_item_data in _modify_folder_role_list:
            modify_folder_role_list_item = cast(list[str], modify_folder_role_list_item_data)

            modify_folder_role_list.append(modify_folder_role_list_item)

        library_folder_current_permissions = cls(
            add_library_item_role_list=add_library_item_role_list,
            manage_folder_role_list=manage_folder_role_list,
            modify_folder_role_list=modify_folder_role_list,
        )

        library_folder_current_permissions.additional_properties = d
        return library_folder_current_permissions

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
