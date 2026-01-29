from dataclasses import dataclass

from .context import Context

__all__ = ["BodyAiAgentsCustomToolCreateCustomTool2"]


@dataclass
class BodyAiAgentsCustomToolCreateCustomTool2:
    """
    BodyAiAgentsCustomToolCreateCustomTool2 dataclass.

    Args:
        query (str)              : Description of the tool to create
        context (Optional[Context])
                                 : The context for the chatbot.
    """

    query: str  # Description of the tool to create
    context: Context | None = ""  # The context for the chatbot.
