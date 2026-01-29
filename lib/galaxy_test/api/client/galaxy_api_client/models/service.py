from dataclasses import dataclass

from .galaxy_schema_drs_organization import GalaxySchemaDrsOrganization
from .service_contact_url import ServiceContactUrl
from .service_created_at import ServiceCreatedAt
from .service_description import ServiceDescription
from .service_documentation_url import ServiceDocumentationUrl
from .service_environment import ServiceEnvironment
from .service_type import ServiceType
from .service_updated_at import ServiceUpdatedAt

__all__ = ["Service"]


@dataclass
class Service:
    """
    Service dataclass

    Args:
        id_ (str)                : Unique ID of this service. Reverse domain name notation
                                   is recommended, though not required. The identifier
                                   should attempt to be globally unique so it can be used in
                                   downstream aggregator services e.g. Service Registry.
                                   (maps from 'id')
        name (str)               : Name of this service. Should be human readable.
        organization (GalaxySchemaDrsOrganization)
                                 :
        type_ (ServiceType)      : Maps from 'type'
        version (str)            : Version of the service being described. Semantic
                                   versioning is recommended, but other identifiers, such as
                                   dates or commit hashes, are also allowed. The version
                                   should be changed whenever the service is updated.
        contact_url (ServiceContactUrl | None)
                                 : URL of the contact for the provider of this service, e.g.
                                   a link to a contact form (RFC 3986 format), or an email
                                   (RFC 2368 format). (maps from 'contactUrl')
        created_at (ServiceCreatedAt | None)
                                 : Timestamp describing when the service was first deployed
                                   and available (RFC 3339 format) (maps from 'createdAt')
        description (ServiceDescription | None)
                                 : Description of the service. Should be human readable and
                                   provide information about the service.
        documentation_url (ServiceDocumentationUrl | None)
                                 : URL of the documentation of this service (RFC 3986
                                   format). This should help someone learn how to use your
                                   service, including any specifics required to access data,
                                   e.g. authentication. (maps from 'documentationUrl')
        environment (ServiceEnvironment | None)
                                 : Environment the service is running in. Use this to
                                   distinguish between production, development and
                                   testing/staging deployments. Suggested values are prod,
                                   test, dev, staging. However this is advised and not
                                   enforced.
        updated_at (ServiceUpdatedAt | None)
                                 : Timestamp describing when the service was last updated
                                   (RFC 3339 format) (maps from 'updatedAt')
    """

    id_: str  # Unique ID of this service. Reverse domain name notation is recommended, though not required. The identifier should attempt to be globally unique so it can be used in downstream aggregator services e.g. Service Registry. (maps from 'id')
    name: str  # Name of this service. Should be human readable.
    organization: GalaxySchemaDrsOrganization
    type_: ServiceType  # Maps from 'type'
    version: str  # Version of the service being described. Semantic versioning is recommended, but other identifiers, such as dates or commit hashes, are also allowed. The version should be changed whenever the service is updated.
    contact_url: ServiceContactUrl | None = (
        None  # URL of the contact for the provider of this service, e.g. a link to a contact form (RFC 3986 format), or an email (RFC 2368 format). (maps from 'contactUrl')
    )
    created_at: ServiceCreatedAt | None = (
        None  # Timestamp describing when the service was first deployed and available (RFC 3339 format) (maps from 'createdAt')
    )
    description: ServiceDescription | None = (
        None  # Description of the service. Should be human readable and provide information about the service.
    )
    documentation_url: ServiceDocumentationUrl | None = (
        None  # URL of the documentation of this service (RFC 3986 format). This should help someone learn how to use your service, including any specifics required to access data, e.g. authentication. (maps from 'documentationUrl')
    )
    environment: ServiceEnvironment | None = (
        None  # Environment the service is running in. Use this to distinguish between production, development and testing/staging deployments. Suggested values are prod, test, dev, staging. However this is advised and not enforced.
    )
    updated_at: ServiceUpdatedAt | None = (
        None  # Timestamp describing when the service was last updated (RFC 3339 format) (maps from 'updatedAt')
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "contactUrl": "contact_url",
            "createdAt": "created_at",
            "description": "description",
            "documentationUrl": "documentation_url",
            "environment": "environment",
            "id": "id_",
            "name": "name",
            "organization": "organization",
            "type": "type_",
            "updatedAt": "updated_at",
            "version": "version",
        }
        key_transform_with_dump = {
            "contact_url": "contactUrl",
            "created_at": "createdAt",
            "description": "description",
            "documentation_url": "documentationUrl",
            "environment": "environment",
            "id_": "id",
            "name": "name",
            "organization": "organization",
            "type_": "type",
            "updated_at": "updatedAt",
            "version": "version",
        }
