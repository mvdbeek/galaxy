from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvocationFailureExpressionEvaluationFailedResponse")


@_attrs_define
class InvocationFailureExpressionEvaluationFailedResponse:
    """
    Attributes:
        reason (Literal['expression_evaluation_failed']):
        workflow_step_id (int): Workflow step id of step that failed.
        details (None | str | Unset): May contain details to help troubleshoot this problem.
    """

    reason: Literal["expression_evaluation_failed"]
    workflow_step_id: int
    details: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        workflow_step_id = self.workflow_step_id

        details: None | str | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "workflow_step_id": workflow_step_id,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = cast(Literal["expression_evaluation_failed"], d.pop("reason"))
        if reason != "expression_evaluation_failed":
            raise ValueError(f"reason must match const 'expression_evaluation_failed', got '{reason}'")

        workflow_step_id = d.pop("workflow_step_id")

        def _parse_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        invocation_failure_expression_evaluation_failed_response = cls(
            reason=reason,
            workflow_step_id=workflow_step_id,
            details=details,
        )

        invocation_failure_expression_evaluation_failed_response.additional_properties = d
        return invocation_failure_expression_evaluation_failed_response

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
