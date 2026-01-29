from typing import TypeAlias

from .help_forum_tag import HelpForumTag

__all__ = ["HelpForumSearchResponseTags"]

HelpForumSearchResponseTags: TypeAlias = list[HelpForumTag] | None
"""Alias for The list of tags returned by the search."""
