from dataclasses import dataclass

from .available_agent import AvailableAgent

__all__ = ["AgentListResponse"]


@dataclass
class AgentListResponse:
    """
    Response listing available agents.

    Args:
        agents (List[AvailableAgent])
                                 : List of available agents
        total_count (int)        : Total number of agents
    """

    agents: list[AvailableAgent]  # List of available agents
    total_count: int  # Total number of agents

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "agents": "agents",
            "total_count": "total_count",
        }
        key_transform_with_dump = {
            "agents": "agents",
            "total_count": "total_count",
        }
