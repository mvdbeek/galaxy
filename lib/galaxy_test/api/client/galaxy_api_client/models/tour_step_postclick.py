from typing import TypeAlias

__all__ = ["TourStepPostclick"]

TourStepPostclick: TypeAlias = bool | list[str] | None
"""Alias for Elements that receive a click() event after the step is shown"""
