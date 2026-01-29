from dataclasses import dataclass, field

from .action_suggestion import ActionSuggestion
from .agent_response_metadata import AgentResponseMetadata
from .agent_response_reasoning import AgentResponseReasoning
from .confidence_level import ConfidenceLevel

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
        metadata (AgentResponseMetadata | None)
                                 : Additional metadata
        reasoning (AgentResponseReasoning | None)
                                 : Explanation of the agent's reasoning
        suggestions (List[ActionSuggestion] | None)
                                 : Actionable suggestions
    """

    agent_type: str  # Type of agent that generated this response
    confidence: ConfidenceLevel  # Confidence levels for agent responses.
    content: str  # Main response content
    metadata: AgentResponseMetadata | None = None  # Additional metadata
    reasoning: AgentResponseReasoning | None = None  # Explanation of the agent's reasoning
    suggestions: list[ActionSuggestion] | None = field(default_factory=list)  # Actionable suggestions

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "agent_type": "agent_type",
            "confidence": "confidence",
            "content": "content",
            "metadata": "metadata",
            "reasoning": "reasoning",
            "suggestions": "suggestions",
        }
        key_transform_with_dump = {
            "agent_type": "agent_type",
            "confidence": "confidence",
            "content": "content",
            "metadata": "metadata",
            "reasoning": "reasoning",
            "suggestions": "suggestions",
        }
