from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FolderLibraryFolderItem")


@_attrs_define
class FolderLibraryFolderItem:
    """
    Attributes:
        can_manage (bool):
        can_modify (bool):
        create_time (datetime.datetime): The time and date this item was created.
        deleted (bool):
        id (str):  Example: 0123456789ABCDEF.
        name (str):
        type_ (Literal['folder']):
        update_time (datetime.datetime): The last time and date this item was updated.
        description (None | str | Unset): A detailed description of the library folder. Default: ''.
    """

    can_manage: bool
    can_modify: bool
    create_time: datetime.datetime
    deleted: bool
    id: str
    name: str
    type_: Literal["folder"]
    update_time: datetime.datetime
    description: None | str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_manage = self.can_manage

        can_modify = self.can_modify

        create_time = self.create_time.isoformat()

        deleted = self.deleted

        id = self.id

        name = self.name

        type_ = self.type_

        update_time = self.update_time.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "can_manage": can_manage,
                "can_modify": can_modify,
                "create_time": create_time,
                "deleted": deleted,
                "id": id,
                "name": name,
                "type": type_,
                "update_time": update_time,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_manage = d.pop("can_manage")

        can_modify = d.pop("can_modify")

        create_time = isoparse(d.pop("create_time"))

        deleted = d.pop("deleted")

        id = d.pop("id")

        name = d.pop("name")

        type_ = cast(Literal["folder"], d.pop("type"))
        if type_ != "folder":
            raise ValueError(f"type must match const 'folder', got '{type_}'")

        update_time = isoparse(d.pop("update_time"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        folder_library_folder_item = cls(
            can_manage=can_manage,
            can_modify=can_modify,
            create_time=create_time,
            deleted=deleted,
            id=id,
            name=name,
            type_=type_,
            update_time=update_time,
            description=description,
        )

        folder_library_folder_item.additional_properties = d
        return folder_library_folder_item

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
