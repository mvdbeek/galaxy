from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLibraryFilePayload")


@_attrs_define
class CreateLibraryFilePayload:
    """
    Attributes:
        from_hda_id (None | str | Unset): The ID of an accessible HDA to copy into the library.
        from_hdca_id (None | str | Unset): The ID of an accessible HDCA to copy into the library. Nested collections are
            not allowed, you must flatten the collection first.
        ldda_message (None | str | Unset): The new message attribute of the LDDA created. Default: ''.
    """

    from_hda_id: None | str | Unset = UNSET
    from_hdca_id: None | str | Unset = UNSET
    ldda_message: None | str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_hda_id: None | str | Unset
        if isinstance(self.from_hda_id, Unset):
            from_hda_id = UNSET
        else:
            from_hda_id = self.from_hda_id

        from_hdca_id: None | str | Unset
        if isinstance(self.from_hdca_id, Unset):
            from_hdca_id = UNSET
        else:
            from_hdca_id = self.from_hdca_id

        ldda_message: None | str | Unset
        if isinstance(self.ldda_message, Unset):
            ldda_message = UNSET
        else:
            ldda_message = self.ldda_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_hda_id is not UNSET:
            field_dict["from_hda_id"] = from_hda_id
        if from_hdca_id is not UNSET:
            field_dict["from_hdca_id"] = from_hdca_id
        if ldda_message is not UNSET:
            field_dict["ldda_message"] = ldda_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_from_hda_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_hda_id = _parse_from_hda_id(d.pop("from_hda_id", UNSET))

        def _parse_from_hdca_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_hdca_id = _parse_from_hdca_id(d.pop("from_hdca_id", UNSET))

        def _parse_ldda_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ldda_message = _parse_ldda_message(d.pop("ldda_message", UNSET))

        create_library_file_payload = cls(
            from_hda_id=from_hda_id,
            from_hdca_id=from_hdca_id,
            ldda_message=ldda_message,
        )

        create_library_file_payload.additional_properties = d
        return create_library_file_payload

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
