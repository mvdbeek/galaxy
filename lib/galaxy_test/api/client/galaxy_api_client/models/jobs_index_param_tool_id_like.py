from typing import TypeAlias

from .anonymous_array_item_208 import AnonymousArrayItem208

__all__ = ["JobsIndexParamToolIdLike"]

JobsIndexParamToolIdLike: TypeAlias = list[AnonymousArrayItem208] | None
"""Alias for Limit listing of jobs to those that match one of the included tool ID sql-like patterns. If none, all are returned"""
