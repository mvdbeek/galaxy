from typing import TypeAlias

from .job_metric import JobMetric

__all__ = ["JobMetricCollection"]

JobMetricCollection: TypeAlias = list[JobMetric]
"""Alias for Represents a collection of metrics associated with a Job."""
