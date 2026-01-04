from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InvocationFailureJobFailedResponse")


@_attrs_define
class InvocationFailureJobFailedResponse:
    """
    Attributes:
        dependent_workflow_step_id (int): Workflow step id of step that caused failure.
        job_id (str): Job ID that relates to failure. Example: 0123456789ABCDEF.
        reason (Literal['job_failed']):
        workflow_step_id (int): Workflow step id of step that failed.
    """

    dependent_workflow_step_id: int
    job_id: str
    reason: Literal["job_failed"]
    workflow_step_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dependent_workflow_step_id = self.dependent_workflow_step_id

        job_id = self.job_id

        reason = self.reason

        workflow_step_id = self.workflow_step_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dependent_workflow_step_id": dependent_workflow_step_id,
                "job_id": job_id,
                "reason": reason,
                "workflow_step_id": workflow_step_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dependent_workflow_step_id = d.pop("dependent_workflow_step_id")

        job_id = d.pop("job_id")

        reason = cast(Literal["job_failed"], d.pop("reason"))
        if reason != "job_failed":
            raise ValueError(f"reason must match const 'job_failed', got '{reason}'")

        workflow_step_id = d.pop("workflow_step_id")

        invocation_failure_job_failed_response = cls(
            dependent_workflow_step_id=dependent_workflow_step_id,
            job_id=job_id,
            reason=reason,
            workflow_step_id=workflow_step_id,
        )

        invocation_failure_job_failed_response.additional_properties = d
        return invocation_failure_job_failed_response

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
