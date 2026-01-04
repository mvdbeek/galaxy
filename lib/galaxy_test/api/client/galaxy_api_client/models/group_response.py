from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupResponse")


@_attrs_define
class GroupResponse:
    """Response schema for a group.

    Attributes:
        id (str):  Example: 0123456789ABCDEF.
        model_class (Literal['Group']): The name of the database model class.
        name (str):
        url (str):
        roles_url (None | str | Unset):
        users_url (None | str | Unset):
    """

    id: str
    model_class: Literal["Group"]
    name: str
    url: str
    roles_url: None | str | Unset = UNSET
    users_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model_class = self.model_class

        name = self.name

        url = self.url

        roles_url: None | str | Unset
        if isinstance(self.roles_url, Unset):
            roles_url = UNSET
        else:
            roles_url = self.roles_url

        users_url: None | str | Unset
        if isinstance(self.users_url, Unset):
            users_url = UNSET
        else:
            users_url = self.users_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "model_class": model_class,
                "name": name,
                "url": url,
            }
        )
        if roles_url is not UNSET:
            field_dict["roles_url"] = roles_url
        if users_url is not UNSET:
            field_dict["users_url"] = users_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        model_class = cast(Literal["Group"], d.pop("model_class"))
        if model_class != "Group":
            raise ValueError(f"model_class must match const 'Group', got '{model_class}'")

        name = d.pop("name")

        url = d.pop("url")

        def _parse_roles_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        roles_url = _parse_roles_url(d.pop("roles_url", UNSET))

        def _parse_users_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        users_url = _parse_users_url(d.pop("users_url", UNSET))

        group_response = cls(
            id=id,
            model_class=model_class,
            name=name,
            url=url,
            roles_url=roles_url,
            users_url=users_url,
        )

        group_response.additional_properties = d
        return group_response

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
