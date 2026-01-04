from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LegacyLibraryPermissionsPayload")


@_attrs_define
class LegacyLibraryPermissionsPayload:
    """
    Attributes:
        library_access_in (list[str] | None | str | Unset): A list of role encoded IDs defining roles that should have
            access permission on the library.
        library_add_in (list[str] | None | str | Unset): A list of role encoded IDs defining roles that should have
            manage permission on the library.
        library_manage_in (list[str] | None | str | Unset): A list of role encoded IDs defining roles that should have
            modify permission on the library.
        library_modify_in (list[str] | None | str | Unset): A list of role encoded IDs defining roles that should be
            able to add items to the library.
    """

    library_access_in: list[str] | None | str | Unset = UNSET
    library_add_in: list[str] | None | str | Unset = UNSET
    library_manage_in: list[str] | None | str | Unset = UNSET
    library_modify_in: list[str] | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        library_access_in: list[str] | None | str | Unset
        if isinstance(self.library_access_in, Unset):
            library_access_in = UNSET
        elif isinstance(self.library_access_in, list):
            library_access_in = self.library_access_in

        else:
            library_access_in = self.library_access_in

        library_add_in: list[str] | None | str | Unset
        if isinstance(self.library_add_in, Unset):
            library_add_in = UNSET
        elif isinstance(self.library_add_in, list):
            library_add_in = self.library_add_in

        else:
            library_add_in = self.library_add_in

        library_manage_in: list[str] | None | str | Unset
        if isinstance(self.library_manage_in, Unset):
            library_manage_in = UNSET
        elif isinstance(self.library_manage_in, list):
            library_manage_in = self.library_manage_in

        else:
            library_manage_in = self.library_manage_in

        library_modify_in: list[str] | None | str | Unset
        if isinstance(self.library_modify_in, Unset):
            library_modify_in = UNSET
        elif isinstance(self.library_modify_in, list):
            library_modify_in = self.library_modify_in

        else:
            library_modify_in = self.library_modify_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if library_access_in is not UNSET:
            field_dict["LIBRARY_ACCESS_in"] = library_access_in
        if library_add_in is not UNSET:
            field_dict["LIBRARY_ADD_in"] = library_add_in
        if library_manage_in is not UNSET:
            field_dict["LIBRARY_MANAGE_in"] = library_manage_in
        if library_modify_in is not UNSET:
            field_dict["LIBRARY_MODIFY_in"] = library_modify_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_library_access_in(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                library_access_in_type_0 = cast(list[str], data)

                return library_access_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        library_access_in = _parse_library_access_in(d.pop("LIBRARY_ACCESS_in", UNSET))

        def _parse_library_add_in(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                library_add_in_type_0 = cast(list[str], data)

                return library_add_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        library_add_in = _parse_library_add_in(d.pop("LIBRARY_ADD_in", UNSET))

        def _parse_library_manage_in(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                library_manage_in_type_0 = cast(list[str], data)

                return library_manage_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        library_manage_in = _parse_library_manage_in(d.pop("LIBRARY_MANAGE_in", UNSET))

        def _parse_library_modify_in(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                library_modify_in_type_0 = cast(list[str], data)

                return library_modify_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        library_modify_in = _parse_library_modify_in(d.pop("LIBRARY_MODIFY_in", UNSET))

        legacy_library_permissions_payload = cls(
            library_access_in=library_access_in,
            library_add_in=library_add_in,
            library_manage_in=library_manage_in,
            library_modify_in=library_modify_in,
        )

        legacy_library_permissions_payload.additional_properties = d
        return legacy_library_permissions_payload

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
