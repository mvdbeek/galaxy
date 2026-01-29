from typing import TypeAlias

__all__ = ["ExtraFilesFuzzyRoot"]

ExtraFilesFuzzyRoot: TypeAlias = bool | None
"""Alias for Prevent Galaxy from checking for a single file in a directory and re-interpreting the archive"""
