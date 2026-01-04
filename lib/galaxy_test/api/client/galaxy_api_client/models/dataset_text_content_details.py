from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DatasetTextContentDetails")


@_attrs_define
class DatasetTextContentDetails:
    """
    Attributes:
        item_data (None | str): First chunk of text content (maximum 1MB) of the dataset.
        item_url (str): URL to access this dataset.
        truncated (bool): Whether the text in `item_data` has been truncated or contains the whole contents.
    """

    item_data: None | str
    item_url: str
    truncated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_data: None | str
        item_data = self.item_data

        item_url = self.item_url

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_data": item_data,
                "item_url": item_url,
                "truncated": truncated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_item_data(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        item_data = _parse_item_data(d.pop("item_data"))

        item_url = d.pop("item_url")

        truncated = d.pop("truncated")

        dataset_text_content_details = cls(
            item_data=item_data,
            item_url=item_url,
            truncated=truncated,
        )

        dataset_text_content_details.additional_properties = d
        return dataset_text_content_details

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
