from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.access_method_type import AccessMethodType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_url import AccessURL
    from ..models.authorizations import Authorizations


T = TypeVar("T", bound="AccessMethod")


@_attrs_define
class AccessMethod:
    """
    Attributes:
        type_ (AccessMethodType):
        access_id (None | str | Unset): An arbitrary string to be passed to the `/access` method to get an `AccessURL`.
            This string must be unique within the scope of a single object. Note that at least one of `access_url` and
            `access_id` must be provided.
        access_url (AccessURL | None | Unset):
        authorizations (Authorizations | None | Unset):
        region (None | str | Unset): Name of the region in the cloud service provider that the object belongs to.
    """

    type_: AccessMethodType
    access_id: None | str | Unset = UNSET
    access_url: AccessURL | None | Unset = UNSET
    authorizations: Authorizations | None | Unset = UNSET
    region: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.access_url import AccessURL
        from ..models.authorizations import Authorizations

        type_ = self.type_.value

        access_id: None | str | Unset
        if isinstance(self.access_id, Unset):
            access_id = UNSET
        else:
            access_id = self.access_id

        access_url: dict[str, Any] | None | Unset
        if isinstance(self.access_url, Unset):
            access_url = UNSET
        elif isinstance(self.access_url, AccessURL):
            access_url = self.access_url.to_dict()
        else:
            access_url = self.access_url

        authorizations: dict[str, Any] | None | Unset
        if isinstance(self.authorizations, Unset):
            authorizations = UNSET
        elif isinstance(self.authorizations, Authorizations):
            authorizations = self.authorizations.to_dict()
        else:
            authorizations = self.authorizations

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if access_id is not UNSET:
            field_dict["access_id"] = access_id
        if access_url is not UNSET:
            field_dict["access_url"] = access_url
        if authorizations is not UNSET:
            field_dict["authorizations"] = authorizations
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.access_url import AccessURL
        from ..models.authorizations import Authorizations

        d = dict(src_dict)
        type_ = AccessMethodType(d.pop("type"))

        def _parse_access_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_id = _parse_access_id(d.pop("access_id", UNSET))

        def _parse_access_url(data: object) -> AccessURL | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                access_url_type_0 = AccessURL.from_dict(data)

                return access_url_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccessURL | None | Unset, data)

        access_url = _parse_access_url(d.pop("access_url", UNSET))

        def _parse_authorizations(data: object) -> Authorizations | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                authorizations_type_0 = Authorizations.from_dict(data)

                return authorizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Authorizations | None | Unset, data)

        authorizations = _parse_authorizations(d.pop("authorizations", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        access_method = cls(
            type_=type_,
            access_id=access_id,
            access_url=access_url,
            authorizations=authorizations,
            region=region,
        )

        access_method.additional_properties = d
        return access_method

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
