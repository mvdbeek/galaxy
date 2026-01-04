from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.requirement import Requirement
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tour_step import TourStep


T = TypeVar("T", bound="TourDetails")


@_attrs_define
class TourDetails:
    """
    Attributes:
        description (str): Tour description
        name (str): Name of tour
        requirements (list[Requirement]): Requirements to run the tour.
        steps (list[TourStep]): Tour steps
        tags (list[str]): Topic topic tags
        title_default (None | str | Unset): Default title for each step
    """

    description: str
    name: str
    requirements: list[Requirement]
    steps: list[TourStep]
    tags: list[str]
    title_default: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        requirements = []
        for requirements_item_data in self.requirements:
            requirements_item = requirements_item_data.value
            requirements.append(requirements_item)

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        tags = self.tags

        title_default: None | str | Unset
        if isinstance(self.title_default, Unset):
            title_default = UNSET
        else:
            title_default = self.title_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
                "requirements": requirements,
                "steps": steps,
                "tags": tags,
            }
        )
        if title_default is not UNSET:
            field_dict["title_default"] = title_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tour_step import TourStep

        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        requirements = []
        _requirements = d.pop("requirements")
        for requirements_item_data in _requirements:
            requirements_item = Requirement(requirements_item_data)

            requirements.append(requirements_item)

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = TourStep.from_dict(steps_item_data)

            steps.append(steps_item)

        tags = cast(list[str], d.pop("tags"))

        def _parse_title_default(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_default = _parse_title_default(d.pop("title_default", UNSET))

        tour_details = cls(
            description=description,
            name=name,
            requirements=requirements,
            steps=steps,
            tags=tags,
            title_default=title_default,
        )

        tour_details.additional_properties = d
        return tour_details

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
