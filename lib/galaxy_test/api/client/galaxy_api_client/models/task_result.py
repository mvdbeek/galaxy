from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_state import TaskState

T = TypeVar("T", bound="TaskResult")


@_attrs_define
class TaskResult:
    """Contains information about the result of an asynchronous task.

    Attributes:
        result (str): The result message of the task. Empty if the task is still running. If the task failed, this will
            contain the exception message.
        state (TaskState): Enum representing the possible states of a task.
    """

    result: str
    state: TaskState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result = self.result

        state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        result = d.pop("result")

        state = TaskState(d.pop("state"))

        task_result = cls(
            result=result,
            state=state,
        )

        task_result.additional_properties = d
        return task_result

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
