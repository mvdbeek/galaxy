from dataclasses import dataclass

from .action_suggestion_parameters import ActionSuggestionParameters
from .action_type import ActionType
from .confidence_level import ConfidenceLevel

__all__ = ["ActionSuggestion"]


@dataclass
class ActionSuggestion:
    """
    Structured suggestion for user action.

    Args:
        action_type (ActionType) : Types of actions agents can suggest.
        confidence (ConfidenceLevel)
                                 : Confidence levels for agent responses.
        description (str)        : Human-readable description of the action
        parameters (ActionSuggestionParameters | None)
                                 : Parameters for the action
        priority (int | None)    : Priority level (1=high, 2=medium, 3=low)
    """

    action_type: ActionType  # Types of actions agents can suggest.
    confidence: ConfidenceLevel  # Confidence levels for agent responses.
    description: str  # Human-readable description of the action
    parameters: ActionSuggestionParameters | None = None  # Parameters for the action
    priority: int | None = 1  # Priority level (1=high, 2=medium, 3=low)

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "confidence": "confidence",
            "description": "description",
            "parameters": "parameters",
            "priority": "priority",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "confidence": "confidence",
            "description": "description",
            "parameters": "parameters",
            "priority": "priority",
        }
