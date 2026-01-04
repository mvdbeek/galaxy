from typing import TypeAlias

__all__ = ["JobsIndexParamUserId"]

JobsIndexParamUserId: TypeAlias = str | None
"""Alias for an encoded user id to restrict query to, must be own id if not admin user"""
