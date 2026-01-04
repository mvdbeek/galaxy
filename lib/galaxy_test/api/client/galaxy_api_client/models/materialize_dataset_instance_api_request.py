from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_source_type import DatasetSourceType

T = TypeVar("T", bound="MaterializeDatasetInstanceAPIRequest")


@_attrs_define
class MaterializeDatasetInstanceAPIRequest:
    """
    Attributes:
        content (str): Depending on the `source` it can be:
            - The encoded id of the source library dataset
            - The encoded id of the HDA
             Example: 0123456789ABCDEF.
        source (DatasetSourceType):
    """

    content: str
    source: DatasetSourceType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        source = DatasetSourceType(d.pop("source"))

        materialize_dataset_instance_api_request = cls(
            content=content,
            source=source,
        )

        materialize_dataset_instance_api_request.additional_properties = d
        return materialize_dataset_instance_api_request

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
