from dataclasses import dataclass, field

from .model_ import Model_

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
        model_ (Model_ | None)   : LLM model used by the agent (maps from 'model')
        specialties (List[str] | None)
                                 : Areas of specialization
    """

    agent_type: str  # Unique identifier for the agent
    description: str  # Description of the agent's capabilities
    enabled: bool  # Whether the agent is currently enabled
    name: str  # Human-readable name
    model_: Model_ | None = None  # LLM model used by the agent (maps from 'model')
    specialties: list[str] | None = field(default_factory=list)  # Areas of specialization

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "agent_type": "agent_type",
            "description": "description",
            "enabled": "enabled",
            "model": "model_",
            "name": "name",
            "specialties": "specialties",
        }
        key_transform_with_dump = {
            "agent_type": "agent_type",
            "description": "description",
            "enabled": "enabled",
            "model_": "model",
            "name": "name",
            "specialties": "specialties",
        }
