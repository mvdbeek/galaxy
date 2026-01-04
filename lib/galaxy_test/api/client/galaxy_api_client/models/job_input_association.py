from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.encoded_data_item_source_id import EncodedDataItemSourceId


T = TypeVar("T", bound="JobInputAssociation")


@_attrs_define
class JobInputAssociation:
    """
    Attributes:
        dataset (EncodedDataItemSourceId):
        name (str): Name of the job input parameter.
    """

    dataset: EncodedDataItemSourceId
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset = self.dataset.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset": dataset,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encoded_data_item_source_id import EncodedDataItemSourceId

        d = dict(src_dict)
        dataset = EncodedDataItemSourceId.from_dict(d.pop("dataset"))

        name = d.pop("name")

        job_input_association = cls(
            dataset=dataset,
            name=name,
        )

        job_input_association.additional_properties = d
        return job_input_association

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
