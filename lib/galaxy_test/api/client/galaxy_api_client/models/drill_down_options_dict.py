from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DrillDownOptionsDict")


@_attrs_define
class DrillDownOptionsDict:
    """
    Attributes:
        name (None | str):
        options (list[DrillDownOptionsDict]):
        selected (bool):
        value (str):
    """

    name: None | str
    options: list[DrillDownOptionsDict]
    selected: bool
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str
        name = self.name

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        selected = self.selected

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "options": options,
                "selected": selected,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = DrillDownOptionsDict.from_dict(options_item_data)

            options.append(options_item)

        selected = d.pop("selected")

        value = d.pop("value")

        drill_down_options_dict = cls(
            name=name,
            options=options,
            selected=selected,
            value=value,
        )

        drill_down_options_dict.additional_properties = d
        return drill_down_options_dict

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
