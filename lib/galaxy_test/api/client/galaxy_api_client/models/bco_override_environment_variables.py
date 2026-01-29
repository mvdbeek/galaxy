from typing import Any, TypeAlias

__all__ = ["BcoOverrideEnvironmentVariables"]

BcoOverrideEnvironmentVariables: TypeAlias = dict[str, Any] | None
"""Alias for Override environment variables for 'execution_domain' when generating BioCompute object."""
