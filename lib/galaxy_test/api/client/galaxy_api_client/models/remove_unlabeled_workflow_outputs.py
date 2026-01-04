from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RemoveUnlabeledWorkflowOutputs")


@_attrs_define
class RemoveUnlabeledWorkflowOutputs:
    """
    Attributes:
        action_type (Literal['remove_unlabeled_workflow_outputs']):
    """

    action_type: Literal["remove_unlabeled_workflow_outputs"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_type = cast(Literal["remove_unlabeled_workflow_outputs"], d.pop("action_type"))
        if action_type != "remove_unlabeled_workflow_outputs":
            raise ValueError(f"action_type must match const 'remove_unlabeled_workflow_outputs', got '{action_type}'")

        remove_unlabeled_workflow_outputs = cls(
            action_type=action_type,
        )

        remove_unlabeled_workflow_outputs.additional_properties = d
        return remove_unlabeled_workflow_outputs

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
