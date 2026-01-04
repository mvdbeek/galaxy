from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvocationUnexpectedFailureResponse")


@_attrs_define
class InvocationUnexpectedFailureResponse:
    """
    Attributes:
        reason (Literal['unexpected_failure']):
        details (None | str | Unset): May contains details to help troubleshoot this problem.
        workflow_step_id (int | None | Unset): Workflow step id of step that failed.
    """

    reason: Literal["unexpected_failure"]
    details: None | str | Unset = UNSET
    workflow_step_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        details: None | str | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details

        workflow_step_id: int | None | Unset
        if isinstance(self.workflow_step_id, Unset):
            workflow_step_id = UNSET
        else:
            workflow_step_id = self.workflow_step_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if workflow_step_id is not UNSET:
            field_dict["workflow_step_id"] = workflow_step_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = cast(Literal["unexpected_failure"], d.pop("reason"))
        if reason != "unexpected_failure":
            raise ValueError(f"reason must match const 'unexpected_failure', got '{reason}'")

        def _parse_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_workflow_step_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        workflow_step_id = _parse_workflow_step_id(d.pop("workflow_step_id", UNSET))

        invocation_unexpected_failure_response = cls(
            reason=reason,
            details=details,
            workflow_step_id=workflow_step_id,
        )

        invocation_unexpected_failure_response.additional_properties = d
        return invocation_unexpected_failure_response

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
