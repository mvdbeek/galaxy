from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hash_function_name_enum import HashFunctionNameEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetHash")


@_attrs_define
class DatasetHash:
    """
    Attributes:
        hash_function (HashFunctionNameEnum): Hash function names that can be used to generate checksums for files.
        hash_value (str): The hash value.
        id (str): Encoded ID of the dataset hash. Example: 0123456789ABCDEF.
        model_class (Literal['DatasetHash']): The name of the database model class.
        extra_files_path (None | str | Unset): The path to the extra files used to generate the hash.
    """

    hash_function: HashFunctionNameEnum
    hash_value: str
    id: str
    model_class: Literal["DatasetHash"]
    extra_files_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_function = self.hash_function.value

        hash_value = self.hash_value

        id = self.id

        model_class = self.model_class

        extra_files_path: None | str | Unset
        if isinstance(self.extra_files_path, Unset):
            extra_files_path = UNSET
        else:
            extra_files_path = self.extra_files_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hash_function": hash_function,
                "hash_value": hash_value,
                "id": id,
                "model_class": model_class,
            }
        )
        if extra_files_path is not UNSET:
            field_dict["extra_files_path"] = extra_files_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hash_function = HashFunctionNameEnum(d.pop("hash_function"))

        hash_value = d.pop("hash_value")

        id = d.pop("id")

        model_class = cast(Literal["DatasetHash"], d.pop("model_class"))
        if model_class != "DatasetHash":
            raise ValueError(f"model_class must match const 'DatasetHash', got '{model_class}'")

        def _parse_extra_files_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extra_files_path = _parse_extra_files_path(d.pop("extra_files_path", UNSET))

        dataset_hash = cls(
            hash_function=hash_function,
            hash_value=hash_value,
            id=id,
            model_class=model_class,
            extra_files_path=extra_files_path,
        )

        dataset_hash.additional_properties = d
        return dataset_hash

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
