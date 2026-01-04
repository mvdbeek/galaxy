from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_object_request_metadata import ExportObjectRequestMetadata
    from ..models.export_object_result_metadata import ExportObjectResultMetadata


T = TypeVar("T", bound="ExportObjectMetadata")


@_attrs_define
class ExportObjectMetadata:
    """
    Attributes:
        request_data (ExportObjectRequestMetadata):
        result_data (ExportObjectResultMetadata | None | Unset):
    """

    request_data: ExportObjectRequestMetadata
    result_data: ExportObjectResultMetadata | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.export_object_result_metadata import ExportObjectResultMetadata

        request_data = self.request_data.to_dict()

        result_data: dict[str, Any] | None | Unset
        if isinstance(self.result_data, Unset):
            result_data = UNSET
        elif isinstance(self.result_data, ExportObjectResultMetadata):
            result_data = self.result_data.to_dict()
        else:
            result_data = self.result_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request_data": request_data,
            }
        )
        if result_data is not UNSET:
            field_dict["result_data"] = result_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_object_request_metadata import ExportObjectRequestMetadata
        from ..models.export_object_result_metadata import ExportObjectResultMetadata

        d = dict(src_dict)
        request_data = ExportObjectRequestMetadata.from_dict(d.pop("request_data"))

        def _parse_result_data(data: object) -> ExportObjectResultMetadata | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_data_type_0 = ExportObjectResultMetadata.from_dict(data)

                return result_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportObjectResultMetadata | None | Unset, data)

        result_data = _parse_result_data(d.pop("result_data", UNSET))

        export_object_metadata = cls(
            request_data=request_data,
            result_data=result_data,
        )

        export_object_metadata.additional_properties = d
        return export_object_metadata

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
