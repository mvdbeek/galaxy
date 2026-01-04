from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Person")


@_attrs_define
class Person:
    """
    Attributes:
        address (None | str | Unset):
        alternate_name (None | str | Unset):
        class_ (str | Unset):  Default: 'Person'.
        email (None | str | Unset):
        family_name (None | str | Unset):
        fax_number (None | str | Unset):
        given_name (None | str | Unset):
        honorific_prefix (None | str | Unset): Honorific Prefix (e.g. Dr/Mrs/Mr)
        honorific_suffix (None | str | Unset): Honorific Suffix (e.g. M.D.)
        identifier (None | str | Unset): Identifier (typically an orcid.org ID)
        image (None | str | Unset):
        job_title (None | str | Unset):
        name (None | str | Unset): The name of the creator.
        telephone (None | str | Unset):
        url (None | str | Unset):
    """

    address: None | str | Unset = UNSET
    alternate_name: None | str | Unset = UNSET
    class_: str | Unset = "Person"
    email: None | str | Unset = UNSET
    family_name: None | str | Unset = UNSET
    fax_number: None | str | Unset = UNSET
    given_name: None | str | Unset = UNSET
    honorific_prefix: None | str | Unset = UNSET
    honorific_suffix: None | str | Unset = UNSET
    identifier: None | str | Unset = UNSET
    image: None | str | Unset = UNSET
    job_title: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    telephone: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        alternate_name: None | str | Unset
        if isinstance(self.alternate_name, Unset):
            alternate_name = UNSET
        else:
            alternate_name = self.alternate_name

        class_ = self.class_

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        family_name: None | str | Unset
        if isinstance(self.family_name, Unset):
            family_name = UNSET
        else:
            family_name = self.family_name

        fax_number: None | str | Unset
        if isinstance(self.fax_number, Unset):
            fax_number = UNSET
        else:
            fax_number = self.fax_number

        given_name: None | str | Unset
        if isinstance(self.given_name, Unset):
            given_name = UNSET
        else:
            given_name = self.given_name

        honorific_prefix: None | str | Unset
        if isinstance(self.honorific_prefix, Unset):
            honorific_prefix = UNSET
        else:
            honorific_prefix = self.honorific_prefix

        honorific_suffix: None | str | Unset
        if isinstance(self.honorific_suffix, Unset):
            honorific_suffix = UNSET
        else:
            honorific_suffix = self.honorific_suffix

        identifier: None | str | Unset
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        image: None | str | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        telephone: None | str | Unset
        if isinstance(self.telephone, Unset):
            telephone = UNSET
        else:
            telephone = self.telephone

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if alternate_name is not UNSET:
            field_dict["alternateName"] = alternate_name
        if class_ is not UNSET:
            field_dict["class"] = class_
        if email is not UNSET:
            field_dict["email"] = email
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if fax_number is not UNSET:
            field_dict["faxNumber"] = fax_number
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if honorific_prefix is not UNSET:
            field_dict["honorificPrefix"] = honorific_prefix
        if honorific_suffix is not UNSET:
            field_dict["honorificSuffix"] = honorific_suffix
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if image is not UNSET:
            field_dict["image"] = image
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if name is not UNSET:
            field_dict["name"] = name
        if telephone is not UNSET:
            field_dict["telephone"] = telephone
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_alternate_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alternate_name = _parse_alternate_name(d.pop("alternateName", UNSET))

        class_ = d.pop("class", UNSET)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_family_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family_name = _parse_family_name(d.pop("familyName", UNSET))

        def _parse_fax_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number = _parse_fax_number(d.pop("faxNumber", UNSET))

        def _parse_given_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        given_name = _parse_given_name(d.pop("givenName", UNSET))

        def _parse_honorific_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        honorific_prefix = _parse_honorific_prefix(d.pop("honorificPrefix", UNSET))

        def _parse_honorific_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        honorific_suffix = _parse_honorific_suffix(d.pop("honorificSuffix", UNSET))

        def _parse_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))

        def _parse_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_telephone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone = _parse_telephone(d.pop("telephone", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        person = cls(
            address=address,
            alternate_name=alternate_name,
            class_=class_,
            email=email,
            family_name=family_name,
            fax_number=fax_number,
            given_name=given_name,
            honorific_prefix=honorific_prefix,
            honorific_suffix=honorific_suffix,
            identifier=identifier,
            image=image,
            job_title=job_title,
            name=name,
            telephone=telephone,
            url=url,
        )

        person.additional_properties = d
        return person

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
