from dataclasses import dataclass

from .agent_query_response_processing_time import AgentQueryResponseProcessingTime
from .agent_query_response_routing_info import AgentQueryResponseRoutingInfo
from .agent_response import AgentResponse

__all__ = ["AgentQueryResponse"]


@dataclass
class AgentQueryResponse:
    """
    Response from an AI agent query.

    Args:
        response (AgentResponse) : Structured response from an AI agent.
        processing_time (AgentQueryResponseProcessingTime | None)
                                 : Time taken to process the query in seconds
        routing_info (AgentQueryResponseRoutingInfo | None)
                                 : Information about how the query was routed
    """

    response: AgentResponse  # Structured response from an AI agent.
    processing_time: AgentQueryResponseProcessingTime | None = None  # Time taken to process the query in seconds
    routing_info: AgentQueryResponseRoutingInfo | None = None  # Information about how the query was routed

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "processing_time": "processing_time",
            "response": "response",
            "routing_info": "routing_info",
        }
        key_transform_with_dump = {
            "processing_time": "processing_time",
            "response": "response",
            "routing_info": "routing_info",
        }
