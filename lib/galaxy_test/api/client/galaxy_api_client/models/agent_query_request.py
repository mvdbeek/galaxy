from dataclasses import dataclass

from .agent_query_request_context import AgentQueryRequestContext

__all__ = ["AgentQueryRequest"]


@dataclass
class AgentQueryRequest:
    """
    Request to query an AI agent.

    Args:
        query (str)              : The user's question or request
        agent_type (str | None)  : Preferred agent type ('auto' for routing)
        context (AgentQueryRequestContext | None)
                                 : Additional context for the query
        stream (bool | None)     : Whether to stream the response
    """

    query: str  # The user's question or request
    agent_type: str | None = "auto"  # Preferred agent type ('auto' for routing)
    context: AgentQueryRequestContext | None = None  # Additional context for the query
    stream: bool | None = False  # Whether to stream the response

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "agent_type": "agent_type",
            "context": "context",
            "query": "query",
            "stream": "stream",
        }
        key_transform_with_dump = {
            "agent_type": "agent_type",
            "context": "context",
            "query": "query",
            "stream": "stream",
        }
