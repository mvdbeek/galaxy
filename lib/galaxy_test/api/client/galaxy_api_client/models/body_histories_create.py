from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyHistoriesCreate")


@_attrs_define
class BodyHistoriesCreate:
    """
    Attributes:
        all_datasets (Any | Unset):  Default: True.
        archive_file (Any | Unset):
        archive_source (Any | Unset):
        archive_type (Any | Unset):  Default: 'url'.
        history_id (Any | Unset):
        name (Any | Unset):
    """

    all_datasets: Any | Unset = True
    archive_file: Any | Unset = UNSET
    archive_source: Any | Unset = UNSET
    archive_type: Any | Unset = "url"
    history_id: Any | Unset = UNSET
    name: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_datasets = self.all_datasets

        archive_file = self.archive_file

        archive_source = self.archive_source

        archive_type = self.archive_type

        history_id = self.history_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_datasets is not UNSET:
            field_dict["all_datasets"] = all_datasets
        if archive_file is not UNSET:
            field_dict["archive_file"] = archive_file
        if archive_source is not UNSET:
            field_dict["archive_source"] = archive_source
        if archive_type is not UNSET:
            field_dict["archive_type"] = archive_type
        if history_id is not UNSET:
            field_dict["history_id"] = history_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_datasets = d.pop("all_datasets", UNSET)

        archive_file = d.pop("archive_file", UNSET)

        archive_source = d.pop("archive_source", UNSET)

        archive_type = d.pop("archive_type", UNSET)

        history_id = d.pop("history_id", UNSET)

        name = d.pop("name", UNSET)

        body_histories_create = cls(
            all_datasets=all_datasets,
            archive_file=archive_file,
            archive_source=archive_source,
            archive_type=archive_type,
            history_id=history_id,
            name=name,
        )

        body_histories_create.additional_properties = d
        return body_histories_create

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
