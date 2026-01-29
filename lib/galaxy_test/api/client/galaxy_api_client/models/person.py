from dataclasses import dataclass

from .email__2 import Email2
from .person_address import PersonAddress
from .person_alternate_name import PersonAlternateName
from .person_family_name import PersonFamilyName
from .person_fax_number import PersonFaxNumber
from .person_given_name import PersonGivenName
from .person_honorific_prefix import PersonHonorificPrefix
from .person_honorific_suffix import PersonHonorificSuffix
from .person_identifier import PersonIdentifier
from .person_image import PersonImage
from .person_job_title import PersonJobTitle
from .person_name import PersonName
from .person_telephone import PersonTelephone
from .person_url import PersonUrl

__all__ = ["Person"]


@dataclass
class Person:
    """
    Person dataclass

    Args:
        address (PersonAddress | None)
                                 :
        alternate_name (PersonAlternateName | None)
                                 : Maps from 'alternateName'
        class_ (str | None)      : Maps from 'class'
        email_ (Email2 | None)   : Maps from 'email'
        family_name (PersonFamilyName | None)
                                 : Maps from 'familyName'
        fax_number (PersonFaxNumber | None)
                                 : Maps from 'faxNumber'
        given_name (PersonGivenName | None)
                                 : Maps from 'givenName'
        honorific_prefix (PersonHonorificPrefix | None)
                                 : Honorific Prefix (e.g. Dr/Mrs/Mr) (maps from
                                   'honorificPrefix')
        honorific_suffix (PersonHonorificSuffix | None)
                                 : Honorific Suffix (e.g. M.D.) (maps from
                                   'honorificSuffix')
        identifier (PersonIdentifier | None)
                                 : Identifier (typically an orcid.org ID)
        image (PersonImage | None):
        job_title (PersonJobTitle | None)
                                 : Maps from 'jobTitle'
        name (PersonName | None) : The name of the creator.
        telephone (PersonTelephone | None)
                                 :
        url (PersonUrl | None)   :
    """

    address: PersonAddress | None = None
    alternate_name: PersonAlternateName | None = None  # Maps from 'alternateName'
    class_: str | None = "Person"  # Maps from 'class'
    email_: Email2 | None = None  # Maps from 'email'
    family_name: PersonFamilyName | None = None  # Maps from 'familyName'
    fax_number: PersonFaxNumber | None = None  # Maps from 'faxNumber'
    given_name: PersonGivenName | None = None  # Maps from 'givenName'
    honorific_prefix: PersonHonorificPrefix | None = (
        None  # Honorific Prefix (e.g. Dr/Mrs/Mr) (maps from 'honorificPrefix')
    )
    honorific_suffix: PersonHonorificSuffix | None = None  # Honorific Suffix (e.g. M.D.) (maps from 'honorificSuffix')
    identifier: PersonIdentifier | None = None  # Identifier (typically an orcid.org ID)
    image: PersonImage | None = None
    job_title: PersonJobTitle | None = None  # Maps from 'jobTitle'
    name: PersonName | None = None  # The name of the creator.
    telephone: PersonTelephone | None = None
    url: PersonUrl | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "address": "address",
            "alternateName": "alternate_name",
            "class": "class_",
            "email": "email_",
            "familyName": "family_name",
            "faxNumber": "fax_number",
            "givenName": "given_name",
            "honorificPrefix": "honorific_prefix",
            "honorificSuffix": "honorific_suffix",
            "identifier": "identifier",
            "image": "image",
            "jobTitle": "job_title",
            "name": "name",
            "telephone": "telephone",
            "url": "url",
        }
        key_transform_with_dump = {
            "address": "address",
            "alternate_name": "alternateName",
            "class_": "class",
            "email_": "email",
            "family_name": "familyName",
            "fax_number": "faxNumber",
            "given_name": "givenName",
            "honorific_prefix": "honorificPrefix",
            "honorific_suffix": "honorificSuffix",
            "identifier": "identifier",
            "image": "image",
            "job_title": "jobTitle",
            "name": "name",
            "telephone": "telephone",
            "url": "url",
        }
