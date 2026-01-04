from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.confidence_level import ConfidenceLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_suggestion import ActionSuggestion
    from ..models.metadata import Metadata


T = TypeVar("T", bound="AgentResponse")


@_attrs_define
class AgentResponse:
    """Structured response from an AI agent.

    Attributes:
        agent_type (str): Type of agent that generated this response
        confidence (ConfidenceLevel): Confidence levels for agent responses.
        content (str): Main response content
        metadata (Metadata | Unset): Additional metadata
        reasoning (None | str | Unset): Explanation of the agent's reasoning
        suggestions (list[ActionSuggestion] | Unset): Actionable suggestions
    """

    agent_type: str
    confidence: ConfidenceLevel
    content: str
    metadata: Metadata | Unset = UNSET
    reasoning: None | str | Unset = UNSET
    suggestions: list[ActionSuggestion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_type = self.agent_type

        confidence = self.confidence.value

        content = self.content

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        reasoning: None | str | Unset
        if isinstance(self.reasoning, Unset):
            reasoning = UNSET
        else:
            reasoning = self.reasoning

        suggestions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = []
            for suggestions_item_data in self.suggestions:
                suggestions_item = suggestions_item_data.to_dict()
                suggestions.append(suggestions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_type": agent_type,
                "confidence": confidence,
                "content": content,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if reasoning is not UNSET:
            field_dict["reasoning"] = reasoning
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_suggestion import ActionSuggestion
        from ..models.metadata import Metadata

        d = dict(src_dict)
        agent_type = d.pop("agent_type")

        confidence = ConfidenceLevel(d.pop("confidence"))

        content = d.pop("content")

        _metadata = d.pop("metadata", UNSET)
        metadata: Metadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        def _parse_reasoning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reasoning = _parse_reasoning(d.pop("reasoning", UNSET))

        _suggestions = d.pop("suggestions", UNSET)
        suggestions: list[ActionSuggestion] | Unset = UNSET
        if _suggestions is not UNSET:
            suggestions = []
            for suggestions_item_data in _suggestions:
                suggestions_item = ActionSuggestion.from_dict(suggestions_item_data)

                suggestions.append(suggestions_item)

        agent_response = cls(
            agent_type=agent_type,
            confidence=confidence,
            content=content,
            metadata=metadata,
            reasoning=reasoning,
            suggestions=suggestions,
        )

        agent_response.additional_properties = d
        return agent_response

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
