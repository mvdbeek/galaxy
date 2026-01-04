from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.async_task_result_summary import AsyncTaskResultSummary


T = TypeVar("T", bound="JobCreateResponse")


@_attrs_define
class JobCreateResponse:
    """
    Attributes:
        task_result (AsyncTaskResultSummary):
        tool_request_id (str):  Example: 0123456789ABCDEF.
    """

    task_result: AsyncTaskResultSummary
    tool_request_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_result = self.task_result.to_dict()

        tool_request_id = self.tool_request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_result": task_result,
                "tool_request_id": tool_request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.async_task_result_summary import AsyncTaskResultSummary

        d = dict(src_dict)
        task_result = AsyncTaskResultSummary.from_dict(d.pop("task_result"))

        tool_request_id = d.pop("tool_request_id")

        job_create_response = cls(
            task_result=task_result,
            tool_request_id=tool_request_id,
        )

        job_create_response.additional_properties = d
        return job_create_response

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
