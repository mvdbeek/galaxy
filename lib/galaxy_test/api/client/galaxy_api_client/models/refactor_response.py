from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.refactor_action_execution import RefactorActionExecution


T = TypeVar("T", bound="RefactorResponse")


@_attrs_define
class RefactorResponse:
    """
    Attributes:
        action_executions (list[RefactorActionExecution]):
        dry_run (bool):
        workflow (str):
    """

    action_executions: list[RefactorActionExecution]
    dry_run: bool
    workflow: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_executions = []
        for action_executions_item_data in self.action_executions:
            action_executions_item = action_executions_item_data.to_dict()
            action_executions.append(action_executions_item)

        dry_run = self.dry_run

        workflow = self.workflow

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_executions": action_executions,
                "dry_run": dry_run,
                "workflow": workflow,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.refactor_action_execution import RefactorActionExecution

        d = dict(src_dict)
        action_executions = []
        _action_executions = d.pop("action_executions")
        for action_executions_item_data in _action_executions:
            action_executions_item = RefactorActionExecution.from_dict(action_executions_item_data)

            action_executions.append(action_executions_item)

        dry_run = d.pop("dry_run")

        workflow = d.pop("workflow")

        refactor_response = cls(
            action_executions=action_executions,
            dry_run=dry_run,
            workflow=workflow,
        )

        refactor_response.additional_properties = d
        return refactor_response

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
