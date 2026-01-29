from dataclasses import dataclass

from .email__5 import Email5
from .galaxy_schema_schema_organization_address import GalaxySchemaSchemaOrganizationAddress
from .galaxy_schema_schema_organization_alternate_name import GalaxySchemaSchemaOrganizationAlternateName
from .galaxy_schema_schema_organization_fax_number import GalaxySchemaSchemaOrganizationFaxNumber
from .galaxy_schema_schema_organization_identifier import GalaxySchemaSchemaOrganizationIdentifier
from .galaxy_schema_schema_organization_image import GalaxySchemaSchemaOrganizationImage
from .galaxy_schema_schema_organization_name import GalaxySchemaSchemaOrganizationName
from .galaxy_schema_schema_organization_telephone import GalaxySchemaSchemaOrganizationTelephone
from .galaxy_schema_schema_organization_url import GalaxySchemaSchemaOrganizationUrl

__all__ = ["GalaxySchemaSchemaOrganization"]


@dataclass
class GalaxySchemaSchemaOrganization:
    """
    GalaxySchemaSchemaOrganization dataclass

    Args:
        address (GalaxySchemaSchemaOrganizationAddress | None)
                                 :
        alternate_name (GalaxySchemaSchemaOrganizationAlternateName | None)
                                 : Maps from 'alternateName'
        class_ (str | None)      : Maps from 'class'
        email_ (Email5 | None)   : Maps from 'email'
        fax_number (GalaxySchemaSchemaOrganizationFaxNumber | None)
                                 : Maps from 'faxNumber'
        identifier (GalaxySchemaSchemaOrganizationIdentifier | None)
                                 : Identifier (typically an orcid.org ID)
        image (GalaxySchemaSchemaOrganizationImage | None)
                                 :
        name (GalaxySchemaSchemaOrganizationName | None)
                                 : The name of the creator.
        telephone (GalaxySchemaSchemaOrganizationTelephone | None)
                                 :
        url (GalaxySchemaSchemaOrganizationUrl | None)
                                 :
    """

    address: GalaxySchemaSchemaOrganizationAddress | None = None
    alternate_name: GalaxySchemaSchemaOrganizationAlternateName | None = None  # Maps from 'alternateName'
    class_: str | None = "Organization"  # Maps from 'class'
    email_: Email5 | None = None  # Maps from 'email'
    fax_number: GalaxySchemaSchemaOrganizationFaxNumber | None = None  # Maps from 'faxNumber'
    identifier: GalaxySchemaSchemaOrganizationIdentifier | None = None  # Identifier (typically an orcid.org ID)
    image: GalaxySchemaSchemaOrganizationImage | None = None
    name: GalaxySchemaSchemaOrganizationName | None = None  # The name of the creator.
    telephone: GalaxySchemaSchemaOrganizationTelephone | None = None
    url: GalaxySchemaSchemaOrganizationUrl | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "address": "address",
            "alternateName": "alternate_name",
            "class": "class_",
            "email": "email_",
            "faxNumber": "fax_number",
            "identifier": "identifier",
            "image": "image",
            "name": "name",
            "telephone": "telephone",
            "url": "url",
        }
        key_transform_with_dump = {
            "address": "address",
            "alternate_name": "alternateName",
            "class_": "class",
            "email_": "email",
            "fax_number": "faxNumber",
            "identifier": "identifier",
            "image": "image",
            "name": "name",
            "telephone": "telephone",
            "url": "url",
        }
