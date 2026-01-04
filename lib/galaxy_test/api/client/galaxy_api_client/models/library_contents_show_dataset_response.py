from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LibraryContentsShowDatasetResponse")


@_attrs_define
class LibraryContentsShowDatasetResponse:
    """
    Attributes:
        created_from_basename (None | str):
        data_type (str):
        date_uploaded (str):
        file_ext (str):
        file_name (str):
        file_size (int):
        folder_id (str):  Example: 0123456789ABCDEF.
        genome_build (None | str):
        id (str):  Example: 0123456789ABCDEF.
        ldda_id (str):  Example: 0123456789ABCDEF.
        message (None | str):
        misc_blurb (None | str):
        misc_info (None | str):
        model_class (Literal['LibraryDataset']): The name of the database model class.
        name (str):
        parent_library_id (str):  Example: 0123456789ABCDEF.
        peek (None | str):
        state (str):
        tags (list[str]): The collection of tags associated with an item.
        update_time (str):
        uploaded_by (None | str):
        uuid (str):
    """

    created_from_basename: None | str
    data_type: str
    date_uploaded: str
    file_ext: str
    file_name: str
    file_size: int
    folder_id: str
    genome_build: None | str
    id: str
    ldda_id: str
    message: None | str
    misc_blurb: None | str
    misc_info: None | str
    model_class: Literal["LibraryDataset"]
    name: str
    parent_library_id: str
    peek: None | str
    state: str
    tags: list[str]
    update_time: str
    uploaded_by: None | str
    uuid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_from_basename: None | str
        created_from_basename = self.created_from_basename

        data_type = self.data_type

        date_uploaded = self.date_uploaded

        file_ext = self.file_ext

        file_name = self.file_name

        file_size = self.file_size

        folder_id = self.folder_id

        genome_build: None | str
        genome_build = self.genome_build

        id = self.id

        ldda_id = self.ldda_id

        message: None | str
        message = self.message

        misc_blurb: None | str
        misc_blurb = self.misc_blurb

        misc_info: None | str
        misc_info = self.misc_info

        model_class = self.model_class

        name = self.name

        parent_library_id = self.parent_library_id

        peek: None | str
        peek = self.peek

        state = self.state

        tags = self.tags

        update_time = self.update_time

        uploaded_by: None | str
        uploaded_by = self.uploaded_by

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_from_basename": created_from_basename,
                "data_type": data_type,
                "date_uploaded": date_uploaded,
                "file_ext": file_ext,
                "file_name": file_name,
                "file_size": file_size,
                "folder_id": folder_id,
                "genome_build": genome_build,
                "id": id,
                "ldda_id": ldda_id,
                "message": message,
                "misc_blurb": misc_blurb,
                "misc_info": misc_info,
                "model_class": model_class,
                "name": name,
                "parent_library_id": parent_library_id,
                "peek": peek,
                "state": state,
                "tags": tags,
                "update_time": update_time,
                "uploaded_by": uploaded_by,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_created_from_basename(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_from_basename = _parse_created_from_basename(d.pop("created_from_basename"))

        data_type = d.pop("data_type")

        date_uploaded = d.pop("date_uploaded")

        file_ext = d.pop("file_ext")

        file_name = d.pop("file_name")

        file_size = d.pop("file_size")

        folder_id = d.pop("folder_id")

        def _parse_genome_build(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        genome_build = _parse_genome_build(d.pop("genome_build"))

        id = d.pop("id")

        ldda_id = d.pop("ldda_id")

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        def _parse_misc_blurb(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        misc_blurb = _parse_misc_blurb(d.pop("misc_blurb"))

        def _parse_misc_info(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        misc_info = _parse_misc_info(d.pop("misc_info"))

        model_class = cast(Literal["LibraryDataset"], d.pop("model_class"))
        if model_class != "LibraryDataset":
            raise ValueError(f"model_class must match const 'LibraryDataset', got '{model_class}'")

        name = d.pop("name")

        parent_library_id = d.pop("parent_library_id")

        def _parse_peek(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        peek = _parse_peek(d.pop("peek"))

        state = d.pop("state")

        tags = cast(list[str], d.pop("tags"))

        update_time = d.pop("update_time")

        def _parse_uploaded_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        uploaded_by = _parse_uploaded_by(d.pop("uploaded_by"))

        uuid = d.pop("uuid")

        library_contents_show_dataset_response = cls(
            created_from_basename=created_from_basename,
            data_type=data_type,
            date_uploaded=date_uploaded,
            file_ext=file_ext,
            file_name=file_name,
            file_size=file_size,
            folder_id=folder_id,
            genome_build=genome_build,
            id=id,
            ldda_id=ldda_id,
            message=message,
            misc_blurb=misc_blurb,
            misc_info=misc_info,
            model_class=model_class,
            name=name,
            parent_library_id=parent_library_id,
            peek=peek,
            state=state,
            tags=tags,
            update_time=update_time,
            uploaded_by=uploaded_by,
            uuid=uuid,
        )

        library_contents_show_dataset_response.additional_properties = d
        return library_contents_show_dataset_response

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
