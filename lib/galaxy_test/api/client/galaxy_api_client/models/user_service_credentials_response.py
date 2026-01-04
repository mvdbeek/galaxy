from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_credential_group_response import ServiceCredentialGroupResponse


T = TypeVar("T", bound="UserServiceCredentialsResponse")


@_attrs_define
class UserServiceCredentialsResponse:
    """
    Attributes:
        groups (list[ServiceCredentialGroupResponse]):
        id (str): The encoded ID of the user credentials. Example: 0123456789ABCDEF.
        name (str): The name of the service requiring credentials.
        source_id (str): The ID of the source (e.g., tool ID).
        source_type (Literal['tool']): The type of source (e.g., 'tool').
        source_version (str): The version of the source.
        user_id (str): The ID of the user who owns these credentials. Example: 0123456789ABCDEF.
        version (str): The version of the service.
        current_group_id (None | str | Unset): The ID of the currently active credential group.
    """

    groups: list[ServiceCredentialGroupResponse]
    id: str
    name: str
    source_id: str
    source_type: Literal["tool"]
    source_version: str
    user_id: str
    version: str
    current_group_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        id = self.id

        name = self.name

        source_id = self.source_id

        source_type = self.source_type

        source_version = self.source_version

        user_id = self.user_id

        version = self.version

        current_group_id: None | str | Unset
        if isinstance(self.current_group_id, Unset):
            current_group_id = UNSET
        else:
            current_group_id = self.current_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groups": groups,
                "id": id,
                "name": name,
                "source_id": source_id,
                "source_type": source_type,
                "source_version": source_version,
                "user_id": user_id,
                "version": version,
            }
        )
        if current_group_id is not UNSET:
            field_dict["current_group_id"] = current_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_credential_group_response import ServiceCredentialGroupResponse

        d = dict(src_dict)
        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = ServiceCredentialGroupResponse.from_dict(groups_item_data)

            groups.append(groups_item)

        id = d.pop("id")

        name = d.pop("name")

        source_id = d.pop("source_id")

        source_type = cast(Literal["tool"], d.pop("source_type"))
        if source_type != "tool":
            raise ValueError(f"source_type must match const 'tool', got '{source_type}'")

        source_version = d.pop("source_version")

        user_id = d.pop("user_id")

        version = d.pop("version")

        def _parse_current_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_group_id = _parse_current_group_id(d.pop("current_group_id", UNSET))

        user_service_credentials_response = cls(
            groups=groups,
            id=id,
            name=name,
            source_id=source_id,
            source_type=source_type,
            source_version=source_version,
            user_id=user_id,
            version=version,
            current_group_id=current_group_id,
        )

        user_service_credentials_response.additional_properties = d
        return user_service_credentials_response

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
