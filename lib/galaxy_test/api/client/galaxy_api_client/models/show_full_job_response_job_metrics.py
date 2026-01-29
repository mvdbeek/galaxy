from typing import TypeAlias

from .job_metric_collection import JobMetricCollection

__all__ = ["ShowFullJobResponseJobMetrics"]

ShowFullJobResponseJobMetrics: TypeAlias = JobMetricCollection | None
"""Alias for Collections of metrics provided by `JobInstrumenter` plugins on a particular job. Only administrators can see these metrics."""
