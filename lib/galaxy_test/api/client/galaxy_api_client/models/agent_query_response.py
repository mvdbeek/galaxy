from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_query_response_routing_info_type_0 import AgentQueryResponseRoutingInfoType0
    from ..models.agent_response import AgentResponse


T = TypeVar("T", bound="AgentQueryResponse")


@_attrs_define
class AgentQueryResponse:
    """Response from an AI agent query.

    Attributes:
        response (AgentResponse): Structured response from an AI agent.
        processing_time (float | None | Unset): Time taken to process the query in seconds
        routing_info (AgentQueryResponseRoutingInfoType0 | None | Unset): Information about how the query was routed
    """

    response: AgentResponse
    processing_time: float | None | Unset = UNSET
    routing_info: AgentQueryResponseRoutingInfoType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_query_response_routing_info_type_0 import AgentQueryResponseRoutingInfoType0

        response = self.response.to_dict()

        processing_time: float | None | Unset
        if isinstance(self.processing_time, Unset):
            processing_time = UNSET
        else:
            processing_time = self.processing_time

        routing_info: dict[str, Any] | None | Unset
        if isinstance(self.routing_info, Unset):
            routing_info = UNSET
        elif isinstance(self.routing_info, AgentQueryResponseRoutingInfoType0):
            routing_info = self.routing_info.to_dict()
        else:
            routing_info = self.routing_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response": response,
            }
        )
        if processing_time is not UNSET:
            field_dict["processing_time"] = processing_time
        if routing_info is not UNSET:
            field_dict["routing_info"] = routing_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_query_response_routing_info_type_0 import AgentQueryResponseRoutingInfoType0
        from ..models.agent_response import AgentResponse

        d = dict(src_dict)
        response = AgentResponse.from_dict(d.pop("response"))

        def _parse_processing_time(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        processing_time = _parse_processing_time(d.pop("processing_time", UNSET))

        def _parse_routing_info(data: object) -> AgentQueryResponseRoutingInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                routing_info_type_0 = AgentQueryResponseRoutingInfoType0.from_dict(data)

                return routing_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentQueryResponseRoutingInfoType0 | None | Unset, data)

        routing_info = _parse_routing_info(d.pop("routing_info", UNSET))

        agent_query_response = cls(
            response=response,
            processing_time=processing_time,
            routing_info=routing_info,
        )

        agent_query_response.additional_properties = d
        return agent_query_response

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
