from dataclasses import dataclass

from .agent_response import AgentResponse
from .processing_time import ProcessingTime
from .routing_info import RoutingInfo

__all__ = ["AgentQueryResponse"]


@dataclass
class AgentQueryResponse:
    """
    Response from an AI agent query.

    Args:
        response (AgentResponse) : Structured response from an AI agent.
        processing_time (Optional[ProcessingTime])
                                 : Time taken to process the query in seconds
        routing_info (Optional[RoutingInfo])
                                 : Information about how the query was routed
    """

    response: AgentResponse  # Structured response from an AI agent.
    processing_time: ProcessingTime | None = None  # Time taken to process the query in seconds
    routing_info: RoutingInfo | None = None  # Information about how the query was routed
