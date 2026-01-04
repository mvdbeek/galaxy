from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.configuration_tool_lineages_tool_lineages_response_200_item_additional_property import (
        ConfigurationToolLineagesToolLineagesResponse200ItemAdditionalProperty,
    )


T = TypeVar("T", bound="ConfigurationToolLineagesToolLineagesResponse200Item")


@_attrs_define
class ConfigurationToolLineagesToolLineagesResponse200Item:
    """ """

    additional_properties: dict[str, ConfigurationToolLineagesToolLineagesResponse200ItemAdditionalProperty] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configuration_tool_lineages_tool_lineages_response_200_item_additional_property import (
            ConfigurationToolLineagesToolLineagesResponse200ItemAdditionalProperty,
        )

        d = dict(src_dict)
        configuration_tool_lineages_tool_lineages_response_200_item = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ConfigurationToolLineagesToolLineagesResponse200ItemAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        configuration_tool_lineages_tool_lineages_response_200_item.additional_properties = additional_properties
        return configuration_tool_lineages_tool_lineages_response_200_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ConfigurationToolLineagesToolLineagesResponse200ItemAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: ConfigurationToolLineagesToolLineagesResponse200ItemAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
