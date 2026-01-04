from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.async_task_result_summary import AsyncTaskResultSummary


T = TypeVar("T", bound="AsyncFile")


@_attrs_define
class AsyncFile:
    """
    Attributes:
        storage_request_id (UUID):
        task (AsyncTaskResultSummary):
    """

    storage_request_id: UUID
    task: AsyncTaskResultSummary
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        storage_request_id = str(self.storage_request_id)

        task = self.task.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storage_request_id": storage_request_id,
                "task": task,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.async_task_result_summary import AsyncTaskResultSummary

        d = dict(src_dict)
        storage_request_id = UUID(d.pop("storage_request_id"))

        task = AsyncTaskResultSummary.from_dict(d.pop("task"))

        async_file = cls(
            storage_request_id=storage_request_id,
            task=task,
        )

        async_file.additional_properties = d
        return async_file

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
