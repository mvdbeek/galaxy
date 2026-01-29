from typing import TypeAlias

from .dataset_source_type import DatasetSourceType

__all__ = ["JobsMetricsMetricsByJobParamHdaLdda"]

JobsMetricsMetricsByJobParamHdaLdda: TypeAlias = DatasetSourceType | None
"""Alias for Whether this dataset belongs to a history (HDA) or a library (LDDA)."""
