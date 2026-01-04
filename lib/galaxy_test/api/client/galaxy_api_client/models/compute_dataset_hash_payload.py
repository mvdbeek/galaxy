from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hash_function_name_enum import HashFunctionNameEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputeDatasetHashPayload")


@_attrs_define
class ComputeDatasetHashPayload:
    """
    Attributes:
        extra_files_path (None | str | Unset): If set, extra files path to compute a hash for.
        hash_function (HashFunctionNameEnum | None | Unset): Hash function name to use to compute dataset hashes.
            Default: HashFunctionNameEnum.MD5.
    """

    extra_files_path: None | str | Unset = UNSET
    hash_function: HashFunctionNameEnum | None | Unset = HashFunctionNameEnum.MD5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extra_files_path: None | str | Unset
        if isinstance(self.extra_files_path, Unset):
            extra_files_path = UNSET
        else:
            extra_files_path = self.extra_files_path

        hash_function: None | str | Unset
        if isinstance(self.hash_function, Unset):
            hash_function = UNSET
        elif isinstance(self.hash_function, HashFunctionNameEnum):
            hash_function = self.hash_function.value
        else:
            hash_function = self.hash_function

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extra_files_path is not UNSET:
            field_dict["extra_files_path"] = extra_files_path
        if hash_function is not UNSET:
            field_dict["hash_function"] = hash_function

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_extra_files_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extra_files_path = _parse_extra_files_path(d.pop("extra_files_path", UNSET))

        def _parse_hash_function(data: object) -> HashFunctionNameEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hash_function_type_0 = HashFunctionNameEnum(data)

                return hash_function_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HashFunctionNameEnum | None | Unset, data)

        hash_function = _parse_hash_function(d.pop("hash_function", UNSET))

        compute_dataset_hash_payload = cls(
            extra_files_path=extra_files_path,
            hash_function=hash_function,
        )

        compute_dataset_hash_payload.additional_properties = d
        return compute_dataset_hash_payload

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
