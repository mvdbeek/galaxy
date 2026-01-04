from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dataset_state import DatasetState
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileLibraryFolderItem")


@_attrs_define
class FileLibraryFolderItem:
    """
    Attributes:
        can_manage (bool):
        create_time (datetime.datetime): The time and date this item was created.
        date_uploaded (datetime.datetime):
        deleted (bool):
        file_ext (str):
        file_size (str):
        id (str):  Example: 0123456789ABCDEF.
        is_private (bool):
        is_unrestricted (bool):
        ldda_id (str):  Example: 0123456789ABCDEF.
        name (str):
        raw_size (int):
        state (DatasetState):
        tags (list[str]): The collection of tags associated with an item.
        type_ (Literal['file']):
        update_time (datetime.datetime): The last time and date this item was updated.
        message (None | str | Unset):
    """

    can_manage: bool
    create_time: datetime.datetime
    date_uploaded: datetime.datetime
    deleted: bool
    file_ext: str
    file_size: str
    id: str
    is_private: bool
    is_unrestricted: bool
    ldda_id: str
    name: str
    raw_size: int
    state: DatasetState
    tags: list[str]
    type_: Literal["file"]
    update_time: datetime.datetime
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_manage = self.can_manage

        create_time = self.create_time.isoformat()

        date_uploaded = self.date_uploaded.isoformat()

        deleted = self.deleted

        file_ext = self.file_ext

        file_size = self.file_size

        id = self.id

        is_private = self.is_private

        is_unrestricted = self.is_unrestricted

        ldda_id = self.ldda_id

        name = self.name

        raw_size = self.raw_size

        state = self.state.value

        tags = self.tags

        type_ = self.type_

        update_time = self.update_time.isoformat()

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "can_manage": can_manage,
                "create_time": create_time,
                "date_uploaded": date_uploaded,
                "deleted": deleted,
                "file_ext": file_ext,
                "file_size": file_size,
                "id": id,
                "is_private": is_private,
                "is_unrestricted": is_unrestricted,
                "ldda_id": ldda_id,
                "name": name,
                "raw_size": raw_size,
                "state": state,
                "tags": tags,
                "type": type_,
                "update_time": update_time,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_manage = d.pop("can_manage")

        create_time = isoparse(d.pop("create_time"))

        date_uploaded = isoparse(d.pop("date_uploaded"))

        deleted = d.pop("deleted")

        file_ext = d.pop("file_ext")

        file_size = d.pop("file_size")

        id = d.pop("id")

        is_private = d.pop("is_private")

        is_unrestricted = d.pop("is_unrestricted")

        ldda_id = d.pop("ldda_id")

        name = d.pop("name")

        raw_size = d.pop("raw_size")

        state = DatasetState(d.pop("state"))

        tags = cast(list[str], d.pop("tags"))

        type_ = cast(Literal["file"], d.pop("type"))
        if type_ != "file":
            raise ValueError(f"type must match const 'file', got '{type_}'")

        update_time = isoparse(d.pop("update_time"))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        file_library_folder_item = cls(
            can_manage=can_manage,
            create_time=create_time,
            date_uploaded=date_uploaded,
            deleted=deleted,
            file_ext=file_ext,
            file_size=file_size,
            id=id,
            is_private=is_private,
            is_unrestricted=is_unrestricted,
            ldda_id=ldda_id,
            name=name,
            raw_size=raw_size,
            state=state,
            tags=tags,
            type_=type_,
            update_time=update_time,
            message=message,
        )

        file_library_folder_item.additional_properties = d
        return file_library_folder_item

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
