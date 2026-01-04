from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LibraryContentsCreateDatasetResponse")


@_attrs_define
class LibraryContentsCreateDatasetResponse:
    """
    Attributes:
        created_from_basename (None | str):
        data_type (str):
        deleted (bool):
        file_ext (str):
        file_name (str):
        file_size (int):
        genome_build (str):
        hda_ldda (str):
        id (str):
        library_dataset_id (str):
        misc_blurb (None | str):
        misc_info (None | str):
        model_class (Literal['LibraryDatasetDatasetAssociation']): The name of the database model class.
        name (str):
        parent_library_id (str):
        state (str):
        update_time (str):
        uuid (str):
        visible (bool):
    """

    created_from_basename: None | str
    data_type: str
    deleted: bool
    file_ext: str
    file_name: str
    file_size: int
    genome_build: str
    hda_ldda: str
    id: str
    library_dataset_id: str
    misc_blurb: None | str
    misc_info: None | str
    model_class: Literal["LibraryDatasetDatasetAssociation"]
    name: str
    parent_library_id: str
    state: str
    update_time: str
    uuid: str
    visible: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_from_basename: None | str
        created_from_basename = self.created_from_basename

        data_type = self.data_type

        deleted = self.deleted

        file_ext = self.file_ext

        file_name = self.file_name

        file_size = self.file_size

        genome_build = self.genome_build

        hda_ldda = self.hda_ldda

        id = self.id

        library_dataset_id = self.library_dataset_id

        misc_blurb: None | str
        misc_blurb = self.misc_blurb

        misc_info: None | str
        misc_info = self.misc_info

        model_class = self.model_class

        name = self.name

        parent_library_id = self.parent_library_id

        state = self.state

        update_time = self.update_time

        uuid = self.uuid

        visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_from_basename": created_from_basename,
                "data_type": data_type,
                "deleted": deleted,
                "file_ext": file_ext,
                "file_name": file_name,
                "file_size": file_size,
                "genome_build": genome_build,
                "hda_ldda": hda_ldda,
                "id": id,
                "library_dataset_id": library_dataset_id,
                "misc_blurb": misc_blurb,
                "misc_info": misc_info,
                "model_class": model_class,
                "name": name,
                "parent_library_id": parent_library_id,
                "state": state,
                "update_time": update_time,
                "uuid": uuid,
                "visible": visible,
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

        deleted = d.pop("deleted")

        file_ext = d.pop("file_ext")

        file_name = d.pop("file_name")

        file_size = d.pop("file_size")

        genome_build = d.pop("genome_build")

        hda_ldda = d.pop("hda_ldda")

        id = d.pop("id")

        library_dataset_id = d.pop("library_dataset_id")

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

        model_class = cast(Literal["LibraryDatasetDatasetAssociation"], d.pop("model_class"))
        if model_class != "LibraryDatasetDatasetAssociation":
            raise ValueError(f"model_class must match const 'LibraryDatasetDatasetAssociation', got '{model_class}'")

        name = d.pop("name")

        parent_library_id = d.pop("parent_library_id")

        state = d.pop("state")

        update_time = d.pop("update_time")

        uuid = d.pop("uuid")

        visible = d.pop("visible")

        library_contents_create_dataset_response = cls(
            created_from_basename=created_from_basename,
            data_type=data_type,
            deleted=deleted,
            file_ext=file_ext,
            file_name=file_name,
            file_size=file_size,
            genome_build=genome_build,
            hda_ldda=hda_ldda,
            id=id,
            library_dataset_id=library_dataset_id,
            misc_blurb=misc_blurb,
            misc_info=misc_info,
            model_class=model_class,
            name=name,
            parent_library_id=parent_library_id,
            state=state,
            update_time=update_time,
            uuid=uuid,
            visible=visible,
        )

        library_contents_create_dataset_response.additional_properties = d
        return library_contents_create_dataset_response

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
