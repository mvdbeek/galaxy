from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LibraryCurrentPermissions")


@_attrs_define
class LibraryCurrentPermissions:
    """
    Attributes:
        access_library_role_list (list[list[str]]): A list containing pairs of role names and corresponding encoded IDs
            which have access to the Library.
        add_library_item_role_list (list[list[str]]): A list containing pairs of role names and corresponding encoded
            IDs which can add items to the Library.
        manage_library_role_list (list[list[str]]): A list containing pairs of role names and corresponding encoded IDs
            which can manage the Library.
        modify_library_role_list (list[list[str]]): A list containing pairs of role names and corresponding encoded IDs
            which can modify the Library.
    """

    access_library_role_list: list[list[str]]
    add_library_item_role_list: list[list[str]]
    manage_library_role_list: list[list[str]]
    modify_library_role_list: list[list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_library_role_list = []
        for access_library_role_list_item_data in self.access_library_role_list:
            access_library_role_list_item = access_library_role_list_item_data

            access_library_role_list.append(access_library_role_list_item)

        add_library_item_role_list = []
        for add_library_item_role_list_item_data in self.add_library_item_role_list:
            add_library_item_role_list_item = add_library_item_role_list_item_data

            add_library_item_role_list.append(add_library_item_role_list_item)

        manage_library_role_list = []
        for manage_library_role_list_item_data in self.manage_library_role_list:
            manage_library_role_list_item = manage_library_role_list_item_data

            manage_library_role_list.append(manage_library_role_list_item)

        modify_library_role_list = []
        for modify_library_role_list_item_data in self.modify_library_role_list:
            modify_library_role_list_item = modify_library_role_list_item_data

            modify_library_role_list.append(modify_library_role_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_library_role_list": access_library_role_list,
                "add_library_item_role_list": add_library_item_role_list,
                "manage_library_role_list": manage_library_role_list,
                "modify_library_role_list": modify_library_role_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_library_role_list = []
        _access_library_role_list = d.pop("access_library_role_list")
        for access_library_role_list_item_data in _access_library_role_list:
            access_library_role_list_item = cast(list[str], access_library_role_list_item_data)

            access_library_role_list.append(access_library_role_list_item)

        add_library_item_role_list = []
        _add_library_item_role_list = d.pop("add_library_item_role_list")
        for add_library_item_role_list_item_data in _add_library_item_role_list:
            add_library_item_role_list_item = cast(list[str], add_library_item_role_list_item_data)

            add_library_item_role_list.append(add_library_item_role_list_item)

        manage_library_role_list = []
        _manage_library_role_list = d.pop("manage_library_role_list")
        for manage_library_role_list_item_data in _manage_library_role_list:
            manage_library_role_list_item = cast(list[str], manage_library_role_list_item_data)

            manage_library_role_list.append(manage_library_role_list_item)

        modify_library_role_list = []
        _modify_library_role_list = d.pop("modify_library_role_list")
        for modify_library_role_list_item_data in _modify_library_role_list:
            modify_library_role_list_item = cast(list[str], modify_library_role_list_item_data)

            modify_library_role_list.append(modify_library_role_list_item)

        library_current_permissions = cls(
            access_library_role_list=access_library_role_list,
            add_library_item_role_list=add_library_item_role_list,
            manage_library_role_list=manage_library_role_list,
            modify_library_role_list=modify_library_role_list,
        )

        library_current_permissions.additional_properties = d
        return library_current_permissions

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
