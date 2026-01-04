from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserQuotaUsage")


@_attrs_define
class UserQuotaUsage:
    """
    Attributes:
        total_disk_usage (float):
        quota (None | str | Unset):
        quota_bytes (int | None | Unset):
        quota_percent (float | None | Unset):
        quota_source_label (None | str | Unset):
    """

    total_disk_usage: float
    quota: None | str | Unset = UNSET
    quota_bytes: int | None | Unset = UNSET
    quota_percent: float | None | Unset = UNSET
    quota_source_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_disk_usage = self.total_disk_usage

        quota: None | str | Unset
        if isinstance(self.quota, Unset):
            quota = UNSET
        else:
            quota = self.quota

        quota_bytes: int | None | Unset
        if isinstance(self.quota_bytes, Unset):
            quota_bytes = UNSET
        else:
            quota_bytes = self.quota_bytes

        quota_percent: float | None | Unset
        if isinstance(self.quota_percent, Unset):
            quota_percent = UNSET
        else:
            quota_percent = self.quota_percent

        quota_source_label: None | str | Unset
        if isinstance(self.quota_source_label, Unset):
            quota_source_label = UNSET
        else:
            quota_source_label = self.quota_source_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_disk_usage": total_disk_usage,
            }
        )
        if quota is not UNSET:
            field_dict["quota"] = quota
        if quota_bytes is not UNSET:
            field_dict["quota_bytes"] = quota_bytes
        if quota_percent is not UNSET:
            field_dict["quota_percent"] = quota_percent
        if quota_source_label is not UNSET:
            field_dict["quota_source_label"] = quota_source_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_disk_usage = d.pop("total_disk_usage")

        def _parse_quota(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quota = _parse_quota(d.pop("quota", UNSET))

        def _parse_quota_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quota_bytes = _parse_quota_bytes(d.pop("quota_bytes", UNSET))

        def _parse_quota_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        quota_percent = _parse_quota_percent(d.pop("quota_percent", UNSET))

        def _parse_quota_source_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quota_source_label = _parse_quota_source_label(d.pop("quota_source_label", UNSET))

        user_quota_usage = cls(
            total_disk_usage=total_disk_usage,
            quota=quota,
            quota_bytes=quota_bytes,
            quota_percent=quota_percent,
            quota_source_label=quota_source_label,
        )

        user_quota_usage.additional_properties = d
        return user_quota_usage

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
