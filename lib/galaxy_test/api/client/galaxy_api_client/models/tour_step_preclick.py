from typing import TypeAlias

__all__ = ["TourStepPreclick"]

TourStepPreclick: TypeAlias = bool | list[str] | None
"""Alias for Elements that receive a click() event before the step is shown"""
