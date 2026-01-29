from dataclasses import dataclass

from .contact_url import ContactUrl
from .created_at import CreatedAt
from .description import Description
from .documentation_url import DocumentationUrl
from .environment import Environment
from .galaxy_schema_drs_organization import GalaxySchemaDrsOrganization
from .service_type import ServiceType
from .updated_at import UpdatedAt

__all__ = ["Service"]


@dataclass
class Service:
    """
    Service dataclass.

    Args:
        id_ (str)                : Unique ID of this service. Reverse domain name notation
                                   is recommended, though not required. The identifier
                                   should attempt to be globally unique so it can be used in
                                   downstream aggregator services e.g. Service Registry.
        name (str)               : Name of this service. Should be human readable.
        organization (GalaxySchemaDrsOrganization)
                                 :
        type_ (ServiceType)      :
        version (str)            : Version of the service being described. Semantic
                                   versioning is recommended, but other identifiers, such as
                                   dates or commit hashes, are also allowed. The version
                                   should be changed whenever the service is updated.
        contact_url (Optional[ContactUrl])
                                 : URL of the contact for the provider of this service, e.g.
                                   a link to a contact form (RFC 3986 format), or an email
                                   (RFC 2368 format).
        created_at (Optional[CreatedAt])
                                 : Timestamp describing when the service was first deployed
                                   and available (RFC 3339 format)
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        documentation_url (Optional[DocumentationUrl])
                                 : URL of the documentation of this service (RFC 3986
                                   format). This should help someone learn how to use your
                                   service, including any specifics required to access data,
                                   e.g. authentication.
        environment (Optional[Environment])
                                 : Environment the service is running in. Use this to
                                   distinguish between production, development and
                                   testing/staging deployments. Suggested values are prod,
                                   test, dev, staging. However this is advised and not
                                   enforced.
        updated_at (Optional[UpdatedAt])
                                 : Timestamp describing when the service was last updated
                                   (RFC 3339 format)
    """

    id_: str  # Unique ID of this service. Reverse domain name notation is recommended, though not required. The identifier should attempt to be globally unique so it can be used in downstream aggregator services e.g. Service Registry.
    name: str  # Name of this service. Should be human readable.
    organization: GalaxySchemaDrsOrganization
    type_: ServiceType
    version: str  # Version of the service being described. Semantic versioning is recommended, but other identifiers, such as dates or commit hashes, are also allowed. The version should be changed whenever the service is updated.
    contact_url: ContactUrl | None = (
        None  # URL of the contact for the provider of this service, e.g. a link to a contact form (RFC 3986 format), or an email (RFC 2368 format).
    )
    created_at: CreatedAt | None = (
        None  # Timestamp describing when the service was first deployed and available (RFC 3339 format)
    )
    description: Description | None = ""  # Detailed text description for this Quota.
    documentation_url: DocumentationUrl | None = (
        None  # URL of the documentation of this service (RFC 3986 format). This should help someone learn how to use your service, including any specifics required to access data, e.g. authentication.
    )
    environment: Environment | None = (
        None  # Environment the service is running in. Use this to distinguish between production, development and testing/staging deployments. Suggested values are prod, test, dev, staging. However this is advised and not enforced.
    )
    updated_at: UpdatedAt | None = None  # Timestamp describing when the service was last updated (RFC 3339 format)
