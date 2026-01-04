from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_type import ActionType
from ..models.confidence_level import ConfidenceLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parameters import Parameters


T = TypeVar("T", bound="ActionSuggestion")


@_attrs_define
class ActionSuggestion:
    """Structured suggestion for user action.

    Attributes:
        action_type (ActionType): Types of actions agents can suggest.
        confidence (ConfidenceLevel): Confidence levels for agent responses.
        description (str): Human-readable description of the action
        parameters (Parameters | Unset): Parameters for the action
        priority (int | Unset): Priority level (1=high, 2=medium, 3=low) Default: 1.
    """

    action_type: ActionType
    confidence: ConfidenceLevel
    description: str
    parameters: Parameters | Unset = UNSET
    priority: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type.value

        confidence = self.confidence.value

        description = self.description

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "confidence": confidence,
                "description": description,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parameters import Parameters

        d = dict(src_dict)
        action_type = ActionType(d.pop("action_type"))

        confidence = ConfidenceLevel(d.pop("confidence"))

        description = d.pop("description")

        _parameters = d.pop("parameters", UNSET)
        parameters: Parameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = Parameters.from_dict(_parameters)

        priority = d.pop("priority", UNSET)

        action_suggestion = cls(
            action_type=action_type,
            confidence=confidence,
            description=description,
            parameters=parameters,
            priority=priority,
        )

        action_suggestion.additional_properties = d
        return action_suggestion

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
