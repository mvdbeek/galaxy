from typing import TypeAlias

from .anonymous_array_item_61 import AnonymousArrayItem61

__all__ = ["JobParameterValue"]

JobParameterValue: TypeAlias = list[AnonymousArrayItem61] | float | int | bool | str | None
"""Alias for The values of the job parameter"""
