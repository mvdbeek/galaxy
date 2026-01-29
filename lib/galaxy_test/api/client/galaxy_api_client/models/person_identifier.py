from typing import TypeAlias

__all__ = ["PersonIdentifier"]

PersonIdentifier: TypeAlias = str | None
"""Alias for Identifier (typically an orcid.org ID)"""
