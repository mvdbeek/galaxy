from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InvocationCancellationReviewFailedResponse")


@_attrs_define
class InvocationCancellationReviewFailedResponse:
    """
    Attributes:
        reason (Literal['cancelled_on_review']):
        workflow_step_id (int): Workflow step id of paused step that did not pass review.
    """

    reason: Literal["cancelled_on_review"]
    workflow_step_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        workflow_step_id = self.workflow_step_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "workflow_step_id": workflow_step_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = cast(Literal["cancelled_on_review"], d.pop("reason"))
        if reason != "cancelled_on_review":
            raise ValueError(f"reason must match const 'cancelled_on_review', got '{reason}'")

        workflow_step_id = d.pop("workflow_step_id")

        invocation_cancellation_review_failed_response = cls(
            reason=reason,
            workflow_step_id=workflow_step_id,
        )

        invocation_cancellation_review_failed_response.additional_properties = d
        return invocation_cancellation_review_failed_response

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
