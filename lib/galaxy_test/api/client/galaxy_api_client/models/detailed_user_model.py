from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preferences import Preferences


T = TypeVar("T", bound="DetailedUserModel")


@_attrs_define
class DetailedUserModel:
    """
    Attributes:
        deleted (bool):  User is deleted
        email (str): Email of the user
        id (str): Encoded ID of the user Example: 0123456789ABCDEF.
        is_admin (bool): User is admin
        nice_total_disk_usage (str): Size of all non-purged, unique datasets of the user in a nice format.
        preferences (Preferences): Preferences of the user
        purged (bool): User is purged
        quota (str): Quota applicable to the user
        total_disk_usage (float): Size of all non-purged, unique datasets of the user in bytes.
        username (str): The name of the user.
        preferred_object_store_id (None | str | Unset): The ID of the object store that should be used to store new
            datasets in this history.
        quota_bytes (int | None | Unset): Quota applicable to the user in bytes.
        quota_percent (float | None | Unset): Percentage of the storage quota applicable to the user.
    """

    deleted: bool
    email: str
    id: str
    is_admin: bool
    nice_total_disk_usage: str
    preferences: Preferences
    purged: bool
    quota: str
    total_disk_usage: float
    username: str
    preferred_object_store_id: None | str | Unset = UNSET
    quota_bytes: int | None | Unset = UNSET
    quota_percent: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        email = self.email

        id = self.id

        is_admin = self.is_admin

        nice_total_disk_usage = self.nice_total_disk_usage

        preferences = self.preferences.to_dict()

        purged = self.purged

        quota = self.quota

        total_disk_usage = self.total_disk_usage

        username = self.username

        preferred_object_store_id: None | str | Unset
        if isinstance(self.preferred_object_store_id, Unset):
            preferred_object_store_id = UNSET
        else:
            preferred_object_store_id = self.preferred_object_store_id

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deleted": deleted,
                "email": email,
                "id": id,
                "is_admin": is_admin,
                "nice_total_disk_usage": nice_total_disk_usage,
                "preferences": preferences,
                "purged": purged,
                "quota": quota,
                "total_disk_usage": total_disk_usage,
                "username": username,
            }
        )
        if preferred_object_store_id is not UNSET:
            field_dict["preferred_object_store_id"] = preferred_object_store_id
        if quota_bytes is not UNSET:
            field_dict["quota_bytes"] = quota_bytes
        if quota_percent is not UNSET:
            field_dict["quota_percent"] = quota_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preferences import Preferences

        d = dict(src_dict)
        deleted = d.pop("deleted")

        email = d.pop("email")

        id = d.pop("id")

        is_admin = d.pop("is_admin")

        nice_total_disk_usage = d.pop("nice_total_disk_usage")

        preferences = Preferences.from_dict(d.pop("preferences"))

        purged = d.pop("purged")

        quota = d.pop("quota")

        total_disk_usage = d.pop("total_disk_usage")

        username = d.pop("username")

        def _parse_preferred_object_store_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_object_store_id = _parse_preferred_object_store_id(d.pop("preferred_object_store_id", UNSET))

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

        detailed_user_model = cls(
            deleted=deleted,
            email=email,
            id=id,
            is_admin=is_admin,
            nice_total_disk_usage=nice_total_disk_usage,
            preferences=preferences,
            purged=purged,
            quota=quota,
            total_disk_usage=total_disk_usage,
            username=username,
            preferred_object_store_id=preferred_object_store_id,
            quota_bytes=quota_bytes,
            quota_percent=quota_percent,
        )

        detailed_user_model.additional_properties = d
        return detailed_user_model

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
