from typing import TypeAlias

from .anonymous_array_item_206 import AnonymousArrayItem206

__all__ = ["JobsIndexParamToolId"]

JobsIndexParamToolId: TypeAlias = list[AnonymousArrayItem206] | None
"""Alias for Limit listing of jobs to those that match one of the included tool_ids. If none, all are returned"""
