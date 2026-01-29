from dataclasses import dataclass

from .body_ai_agents_custom_tool_create_custom_tool_context import BodyAiAgentsCustomToolCreateCustomToolContext

__all__ = ["BodyAiAgentsCustomToolCreateCustomTool2"]


@dataclass
class BodyAiAgentsCustomToolCreateCustomTool2:
    """
    BodyAiAgentsCustomToolCreateCustomTool2 dataclass

    Args:
        query (str)              : Description of the tool to create
        context (BodyAiAgentsCustomToolCreateCustomToolContext | None)
                                 : Additional context for tool creation
    """

    query: str  # Description of the tool to create
    context: BodyAiAgentsCustomToolCreateCustomToolContext | None = None  # Additional context for tool creation

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "context": "context",
            "query": "query",
        }
        key_transform_with_dump = {
            "context": "context",
            "query": "query",
        }
