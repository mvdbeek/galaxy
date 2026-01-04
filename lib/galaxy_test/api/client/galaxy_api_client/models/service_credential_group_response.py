from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.secret_response import SecretResponse
    from ..models.variable_response import VariableResponse


T = TypeVar("T", bound="ServiceCredentialGroupResponse")


@_attrs_define
class ServiceCredentialGroupResponse:
    """
    Attributes:
        id (str): Encoded ID of the credential group. Example: 0123456789ABCDEF.
        name (str): The name of the credential group.
        secrets (list[SecretResponse]):
        update_time (datetime.datetime): The last time the credential group was updated.
        variables (list[VariableResponse]):
    """

    id: str
    name: str
    secrets: list[SecretResponse]
    update_time: datetime.datetime
    variables: list[VariableResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        secrets = []
        for secrets_item_data in self.secrets:
            secrets_item = secrets_item_data.to_dict()
            secrets.append(secrets_item)

        update_time = self.update_time.isoformat()

        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()
            variables.append(variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "secrets": secrets,
                "update_time": update_time,
                "variables": variables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.secret_response import SecretResponse
        from ..models.variable_response import VariableResponse

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        secrets = []
        _secrets = d.pop("secrets")
        for secrets_item_data in _secrets:
            secrets_item = SecretResponse.from_dict(secrets_item_data)

            secrets.append(secrets_item)

        update_time = isoparse(d.pop("update_time"))

        variables = []
        _variables = d.pop("variables")
        for variables_item_data in _variables:
            variables_item = VariableResponse.from_dict(variables_item_data)

            variables.append(variables_item)

        service_credential_group_response = cls(
            id=id,
            name=name,
            secrets=secrets,
            update_time=update_time,
            variables=variables,
        )

        service_credential_group_response.additional_properties = d
        return service_credential_group_response

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
