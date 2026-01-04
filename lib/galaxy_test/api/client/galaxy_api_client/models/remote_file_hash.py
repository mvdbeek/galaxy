from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.remote_file_hash_hash_function import RemoteFileHashHashFunction

T = TypeVar("T", bound="RemoteFileHash")


@_attrs_define
class RemoteFileHash:
    """
    Attributes:
        hash_function (RemoteFileHashHashFunction):
        hash_value (str):
    """

    hash_function: RemoteFileHashHashFunction
    hash_value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_function = self.hash_function.value

        hash_value = self.hash_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hash_function": hash_function,
                "hash_value": hash_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hash_function = RemoteFileHashHashFunction(d.pop("hash_function"))

        hash_value = d.pop("hash_value")

        remote_file_hash = cls(
            hash_function=hash_function,
            hash_value=hash_value,
        )

        remote_file_hash.additional_properties = d
        return remote_file_hash

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
