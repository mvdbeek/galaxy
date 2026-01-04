from dataclasses import dataclass

from .tools import Tools

__all__ = ["FavoriteObjectsSummary"]


@dataclass
class FavoriteObjectsSummary:
    """
    FavoriteObjectsSummary dataclass.

    Args:
        tools (Tools)            : The name of the tools the user favored.
    """

    tools: Tools  # The name of the tools the user favored.
