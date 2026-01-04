from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteHistoryContentPayload")


@_attrs_define
class DeleteHistoryContentPayload:
    """
    Attributes:
        purge (bool | Unset): Whether to remove the dataset from storage. Datasets will only be removed from storage
            once all HDAs or LDDAs that refer to this datasets are deleted. Default: False.
        recursive (bool | Unset): When deleting a dataset collection, whether to also delete containing datasets.
            Default: False.
        stop_job (bool | Unset): Whether to stop the creating job if all the job's outputs are deleted. Default: False.
    """

    purge: bool | Unset = False
    recursive: bool | Unset = False
    stop_job: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purge = self.purge

        recursive = self.recursive

        stop_job = self.stop_job

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purge is not UNSET:
            field_dict["purge"] = purge
        if recursive is not UNSET:
            field_dict["recursive"] = recursive
        if stop_job is not UNSET:
            field_dict["stop_job"] = stop_job

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        purge = d.pop("purge", UNSET)

        recursive = d.pop("recursive", UNSET)

        stop_job = d.pop("stop_job", UNSET)

        delete_history_content_payload = cls(
            purge=purge,
            recursive=recursive,
            stop_job=stop_job,
        )

        delete_history_content_payload.additional_properties = d
        return delete_history_content_payload

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
