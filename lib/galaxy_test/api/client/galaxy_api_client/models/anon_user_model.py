from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnonUserModel")


@_attrs_define
class AnonUserModel:
    """
    Attributes:
        nice_total_disk_usage (str): Size of all non-purged, unique datasets of the user in a nice format.
        total_disk_usage (float): Size of all non-purged, unique datasets of the user in bytes.
        quota_percent (float | None | Unset): Percentage of the storage quota applicable to the user.
    """

    nice_total_disk_usage: str
    total_disk_usage: float
    quota_percent: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nice_total_disk_usage = self.nice_total_disk_usage

        total_disk_usage = self.total_disk_usage

        quota_percent: float | None | Unset
        if isinstance(self.quota_percent, Unset):
            quota_percent = UNSET
        else:
            quota_percent = self.quota_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nice_total_disk_usage": nice_total_disk_usage,
                "total_disk_usage": total_disk_usage,
            }
        )
        if quota_percent is not UNSET:
            field_dict["quota_percent"] = quota_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nice_total_disk_usage = d.pop("nice_total_disk_usage")

        total_disk_usage = d.pop("total_disk_usage")

        def _parse_quota_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        quota_percent = _parse_quota_percent(d.pop("quota_percent", UNSET))

        anon_user_model = cls(
            nice_total_disk_usage=nice_total_disk_usage,
            total_disk_usage=total_disk_usage,
            quota_percent=quota_percent,
        )

        anon_user_model.additional_properties = d
        return anon_user_model

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
