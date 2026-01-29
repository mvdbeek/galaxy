from dataclasses import dataclass

from .address import Address
from .alternate_name import AlternateName
from .email_ import Email_
from .family_name import FamilyName
from .fax_number import FaxNumber
from .given_name import GivenName
from .honorific_prefix import HonorificPrefix
from .honorific_suffix import HonorificSuffix
from .identifier import Identifier
from .image import Image
from .job_title import JobTitle
from .name import Name
from .telephone import Telephone
from .url import Url

__all__ = ["Person"]


@dataclass
class Person:
    """
    Person dataclass.

    Args:
        address (Optional[Address])
                                 :
        alternate_name (Optional[AlternateName])
                                 :
        class_ (Optional[str])   :
        email_ (Optional[Email_]): Email address for communication with the user. Only
                                   required for anonymous users.
        family_name (Optional[FamilyName])
                                 :
        fax_number (Optional[FaxNumber])
                                 :
        given_name (Optional[GivenName])
                                 :
        honorific_prefix (Optional[HonorificPrefix])
                                 : Honorific Prefix (e.g. Dr/Mrs/Mr)
        honorific_suffix (Optional[HonorificSuffix])
                                 : Honorific Suffix (e.g. M.D.)
        identifier (Optional[Identifier])
                                 : Identifier (typically an orcid.org ID)
        image (Optional[Image])  :
        job_title (Optional[JobTitle])
                                 :
        name (Optional[Name])    : The name of the creator.
        telephone (Optional[Telephone])
                                 :
        url (Optional[Url])      : The relative URL to access this item.
    """

    address: Address | None = None
    alternate_name: AlternateName | None = None
    class_: str | None = "Person"
    email_: Email_ | None = None  # Email address for communication with the user. Only required for anonymous users.
    family_name: FamilyName | None = None
    fax_number: FaxNumber | None = None
    given_name: GivenName | None = None
    honorific_prefix: HonorificPrefix | None = None  # Honorific Prefix (e.g. Dr/Mrs/Mr)
    honorific_suffix: HonorificSuffix | None = None  # Honorific Suffix (e.g. M.D.)
    identifier: Identifier | None = None  # Identifier (typically an orcid.org ID)
    image: Image | None = None
    job_title: JobTitle | None = None
    name: Name | None = None  # The name of the creator.
    telephone: Telephone | None = None
    url: Url | None = None  # The relative URL to access this item.
