from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.credential_payload import CredentialPayload


T = TypeVar("T", bound="ServiceCredentialGroupPayload")


@_attrs_define
class ServiceCredentialGroupPayload:
    """
    Attributes:
        name (str): The name of the credential group (minimum 3 characters).
        secrets (list[CredentialPayload]): List of secrets for this credential group.
        variables (list[CredentialPayload]): List of variables for this credential group.
    """

    name: str
    secrets: list[CredentialPayload]
    variables: list[CredentialPayload]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        secrets = []
        for secrets_item_data in self.secrets:
            secrets_item = secrets_item_data.to_dict()
            secrets.append(secrets_item)

        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()
            variables.append(variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "secrets": secrets,
                "variables": variables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_payload import CredentialPayload

        d = dict(src_dict)
        name = d.pop("name")

        secrets = []
        _secrets = d.pop("secrets")
        for secrets_item_data in _secrets:
            secrets_item = CredentialPayload.from_dict(secrets_item_data)

            secrets.append(secrets_item)

        variables = []
        _variables = d.pop("variables")
        for variables_item_data in _variables:
            variables_item = CredentialPayload.from_dict(variables_item_data)

            variables.append(variables_item)

        service_credential_group_payload = cls(
            name=name,
            secrets=secrets,
            variables=variables,
        )

        service_credential_group_payload.additional_properties = d
        return service_credential_group_payload

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
