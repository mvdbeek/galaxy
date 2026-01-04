from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.body_ai_agents_custom_tool_create_custom_tool_context_type_0 import (
        BodyAiAgentsCustomToolCreateCustomToolContextType0,
    )


T = TypeVar("T", bound="BodyAiAgentsCustomToolCreateCustomTool")


@_attrs_define
class BodyAiAgentsCustomToolCreateCustomTool:
    """
    Attributes:
        query (str): Description of the tool to create
        context (BodyAiAgentsCustomToolCreateCustomToolContextType0 | None | Unset): Additional context for tool
            creation
    """

    query: str
    context: BodyAiAgentsCustomToolCreateCustomToolContextType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.body_ai_agents_custom_tool_create_custom_tool_context_type_0 import (
            BodyAiAgentsCustomToolCreateCustomToolContextType0,
        )

        query = self.query

        context: dict[str, Any] | None | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, BodyAiAgentsCustomToolCreateCustomToolContextType0):
            context = self.context.to_dict()
        else:
            context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.body_ai_agents_custom_tool_create_custom_tool_context_type_0 import (
            BodyAiAgentsCustomToolCreateCustomToolContextType0,
        )

        d = dict(src_dict)
        query = d.pop("query")

        def _parse_context(data: object) -> BodyAiAgentsCustomToolCreateCustomToolContextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = BodyAiAgentsCustomToolCreateCustomToolContextType0.from_dict(data)

                return context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BodyAiAgentsCustomToolCreateCustomToolContextType0 | None | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        body_ai_agents_custom_tool_create_custom_tool = cls(
            query=query,
            context=context,
        )

        body_ai_agents_custom_tool_create_custom_tool.additional_properties = d
        return body_ai_agents_custom_tool_create_custom_tool

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
