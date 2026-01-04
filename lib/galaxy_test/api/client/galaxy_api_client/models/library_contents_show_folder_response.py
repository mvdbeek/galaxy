from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LibraryContentsShowFolderResponse")


@_attrs_define
class LibraryContentsShowFolderResponse:
    """
    Attributes:
        deleted (bool):
        description (str):
        genome_build (None | str):
        id (str):  Example: 0123456789ABCDEF.
        item_count (int):
        library_path (list[str]):
        model_class (Literal['LibraryFolder']): The name of the database model class.
        name (str):
        parent_id (None | str):
        parent_library_id (str):  Example: 0123456789ABCDEF.
        update_time (str):
    """

    deleted: bool
    description: str
    genome_build: None | str
    id: str
    item_count: int
    library_path: list[str]
    model_class: Literal["LibraryFolder"]
    name: str
    parent_id: None | str
    parent_library_id: str
    update_time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        description = self.description

        genome_build: None | str
        genome_build = self.genome_build

        id = self.id

        item_count = self.item_count

        library_path = self.library_path

        model_class = self.model_class

        name = self.name

        parent_id: None | str
        parent_id = self.parent_id

        parent_library_id = self.parent_library_id

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deleted": deleted,
                "description": description,
                "genome_build": genome_build,
                "id": id,
                "item_count": item_count,
                "library_path": library_path,
                "model_class": model_class,
                "name": name,
                "parent_id": parent_id,
                "parent_library_id": parent_library_id,
                "update_time": update_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deleted = d.pop("deleted")

        description = d.pop("description")

        def _parse_genome_build(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        genome_build = _parse_genome_build(d.pop("genome_build"))

        id = d.pop("id")

        item_count = d.pop("item_count")

        library_path = cast(list[str], d.pop("library_path"))

        model_class = cast(Literal["LibraryFolder"], d.pop("model_class"))
        if model_class != "LibraryFolder":
            raise ValueError(f"model_class must match const 'LibraryFolder', got '{model_class}'")

        name = d.pop("name")

        def _parse_parent_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_id = _parse_parent_id(d.pop("parent_id"))

        parent_library_id = d.pop("parent_library_id")

        update_time = d.pop("update_time")

        library_contents_show_folder_response = cls(
            deleted=deleted,
            description=description,
            genome_build=genome_build,
            id=id,
            item_count=item_count,
            library_path=library_path,
            model_class=model_class,
            name=name,
            parent_id=parent_id,
            parent_library_id=parent_library_id,
            update_time=update_time,
        )

        library_contents_show_folder_response.additional_properties = d
        return library_contents_show_folder_response

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
