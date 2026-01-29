from typing import TypeAlias

from .help_content import HelpContent

__all__ = ["Help43"]

Help43: TypeAlias = HelpContent | None
"""Alias for Help text shown below the tool interface."""
