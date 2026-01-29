from dataclasses import dataclass

from .model_ import Model_
from .specialties import Specialties

__all__ = ["AvailableAgent"]


@dataclass
class AvailableAgent:
    """
    Information about an available agent.

    Args:
        agent_type (str)         : Unique identifier for the agent
        description (str)        : Description of the agent's capabilities
        enabled (bool)           : Whether the agent is currently enabled
        name (str)               : Human-readable name
        model_ (Optional[Model_]): LLM model used by the agent
        specialties (Optional[Specialties])
                                 : Areas of specialization
    """

    agent_type: str  # Unique identifier for the agent
    description: str  # Description of the agent's capabilities
    enabled: bool  # Whether the agent is currently enabled
    name: str  # Human-readable name
    model_: Model_ | None = None  # LLM model used by the agent
    specialties: Specialties | None = None  # Areas of specialization
