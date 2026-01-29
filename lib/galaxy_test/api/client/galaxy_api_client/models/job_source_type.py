from typing import Optional, TypeAlias

__all__ = ["JobSourceType"]

JobSourceType: TypeAlias = Optional["JobSourceType"]
"""Alias for The type of job (model class) that produced this dataset collection. Used to track the state of the job."""
