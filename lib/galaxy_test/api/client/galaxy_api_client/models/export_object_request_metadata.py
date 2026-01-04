from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_object_type import ExportObjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.short_term_store_export_payload import ShortTermStoreExportPayload
    from ..models.write_store_to_payload import WriteStoreToPayload


T = TypeVar("T", bound="ExportObjectRequestMetadata")


@_attrs_define
class ExportObjectRequestMetadata:
    """
    Attributes:
        object_id (str):  Example: 0123456789ABCDEF.
        object_type (ExportObjectType): Types of objects that can be exported.
        payload (ShortTermStoreExportPayload | WriteStoreToPayload):
        user_id (None | str | Unset):
    """

    object_id: str
    object_type: ExportObjectType
    payload: ShortTermStoreExportPayload | WriteStoreToPayload
    user_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.write_store_to_payload import WriteStoreToPayload

        object_id = self.object_id

        object_type = self.object_type.value

        payload: dict[str, Any]
        if isinstance(self.payload, WriteStoreToPayload):
            payload = self.payload.to_dict()
        else:
            payload = self.payload.to_dict()

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_id": object_id,
                "object_type": object_type,
                "payload": payload,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.short_term_store_export_payload import ShortTermStoreExportPayload
        from ..models.write_store_to_payload import WriteStoreToPayload

        d = dict(src_dict)
        object_id = d.pop("object_id")

        object_type = ExportObjectType(d.pop("object_type"))

        def _parse_payload(data: object) -> ShortTermStoreExportPayload | WriteStoreToPayload:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_0 = WriteStoreToPayload.from_dict(data)

                return payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            payload_type_1 = ShortTermStoreExportPayload.from_dict(data)

            return payload_type_1

        payload = _parse_payload(d.pop("payload"))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        export_object_request_metadata = cls(
            object_id=object_id,
            object_type=object_type,
            payload=payload,
            user_id=user_id,
        )

        export_object_request_metadata.additional_properties = d
        return export_object_request_metadata

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
