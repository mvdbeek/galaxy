from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="UserModel")


@_attrs_define
class UserModel:
    """User in a transaction context.

    Attributes:
        active (bool): User is active
        deleted (bool):  User is deleted
        email (str): Email of the user
        id (str): Encoded ID of the user Example: 0123456789ABCDEF.
        last_password_change (datetime.datetime | None):
        model_class (Literal['User']): The name of the database model class.
        username (str): The name of the user.
    """

    active: bool
    deleted: bool
    email: str
    id: str
    last_password_change: datetime.datetime | None
    model_class: Literal["User"]
    username: str
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

        username = self.username

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
                "username": username,
            }
        )

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

        username = d.pop("username")

        user_model = cls(
            active=active,
            deleted=deleted,
            email=email,
            id=id,
            last_password_change=last_password_change,
            model_class=model_class,
            username=username,
        )

        user_model.additional_properties = d
        return user_model

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
