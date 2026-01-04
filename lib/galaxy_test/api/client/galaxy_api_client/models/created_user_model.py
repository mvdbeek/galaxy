from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatedUserModel")


@_attrs_define
class CreatedUserModel:
    """
    Attributes:
        active (bool): User is active
        deleted (bool):  User is deleted
        email (str): Email of the user
        id (str): Encoded ID of the user Example: 0123456789ABCDEF.
        last_password_change (datetime.datetime | None):
        model_class (Literal['User']): The name of the database model class.
        nice_total_disk_usage (str): Size of all non-purged, unique datasets of the user in a nice format.
        total_disk_usage (float): Size of all non-purged, unique datasets of the user in bytes.
        username (str): The name of the user.
        preferred_object_store_id (None | str | Unset): The ID of the object store that should be used to store new
            datasets in this history.
    """

    active: bool
    deleted: bool
    email: str
    id: str
    last_password_change: datetime.datetime | None
    model_class: Literal["User"]
    nice_total_disk_usage: str
    total_disk_usage: float
    username: str
    preferred_object_store_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        deleted = self.deleted

        email = self.email

        id = self.id

        last_password_change: None | str
        if isinstance(self.last_password_change, datetime.datetime):
            last_password_change = self.last_password_change.isoformat()
        else:
            last_password_change = self.last_password_change

        model_class = self.model_class

        nice_total_disk_usage = self.nice_total_disk_usage

        total_disk_usage = self.total_disk_usage

        username = self.username

        preferred_object_store_id: None | str | Unset
        if isinstance(self.preferred_object_store_id, Unset):
            preferred_object_store_id = UNSET
        else:
            preferred_object_store_id = self.preferred_object_store_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "deleted": deleted,
                "email": email,
                "id": id,
                "last_password_change": last_password_change,
                "model_class": model_class,
                "nice_total_disk_usage": nice_total_disk_usage,
                "total_disk_usage": total_disk_usage,
                "username": username,
            }
        )
        if preferred_object_store_id is not UNSET:
            field_dict["preferred_object_store_id"] = preferred_object_store_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        deleted = d.pop("deleted")

        email = d.pop("email")

        id = d.pop("id")

        def _parse_last_password_change(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_password_change_type_0 = isoparse(data)

                return last_password_change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_password_change = _parse_last_password_change(d.pop("last_password_change"))

        model_class = cast(Literal["User"], d.pop("model_class"))
        if model_class != "User":
            raise ValueError(f"model_class must match const 'User', got '{model_class}'")

        nice_total_disk_usage = d.pop("nice_total_disk_usage")

        total_disk_usage = d.pop("total_disk_usage")

        username = d.pop("username")

        def _parse_preferred_object_store_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_object_store_id = _parse_preferred_object_store_id(d.pop("preferred_object_store_id", UNSET))

        created_user_model = cls(
            active=active,
            deleted=deleted,
            email=email,
            id=id,
            last_password_change=last_password_change,
            model_class=model_class,
            nice_total_disk_usage=nice_total_disk_usage,
            total_disk_usage=total_disk_usage,
            username=username,
            preferred_object_store_id=preferred_object_store_id,
        )

        created_user_model.additional_properties = d
        return created_user_model

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
