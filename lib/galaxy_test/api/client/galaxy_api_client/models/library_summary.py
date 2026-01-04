from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LibrarySummary")


@_attrs_define
class LibrarySummary:
    """
    Attributes:
        can_user_add (bool): Whether the current user can add contents to this Library.
        can_user_manage (bool): Whether the current user can manage the Library and its contents.
        can_user_modify (bool): Whether the current user can modify this Library.
        create_time (datetime.datetime): The time and date this item was created.
        create_time_pretty (str): Nice time representation of the creation date.
        deleted (bool): Whether this Library has been deleted.
        id (str): Encoded ID of the Library. Example: 0123456789ABCDEF.
        model_class (Literal['Library']): The name of the database model class.
        name (str): The name of the Library.
        public (bool): Whether this Library has been deleted.
        root_folder_id (str): Encoded ID of the Library's base folder. Example: 0123456789ABCDEF.
        description (None | str | Unset): A detailed description of the Library. Default: ''.
        synopsis (None | str | Unset): A short text describing the contents of the Library.
    """

    can_user_add: bool
    can_user_manage: bool
    can_user_modify: bool
    create_time: datetime.datetime
    create_time_pretty: str
    deleted: bool
    id: str
    model_class: Literal["Library"]
    name: str
    public: bool
    root_folder_id: str
    description: None | str | Unset = ""
    synopsis: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_user_add = self.can_user_add

        can_user_manage = self.can_user_manage

        can_user_modify = self.can_user_modify

        create_time = self.create_time.isoformat()

        create_time_pretty = self.create_time_pretty

        deleted = self.deleted

        id = self.id

        model_class = self.model_class

        name = self.name

        public = self.public

        root_folder_id = self.root_folder_id

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
                "can_user_add": can_user_add,
                "can_user_manage": can_user_manage,
                "can_user_modify": can_user_modify,
                "create_time": create_time,
                "create_time_pretty": create_time_pretty,
                "deleted": deleted,
                "id": id,
                "model_class": model_class,
                "name": name,
                "public": public,
                "root_folder_id": root_folder_id,
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
        can_user_add = d.pop("can_user_add")

        can_user_manage = d.pop("can_user_manage")

        can_user_modify = d.pop("can_user_modify")

        create_time = isoparse(d.pop("create_time"))

        create_time_pretty = d.pop("create_time_pretty")

        deleted = d.pop("deleted")

        id = d.pop("id")

        model_class = cast(Literal["Library"], d.pop("model_class"))
        if model_class != "Library":
            raise ValueError(f"model_class must match const 'Library', got '{model_class}'")

        name = d.pop("name")

        public = d.pop("public")

        root_folder_id = d.pop("root_folder_id")

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

        library_summary = cls(
            can_user_add=can_user_add,
            can_user_manage=can_user_manage,
            can_user_modify=can_user_modify,
            create_time=create_time,
            create_time_pretty=create_time_pretty,
            deleted=deleted,
            id=id,
            model_class=model_class,
            name=name,
            public=public,
            root_folder_id=root_folder_id,
            description=description,
            synopsis=synopsis,
        )

        library_summary.additional_properties = d
        return library_summary

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
