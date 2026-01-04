from dataclasses import dataclass

from .address import Address
from .alternate_name import AlternateName
from .email_ import Email_
from .fax_number import FaxNumber
from .identifier import Identifier
from .image import Image
from .name import Name
from .telephone import Telephone
from .url import Url

__all__ = ["GalaxySchemaSchemaOrganization"]


@dataclass
class GalaxySchemaSchemaOrganization:
    """
    GalaxySchemaSchemaOrganization dataclass.

    Args:
        address (Optional[Address])
                                 :
        alternate_name (Optional[AlternateName])
                                 :
        class_ (Optional[str])   :
        email_ (Optional[Email_]): Email address for communication with the user. Only
                                   required for anonymous users.
        fax_number (Optional[FaxNumber])
                                 :
        identifier (Optional[Identifier])
                                 : Identifier (typically an orcid.org ID)
        image (Optional[Image])  :
        name (Optional[Name])    : The name of the creator.
        telephone (Optional[Telephone])
                                 :
        url (Optional[Url])      : The relative URL to access this item.
    """

    address: Address | None = None
    alternate_name: AlternateName | None = None
    class_: str | None = "Organization"
    email_: Email_ | None = None  # Email address for communication with the user. Only required for anonymous users.
    fax_number: FaxNumber | None = None
    identifier: Identifier | None = None  # Identifier (typically an orcid.org ID)
    image: Image | None = None
    name: Name | None = None  # The name of the creator.
    telephone: Telephone | None = None
    url: Url | None = None  # The relative URL to access this item.
