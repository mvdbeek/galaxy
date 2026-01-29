from typing import TypeAlias

from .help_forum_group import HelpForumGroup

__all__ = ["HelpForumSearchResponseGroups"]

HelpForumSearchResponseGroups: TypeAlias = list[HelpForumGroup] | None
"""Alias for The list of groups returned by the search."""
