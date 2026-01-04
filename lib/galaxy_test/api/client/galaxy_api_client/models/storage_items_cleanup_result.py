from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.storage_item_cleanup_error import StorageItemCleanupError


T = TypeVar("T", bound="StorageItemsCleanupResult")


@_attrs_define
class StorageItemsCleanupResult:
    """
    Attributes:
        errors (list[StorageItemCleanupError]):
        success_item_count (int):
        total_free_bytes (int):
        total_item_count (int):
    """

    errors: list[StorageItemCleanupError]
    success_item_count: int
    total_free_bytes: int
    total_item_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        success_item_count = self.success_item_count

        total_free_bytes = self.total_free_bytes

        total_item_count = self.total_item_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
                "success_item_count": success_item_count,
                "total_free_bytes": total_free_bytes,
                "total_item_count": total_item_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_item_cleanup_error import StorageItemCleanupError

        d = dict(src_dict)
        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = StorageItemCleanupError.from_dict(errors_item_data)

            errors.append(errors_item)

        success_item_count = d.pop("success_item_count")

        total_free_bytes = d.pop("total_free_bytes")

        total_item_count = d.pop("total_item_count")

        storage_items_cleanup_result = cls(
            errors=errors,
            success_item_count=success_item_count,
            total_free_bytes=total_free_bytes,
            total_item_count=total_item_count,
        )

        storage_items_cleanup_result.additional_properties = d
        return storage_items_cleanup_result

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
