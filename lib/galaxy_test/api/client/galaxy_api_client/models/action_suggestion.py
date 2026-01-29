from dataclasses import dataclass

from .action_type import ActionType
from .confidence_level import ConfidenceLevel
from .parameters import Parameters

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
        parameters (Optional[Parameters])
                                 : Parameters for the action
        priority (Optional[int]) : Priority level (1=high, 2=medium, 3=low)
    """

    action_type: ActionType  # Types of actions agents can suggest.
    confidence: ConfidenceLevel  # Confidence levels for agent responses.
    description: str  # Human-readable description of the action
    parameters: Parameters | None = None  # Parameters for the action
    priority: int | None = 1  # Priority level (1=high, 2=medium, 3=low)
