from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.encoded_data_item_source_id import EncodedDataItemSourceId


T = TypeVar("T", bound="JobOutput")


@_attrs_define
class JobOutput:
    """
    Attributes:
        label (Any): The output label
        value (EncodedDataItemSourceId):
    """

    label: Any
    value: EncodedDataItemSourceId
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encoded_data_item_source_id import EncodedDataItemSourceId

        d = dict(src_dict)
        label = d.pop("label")

        value = EncodedDataItemSourceId.from_dict(d.pop("value"))

        job_output = cls(
            label=label,
            value=value,
        )

        job_output.additional_properties = d
        return job_output

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
