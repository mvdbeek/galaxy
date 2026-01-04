from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryFolderDetails")


@_attrs_define
class LibraryFolderDetails:
    """
    Attributes:
        deleted (bool): Whether this folder is marked as deleted.
        id (str): Encoded ID of the library folder. Example: 0123456789ABCDEF.
        item_count (int): A detailed description of the library folder.
        model_class (Literal['LibraryFolder']): The name of the database model class.
        name (str): The name of the library folder.
        parent_library_id (str): Encoded ID of the Library this folder belongs to. Example: 0123456789ABCDEF.
        update_time (datetime.datetime): The last time and date this item was updated.
        description (None | str | Unset): A detailed description of the library folder. Default: ''.
        genome_build (None | str | Unset): TODO Default: '?'.
        library_path (list[str] | Unset): The list of folder names composing the path to this folder.
        parent_id (None | str | Unset): Encoded ID of the parent folder. Empty if it's the root folder.
    """

    deleted: bool
    id: str
    item_count: int
    model_class: Literal["LibraryFolder"]
    name: str
    parent_library_id: str
    update_time: datetime.datetime
    description: None | str | Unset = ""
    genome_build: None | str | Unset = "?"
    library_path: list[str] | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        id = self.id

        item_count = self.item_count

        model_class = self.model_class

        name = self.name

        parent_library_id = self.parent_library_id

        update_time = self.update_time.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        genome_build: None | str | Unset
        if isinstance(self.genome_build, Unset):
            genome_build = UNSET
        else:
            genome_build = self.genome_build

        library_path: list[str] | Unset = UNSET
        if not isinstance(self.library_path, Unset):
            library_path = self.library_path

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deleted": deleted,
                "id": id,
                "item_count": item_count,
                "model_class": model_class,
                "name": name,
                "parent_library_id": parent_library_id,
                "update_time": update_time,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if genome_build is not UNSET:
            field_dict["genome_build"] = genome_build
        if library_path is not UNSET:
            field_dict["library_path"] = library_path
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deleted = d.pop("deleted")

        id = d.pop("id")

        item_count = d.pop("item_count")

        model_class = cast(Literal["LibraryFolder"], d.pop("model_class"))
        if model_class != "LibraryFolder":
            raise ValueError(f"model_class must match const 'LibraryFolder', got '{model_class}'")

        name = d.pop("name")

        parent_library_id = d.pop("parent_library_id")

        update_time = isoparse(d.pop("update_time"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_genome_build(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        genome_build = _parse_genome_build(d.pop("genome_build", UNSET))

        library_path = cast(list[str], d.pop("library_path", UNSET))

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        library_folder_details = cls(
            deleted=deleted,
            id=id,
            item_count=item_count,
            model_class=model_class,
            name=name,
            parent_library_id=parent_library_id,
            update_time=update_time,
            description=description,
            genome_build=genome_build,
            library_path=library_path,
            parent_id=parent_id,
        )

        library_folder_details.additional_properties = d
        return library_folder_details

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
