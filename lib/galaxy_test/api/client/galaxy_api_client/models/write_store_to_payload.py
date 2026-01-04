from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_store_format import ModelStoreFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="WriteStoreToPayload")


@_attrs_define
class WriteStoreToPayload:
    """
    Attributes:
        target_uri (str): Galaxy Files URI to write mode store content to.
        include_deleted (bool | Unset): Include file contents for deleted datasets (if include_files is True). Default:
            False.
        include_files (bool | Unset): include materialized files in export when available Default: True.
        include_hidden (bool | Unset): Include file contents for hidden datasets (if include_files is True). Default:
            False.
        model_store_format (ModelStoreFormat | Unset): Available types of model stores for export.
    """

    target_uri: str
    include_deleted: bool | Unset = False
    include_files: bool | Unset = True
    include_hidden: bool | Unset = False
    model_store_format: ModelStoreFormat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_uri = self.target_uri

        include_deleted = self.include_deleted

        include_files = self.include_files

        include_hidden = self.include_hidden

        model_store_format: str | Unset = UNSET
        if not isinstance(self.model_store_format, Unset):
            model_store_format = self.model_store_format.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_uri": target_uri,
            }
        )
        if include_deleted is not UNSET:
            field_dict["include_deleted"] = include_deleted
        if include_files is not UNSET:
            field_dict["include_files"] = include_files
        if include_hidden is not UNSET:
            field_dict["include_hidden"] = include_hidden
        if model_store_format is not UNSET:
            field_dict["model_store_format"] = model_store_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_uri = d.pop("target_uri")

        include_deleted = d.pop("include_deleted", UNSET)

        include_files = d.pop("include_files", UNSET)

        include_hidden = d.pop("include_hidden", UNSET)

        _model_store_format = d.pop("model_store_format", UNSET)
        model_store_format: ModelStoreFormat | Unset
        if isinstance(_model_store_format, Unset):
            model_store_format = UNSET
        else:
            model_store_format = ModelStoreFormat(_model_store_format)

        write_store_to_payload = cls(
            target_uri=target_uri,
            include_deleted=include_deleted,
            include_files=include_files,
            include_hidden=include_hidden,
            model_store_format=model_store_format,
        )

        write_store_to_payload.additional_properties = d
        return write_store_to_payload

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
