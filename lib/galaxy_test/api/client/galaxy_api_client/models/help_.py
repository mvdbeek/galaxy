from typing import TypeAlias

from .help_content import HelpContent

__all__ = ["Help_"]

Help_: TypeAlias = HelpContent | None
"""Alias for Help text shown below the tool interface."""
