from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvocationFailureDatasetFailedResponse")


@_attrs_define
class InvocationFailureDatasetFailedResponse:
    """
    Attributes:
        hda_id (str): HistoryDatasetAssociation ID that relates to failure. Example: 0123456789ABCDEF.
        reason (Literal['dataset_failed']):
        workflow_step_id (int): Workflow step id of step that failed.
        dependent_workflow_step_id (int | None | Unset): Workflow step id of step that caused failure.
    """

    hda_id: str
    reason: Literal["dataset_failed"]
    workflow_step_id: int
    dependent_workflow_step_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hda_id = self.hda_id

        reason = self.reason

        workflow_step_id = self.workflow_step_id

        dependent_workflow_step_id: int | None | Unset
        if isinstance(self.dependent_workflow_step_id, Unset):
            dependent_workflow_step_id = UNSET
        else:
            dependent_workflow_step_id = self.dependent_workflow_step_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hda_id": hda_id,
                "reason": reason,
                "workflow_step_id": workflow_step_id,
            }
        )
        if dependent_workflow_step_id is not UNSET:
            field_dict["dependent_workflow_step_id"] = dependent_workflow_step_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hda_id = d.pop("hda_id")

        reason = cast(Literal["dataset_failed"], d.pop("reason"))
        if reason != "dataset_failed":
            raise ValueError(f"reason must match const 'dataset_failed', got '{reason}'")

        workflow_step_id = d.pop("workflow_step_id")

        def _parse_dependent_workflow_step_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dependent_workflow_step_id = _parse_dependent_workflow_step_id(d.pop("dependent_workflow_step_id", UNSET))

        invocation_failure_dataset_failed_response = cls(
            hda_id=hda_id,
            reason=reason,
            workflow_step_id=workflow_step_id,
            dependent_workflow_step_id=dependent_workflow_step_id,
        )

        invocation_failure_dataset_failed_response.additional_properties = d
        return invocation_failure_dataset_failed_response

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
