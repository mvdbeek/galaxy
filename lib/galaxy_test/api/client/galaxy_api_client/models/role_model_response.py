from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RoleModelResponse")


@_attrs_define
class RoleModelResponse:
    """
    Attributes:
        description (None | str):
        id (str): Encoded ID of the role Example: 0123456789ABCDEF.
        model_class (Literal['Role']): The name of the database model class.
        name (str): Name of the role
        type_ (str): Type or category of the role
        url (str): The relative URL to access this item.
    """

    description: None | str
    id: str
    model_class: Literal["Role"]
    name: str
    type_: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str
        description = self.description

        id = self.id

        model_class = self.model_class

        name = self.name

        type_ = self.type_

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "id": id,
                "model_class": model_class,
                "name": name,
                "type": type_,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        id = d.pop("id")

        model_class = cast(Literal["Role"], d.pop("model_class"))
        if model_class != "Role":
            raise ValueError(f"model_class must match const 'Role', got '{model_class}'")

        name = d.pop("name")

        type_ = d.pop("type")

        url = d.pop("url")

        role_model_response = cls(
            description=description,
            id=id,
            model_class=model_class,
            name=name,
            type_=type_,
            url=url,
        )

        role_model_response.additional_properties = d
        return role_model_response

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
