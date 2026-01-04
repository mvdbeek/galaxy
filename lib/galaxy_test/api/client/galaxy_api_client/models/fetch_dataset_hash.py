from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.fetch_dataset_hash_hash_function import FetchDatasetHashHashFunction

T = TypeVar("T", bound="FetchDatasetHash")


@_attrs_define
class FetchDatasetHash:
    """
    Attributes:
        hash_function (FetchDatasetHashHashFunction):
        hash_value (str):
    """

    hash_function: FetchDatasetHashHashFunction
    hash_value: str

    def to_dict(self) -> dict[str, Any]:
        hash_function = self.hash_function.value

        hash_value = self.hash_value

        field_dict: dict[str, Any] = {}

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
        hash_function = FetchDatasetHashHashFunction(d.pop("hash_function"))

        hash_value = d.pop("hash_value")

        fetch_dataset_hash = cls(
            hash_function=hash_function,
            hash_value=hash_value,
        )

        return fetch_dataset_hash
