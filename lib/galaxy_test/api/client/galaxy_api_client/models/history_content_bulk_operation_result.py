from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_operation_item_error import BulkOperationItemError


T = TypeVar("T", bound="HistoryContentBulkOperationResult")


@_attrs_define
class HistoryContentBulkOperationResult:
    """
    Attributes:
        errors (list[BulkOperationItemError]):
        success_count (int):
    """

    errors: list[BulkOperationItemError]
    success_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        success_count = self.success_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
                "success_count": success_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_operation_item_error import BulkOperationItemError

        d = dict(src_dict)
        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = BulkOperationItemError.from_dict(errors_item_data)

            errors.append(errors_item)

        success_count = d.pop("success_count")

        history_content_bulk_operation_result = cls(
            errors=errors,
            success_count=success_count,
        )

        history_content_bulk_operation_result.additional_properties = d
        return history_content_bulk_operation_result

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
