from typing import TypeAlias

__all__ = ["UsernameAndSlug"]

UsernameAndSlug: TypeAlias = str | None
"""Alias for The relative URL in the form of /u/{username}/{resource_single_char}/{slug}"""
