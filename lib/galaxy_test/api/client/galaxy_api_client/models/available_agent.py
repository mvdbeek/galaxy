from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableAgent")


@_attrs_define
class AvailableAgent:
    """Information about an available agent.

    Attributes:
        agent_type (str): Unique identifier for the agent
        description (str): Description of the agent's capabilities
        enabled (bool): Whether the agent is currently enabled
        name (str): Human-readable name
        model (None | str | Unset): LLM model used by the agent
        specialties (list[str] | Unset): Areas of specialization
    """

    agent_type: str
    description: str
    enabled: bool
    name: str
    model: None | str | Unset = UNSET
    specialties: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_type = self.agent_type

        description = self.description

        enabled = self.enabled

        name = self.name

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        specialties: list[str] | Unset = UNSET
        if not isinstance(self.specialties, Unset):
            specialties = self.specialties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_type": agent_type,
                "description": description,
                "enabled": enabled,
                "name": name,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if specialties is not UNSET:
            field_dict["specialties"] = specialties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_type = d.pop("agent_type")

        description = d.pop("description")

        enabled = d.pop("enabled")

        name = d.pop("name")

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        specialties = cast(list[str], d.pop("specialties", UNSET))

        available_agent = cls(
            agent_type=agent_type,
            description=description,
            enabled=enabled,
            name=name,
            model=model,
            specialties=specialties,
        )

        available_agent.additional_properties = d
        return available_agent

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
