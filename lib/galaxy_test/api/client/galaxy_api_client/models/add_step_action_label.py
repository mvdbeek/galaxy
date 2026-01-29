from typing import TypeAlias

__all__ = ["AddStepActionLabel"]

AddStepActionLabel: TypeAlias = str | None
"""Alias for A unique label for the step being added, must be distinct from the labels already present in the workflow."""
