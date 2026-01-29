from dataclasses import dataclass

__all__ = ["FavoriteObjectsSummary"]


@dataclass
class FavoriteObjectsSummary:
    """
    FavoriteObjectsSummary dataclass

    Args:
        tools (List[str])        : The name of the tools the user favored.
    """

    tools: list[str]  # The name of the tools the user favored.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "tools": "tools",
        }
        key_transform_with_dump = {
            "tools": "tools",
        }
