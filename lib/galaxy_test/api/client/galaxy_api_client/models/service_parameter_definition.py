from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceParameterDefinition")


@_attrs_define
class ServiceParameterDefinition:
    """
    Attributes:
        description (str): A description of what this credential is used for.
        label (str): The human-readable label for the credential.
        name (str): The name of the credential definition.
        optional (bool): Whether this credential is optional or required.
    """

    description: str
    label: str
    name: str
    optional: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        label = self.label

        name = self.name

        optional = self.optional

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "label": label,
                "name": name,
                "optional": optional,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        label = d.pop("label")

        name = d.pop("name")

        optional = d.pop("optional")

        service_parameter_definition = cls(
            description=description,
            label=label,
            name=name,
            optional=optional,
        )

        service_parameter_definition.additional_properties = d
        return service_parameter_definition

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
