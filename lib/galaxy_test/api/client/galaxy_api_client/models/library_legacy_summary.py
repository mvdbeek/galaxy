from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryLegacySummary")


@_attrs_define
class LibraryLegacySummary:
    """
    Attributes:
        create_time (datetime.datetime): The time and date this item was created.
        deleted (bool): Whether this Library has been deleted.
        id (str): Encoded ID of the Library. Example: 0123456789ABCDEF.
        model_class (Literal['Library']): The name of the database model class.
        name (str): The name of the Library.
        root_folder_id (str): Encoded ID of the Library's base folder. Example: 0123456789ABCDEF.
        description (None | str | Unset): A detailed description of the Library. Default: ''.
        synopsis (None | str | Unset): A short text describing the contents of the Library.
    """

    create_time: datetime.datetime
    deleted: bool
    id: str
    model_class: Literal["Library"]
    name: str
    root_folder_id: str
    description: None | str | Unset = ""
    synopsis: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time = self.create_time.isoformat()

        deleted = self.deleted

        id = self.id

        model_class = self.model_class

        name = self.name

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
                "create_time": create_time,
                "deleted": deleted,
                "id": id,
                "model_class": model_class,
                "name": name,
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
        create_time = isoparse(d.pop("create_time"))

        deleted = d.pop("deleted")

        id = d.pop("id")

        model_class = cast(Literal["Library"], d.pop("model_class"))
        if model_class != "Library":
            raise ValueError(f"model_class must match const 'Library', got '{model_class}'")

        name = d.pop("name")

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

        library_legacy_summary = cls(
            create_time=create_time,
            deleted=deleted,
            id=id,
            model_class=model_class,
            name=name,
            root_folder_id=root_folder_id,
            description=description,
            synopsis=synopsis,
        )

        library_legacy_summary.additional_properties = d
        return library_legacy_summary

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
