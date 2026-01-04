from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_parameter_definition import ServiceParameterDefinition


T = TypeVar("T", bound="ServiceCredentialsDefinition")


@_attrs_define
class ServiceCredentialsDefinition:
    """
    Attributes:
        description (str): A description of the service.
        name (str): The name of the service.
        optional (bool): If true, tools can run without credentials; if false, credentials must be provided before
            execution.
        secrets (list[ServiceParameterDefinition]):
        variables (list[ServiceParameterDefinition]):
        version (str): The version of the service.
        label (None | str | Unset): A human-readable label for the service.
    """

    description: str
    name: str
    optional: bool
    secrets: list[ServiceParameterDefinition]
    variables: list[ServiceParameterDefinition]
    version: str
    label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        optional = self.optional

        secrets = []
        for secrets_item_data in self.secrets:
            secrets_item = secrets_item_data.to_dict()
            secrets.append(secrets_item)

        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()
            variables.append(variables_item)

        version = self.version

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
                "optional": optional,
                "secrets": secrets,
                "variables": variables,
                "version": version,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_parameter_definition import ServiceParameterDefinition

        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        optional = d.pop("optional")

        secrets = []
        _secrets = d.pop("secrets")
        for secrets_item_data in _secrets:
            secrets_item = ServiceParameterDefinition.from_dict(secrets_item_data)

            secrets.append(secrets_item)

        variables = []
        _variables = d.pop("variables")
        for variables_item_data in _variables:
            variables_item = ServiceParameterDefinition.from_dict(variables_item_data)

            variables.append(variables_item)

        version = d.pop("version")

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        service_credentials_definition = cls(
            description=description,
            name=name,
            optional=optional,
            secrets=secrets,
            variables=variables,
            version=version,
            label=label,
        )

        service_credentials_definition.additional_properties = d
        return service_credentials_definition

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
