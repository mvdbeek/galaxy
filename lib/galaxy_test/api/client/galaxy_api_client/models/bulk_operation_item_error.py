from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.encoded_history_content_item import EncodedHistoryContentItem


T = TypeVar("T", bound="BulkOperationItemError")


@_attrs_define
class BulkOperationItemError:
    """
    Attributes:
        error (str):
        item (EncodedHistoryContentItem):
    """

    error: str
    item: EncodedHistoryContentItem
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        item = self.item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "item": item,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encoded_history_content_item import EncodedHistoryContentItem

        d = dict(src_dict)
        error = d.pop("error")

        item = EncodedHistoryContentItem.from_dict(d.pop("item"))

        bulk_operation_item_error = cls(
            error=error,
            item=item,
        )

        bulk_operation_item_error.additional_properties = d
        return bulk_operation_item_error

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
