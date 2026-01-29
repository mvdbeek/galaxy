from dataclasses import dataclass

from .context import Context

__all__ = ["AgentQueryRequest"]


@dataclass
class AgentQueryRequest:
    """
    Request to query an AI agent.

    Args:
        query (str)              : The user's question or request
        agent_type (Optional[str]): Preferred agent type ('auto' for routing)
        context (Optional[Context])
                                 : Additional context for the query
        stream (Optional[bool])  : Whether to stream the response
    """

    query: str  # The user's question or request
    agent_type: str | None = "auto"  # Preferred agent type ('auto' for routing)
    context: Context | None = None  # Additional context for the query
    stream: bool | None = False  # Whether to stream the response
