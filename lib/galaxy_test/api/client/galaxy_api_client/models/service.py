from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization import Organization
    from ..models.service_type import ServiceType


T = TypeVar("T", bound="Service")


@_attrs_define
class Service:
    """
    Attributes:
        id (str): Unique ID of this service. Reverse domain name notation is recommended, though not required. The
            identifier should attempt to be globally unique so it can be used in downstream aggregator services e.g. Service
            Registry.
        name (str): Name of this service. Should be human readable.
        organization (Organization):
        type_ (ServiceType):
        version (str): Version of the service being described. Semantic versioning is recommended, but other
            identifiers, such as dates or commit hashes, are also allowed. The version should be changed whenever the
            service is updated.
        contact_url (None | str | Unset): URL of the contact for the provider of this service, e.g. a link to a contact
            form (RFC 3986 format), or an email (RFC 2368 format).
        created_at (datetime.datetime | None | Unset): Timestamp describing when the service was first deployed and
            available (RFC 3339 format)
        description (None | str | Unset): Description of the service. Should be human readable and provide information
            about the service.
        documentation_url (None | str | Unset): URL of the documentation of this service (RFC 3986 format). This should
            help someone learn how to use your service, including any specifics required to access data, e.g.
            authentication.
        environment (None | str | Unset): Environment the service is running in. Use this to distinguish between
            production, development and testing/staging deployments. Suggested values are prod, test, dev, staging. However
            this is advised and not enforced.
        updated_at (datetime.datetime | None | Unset): Timestamp describing when the service was last updated (RFC 3339
            format)
    """

    id: str
    name: str
    organization: Organization
    type_: ServiceType
    version: str
    contact_url: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    documentation_url: None | str | Unset = UNSET
    environment: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        organization = self.organization.to_dict()

        type_ = self.type_.to_dict()

        version = self.version

        contact_url: None | str | Unset
        if isinstance(self.contact_url, Unset):
            contact_url = UNSET
        else:
            contact_url = self.contact_url

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        documentation_url: None | str | Unset
        if isinstance(self.documentation_url, Unset):
            documentation_url = UNSET
        else:
            documentation_url = self.documentation_url

        environment: None | str | Unset
        if isinstance(self.environment, Unset):
            environment = UNSET
        else:
            environment = self.environment

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "organization": organization,
                "type": type_,
                "version": version,
            }
        )
        if contact_url is not UNSET:
            field_dict["contactUrl"] = contact_url
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if documentation_url is not UNSET:
            field_dict["documentationUrl"] = documentation_url
        if environment is not UNSET:
            field_dict["environment"] = environment
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization import Organization
        from ..models.service_type import ServiceType

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        organization = Organization.from_dict(d.pop("organization"))

        type_ = ServiceType.from_dict(d.pop("type"))

        version = d.pop("version")

        def _parse_contact_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_url = _parse_contact_url(d.pop("contactUrl", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_documentation_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        documentation_url = _parse_documentation_url(d.pop("documentationUrl", UNSET))

        def _parse_environment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment = _parse_environment(d.pop("environment", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        service = cls(
            id=id,
            name=name,
            organization=organization,
            type_=type_,
            version=version,
            contact_url=contact_url,
            created_at=created_at,
            description=description,
            documentation_url=documentation_url,
            environment=environment,
            updated_at=updated_at,
        )

        service.additional_properties = d
        return service

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
