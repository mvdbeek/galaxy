from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InvocationFailureWorkflowParameterInvalidResponse")


@_attrs_define
class InvocationFailureWorkflowParameterInvalidResponse:
    """
    Attributes:
        details (str): Message raised by validator
        reason (Literal['workflow_parameter_invalid']):
        workflow_step_id (int):
    """

    details: str
    reason: Literal["workflow_parameter_invalid"]
    workflow_step_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        reason = self.reason

        workflow_step_id = self.workflow_step_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "details": details,
                "reason": reason,
                "workflow_step_id": workflow_step_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        details = d.pop("details")

        reason = cast(Literal["workflow_parameter_invalid"], d.pop("reason"))
        if reason != "workflow_parameter_invalid":
            raise ValueError(f"reason must match const 'workflow_parameter_invalid', got '{reason}'")

        workflow_step_id = d.pop("workflow_step_id")

        invocation_failure_workflow_parameter_invalid_response = cls(
            details=details,
            reason=reason,
            workflow_step_id=workflow_step_id,
        )

        invocation_failure_workflow_parameter_invalid_response.additional_properties = d
        return invocation_failure_workflow_parameter_invalid_response

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
