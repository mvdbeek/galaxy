from typing import TypeAlias

from .action_link import ActionLink

__all__ = ["ActionLinks"]

ActionLinks: TypeAlias = list[ActionLink] | None
"""Alias for The optional action links (buttons) to be displayed in the notification."""
