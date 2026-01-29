from typing import TypeAlias

__all__ = ["ResourceRequirementRamMin"]

ResourceRequirementRamMin: TypeAlias = int | float | None
"""Alias for Minimum reserved RAM in mebibytes (2**20).
May be a fractional value. If so, the actual RAM request is rounded up to the next whole number. The reported amount of RAM reserved for the process is a non-zero integer."""
