from dataclasses import dataclass, field

from .action_suggestion import ActionSuggestion
from .confidence_level import ConfidenceLevel
from .metadata import Metadata
from .reasoning import Reasoning

__all__ = ["AgentResponse"]


@dataclass
class AgentResponse:
    """
    Structured response from an AI agent.

    Args:
        agent_type (str)         : Type of agent that generated this response
        confidence (ConfidenceLevel)
                                 : Confidence levels for agent responses.
        content (str)            : Main response content
        metadata (Optional[Metadata])
                                 : Additional metadata
        reasoning (Optional[Reasoning])
                                 : Explanation of the agent's reasoning
        suggestions (Optional[List[ActionSuggestion]])
                                 : Actionable suggestions
    """

    agent_type: str  # Type of agent that generated this response
    confidence: ConfidenceLevel  # Confidence levels for agent responses.
    content: str  # Main response content
    metadata: Metadata | None = None  # Additional metadata
    reasoning: Reasoning | None = None  # Explanation of the agent's reasoning
    suggestions: list[ActionSuggestion] | None = field(default_factory=list)  # Actionable suggestions
