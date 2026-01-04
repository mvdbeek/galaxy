from typing import TypeAlias

from .help_forum_category import HelpForumCategory

__all__ = ["Categories"]

Categories: TypeAlias = list[HelpForumCategory] | None
"""Alias for The list of categories returned by the search."""
