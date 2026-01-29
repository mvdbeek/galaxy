from typing import TypeAlias

from .job_source_type import JobSourceType

__all__ = ["HdcaSummaryJobSourceType"]

HdcaSummaryJobSourceType: TypeAlias = JobSourceType | None
"""Alias for The type of job (model class) that produced this dataset collection. Used to track the state of the job."""
