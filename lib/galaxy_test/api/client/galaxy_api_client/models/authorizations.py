from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supported_type import SupportedType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Authorizations")


@_attrs_define
class Authorizations:
    """
    Attributes:
        bearer_auth_issuers (list[str] | None | Unset): If authorizations contain `BearerAuth` this is an optional list
            of issuers that may authorize access to this object. The caller must provide a token from one of these issuers.
            If this is empty or missing it assumed the caller knows which token to send via other means. It is strongly
            recommended that the caller validate that it is appropriate to send the requested token to the DRS server to
            mitigate attacks by malicious DRS servers requesting credentials they should not have.
        passport_auth_issuers (list[str] | None | Unset): If authorizations contain `PassportAuth` this is a required
            list of visa issuers (as found in a visa's `iss` claim) that may authorize access to this object. The caller
            must only provide passports that contain visas from this list. It is strongly recommended that the caller
            validate that it is appropriate to send the requested passport/visa to the DRS server to mitigate attacks by
            malicious DRS servers requesting credentials they should not have.
        supported_types (list[SupportedType] | None | Unset): An Optional list of support authorization types. More than
            one can be supported and tried in sequence. Defaults to `None` if empty or missing.
    """

    bearer_auth_issuers: list[str] | None | Unset = UNSET
    passport_auth_issuers: list[str] | None | Unset = UNSET
    supported_types: list[SupportedType] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bearer_auth_issuers: list[str] | None | Unset
        if isinstance(self.bearer_auth_issuers, Unset):
            bearer_auth_issuers = UNSET
        elif isinstance(self.bearer_auth_issuers, list):
            bearer_auth_issuers = self.bearer_auth_issuers

        else:
            bearer_auth_issuers = self.bearer_auth_issuers

        passport_auth_issuers: list[str] | None | Unset
        if isinstance(self.passport_auth_issuers, Unset):
            passport_auth_issuers = UNSET
        elif isinstance(self.passport_auth_issuers, list):
            passport_auth_issuers = self.passport_auth_issuers

        else:
            passport_auth_issuers = self.passport_auth_issuers

        supported_types: list[str] | None | Unset
        if isinstance(self.supported_types, Unset):
            supported_types = UNSET
        elif isinstance(self.supported_types, list):
            supported_types = []
            for supported_types_type_0_item_data in self.supported_types:
                supported_types_type_0_item = supported_types_type_0_item_data.value
                supported_types.append(supported_types_type_0_item)

        else:
            supported_types = self.supported_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bearer_auth_issuers is not UNSET:
            field_dict["bearer_auth_issuers"] = bearer_auth_issuers
        if passport_auth_issuers is not UNSET:
            field_dict["passport_auth_issuers"] = passport_auth_issuers
        if supported_types is not UNSET:
            field_dict["supported_types"] = supported_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_bearer_auth_issuers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bearer_auth_issuers_type_0 = cast(list[str], data)

                return bearer_auth_issuers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        bearer_auth_issuers = _parse_bearer_auth_issuers(d.pop("bearer_auth_issuers", UNSET))

        def _parse_passport_auth_issuers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                passport_auth_issuers_type_0 = cast(list[str], data)

                return passport_auth_issuers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        passport_auth_issuers = _parse_passport_auth_issuers(d.pop("passport_auth_issuers", UNSET))

        def _parse_supported_types(data: object) -> list[SupportedType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_types_type_0 = []
                _supported_types_type_0 = data
                for supported_types_type_0_item_data in _supported_types_type_0:
                    supported_types_type_0_item = SupportedType(supported_types_type_0_item_data)

                    supported_types_type_0.append(supported_types_type_0_item)

                return supported_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SupportedType] | None | Unset, data)

        supported_types = _parse_supported_types(d.pop("supported_types", UNSET))

        authorizations = cls(
            bearer_auth_issuers=bearer_auth_issuers,
            passport_auth_issuers=passport_auth_issuers,
            supported_types=supported_types,
        )

        authorizations.additional_properties = d
        return authorizations

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
