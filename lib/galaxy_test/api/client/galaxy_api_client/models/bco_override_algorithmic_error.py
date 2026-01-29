from typing import Any, TypeAlias

__all__ = ["BcoOverrideAlgorithmicError"]

BcoOverrideAlgorithmicError: TypeAlias = dict[str, Any] | None
"""Alias for Override algorithmic error for 'error domain' when generating BioCompute object."""
