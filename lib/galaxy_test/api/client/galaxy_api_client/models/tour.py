from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.requirement import Requirement

T = TypeVar("T", bound="Tour")


@_attrs_define
class Tour:
    """
    Attributes:
        description (str): Tour description
        id (str): Tour identifier
        name (str): Name of tour
        requirements (list[Requirement]): Requirements to run the tour.
        tags (list[str]): Topic topic tags
    """

    description: str
    id: str
    name: str
    requirements: list[Requirement]
    tags: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        name = self.name

        requirements = []
        for requirements_item_data in self.requirements:
            requirements_item = requirements_item_data.value
            requirements.append(requirements_item)

        tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "id": id,
                "name": name,
                "requirements": requirements,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        id = d.pop("id")

        name = d.pop("name")

        requirements = []
        _requirements = d.pop("requirements")
        for requirements_item_data in _requirements:
            requirements_item = Requirement(requirements_item_data)

            requirements.append(requirements_item)

        tags = cast(list[str], d.pop("tags"))

        tour = cls(
            description=description,
            id=id,
            name=name,
            requirements=requirements,
            tags=tags,
        )

        tour.additional_properties = d
        return tour

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
