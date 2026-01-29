from typing import TypeAlias

__all__ = ["VariableResponseValue"]

VariableResponseValue: TypeAlias = str | None
"""Alias for The value of the variable (for variables, not secrets)."""
