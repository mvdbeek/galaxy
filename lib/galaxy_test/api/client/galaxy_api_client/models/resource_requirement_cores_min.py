from typing import TypeAlias

__all__ = ["ResourceRequirementCoresMin"]

ResourceRequirementCoresMin: TypeAlias = int | float | None
"""Alias for Minimum reserved number of CPU cores.
May be a fractional value to indicate to a scheduling algorithm that one core can be allocated to multiple jobs. For example, a value of 0.25 indicates that up to 4 jobs may run in parallel on 1 core. A value of 1.25 means that up to 3 jobs can run on a 4 core system (4/1.25 ≈ 3).
The reported number of CPU cores reserved for the process is a non-zero integer calculated by rounding up the cores request to the next whole number.
"""
