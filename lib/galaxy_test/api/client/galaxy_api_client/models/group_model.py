from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GroupModel")


@_attrs_define
class GroupModel:
    """User group model

    Attributes:
        id (str): Encoded group ID Example: 0123456789ABCDEF.
        model_class (Literal['Group']): The name of the database model class.
        name (str): The name of the group.
    """

    id: str
    model_class: Literal["Group"]
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model_class = self.model_class

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "model_class": model_class,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        model_class = cast(Literal["Group"], d.pop("model_class"))
        if model_class != "Group":
            raise ValueError(f"model_class must match const 'Group', got '{model_class}'")

        name = d.pop("name")

        group_model = cls(
            id=id,
            model_class=model_class,
            name=name,
        )

        group_model.additional_properties = d
        return group_model

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
