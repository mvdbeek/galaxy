from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.context import Context


T = TypeVar("T", bound="AgentQueryRequest")


@_attrs_define
class AgentQueryRequest:
    """Request to query an AI agent.

    Attributes:
        query (str): The user's question or request
        agent_type (str | Unset): Preferred agent type ('auto' for routing) Default: 'auto'.
        context (Context | Unset): Additional context for the query
        stream (bool | Unset): Whether to stream the response Default: False.
    """

    query: str
    agent_type: str | Unset = "auto"
    context: Context | Unset = UNSET
    stream: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        agent_type = self.agent_type

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        stream = self.stream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if agent_type is not UNSET:
            field_dict["agent_type"] = agent_type
        if context is not UNSET:
            field_dict["context"] = context
        if stream is not UNSET:
            field_dict["stream"] = stream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context import Context

        d = dict(src_dict)
        query = d.pop("query")

        agent_type = d.pop("agent_type", UNSET)

        _context = d.pop("context", UNSET)
        context: Context | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = Context.from_dict(_context)

        stream = d.pop("stream", UNSET)

        agent_query_request = cls(
            query=query,
            agent_type=agent_type,
            context=context,
            stream=stream,
        )

        agent_query_request.additional_properties = d
        return agent_query_request

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
