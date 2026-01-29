from typing import TypeAlias

from .help_forum_user import HelpForumUser

__all__ = ["Users"]

Users: TypeAlias = list[HelpForumUser] | None
"""Alias for The list of users returned by the search."""
