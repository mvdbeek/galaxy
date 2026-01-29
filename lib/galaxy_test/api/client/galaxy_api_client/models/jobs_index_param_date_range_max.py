from datetime import date, datetime
from typing import TypeAlias

__all__ = ["JobsIndexParamDateRangeMax"]

JobsIndexParamDateRangeMax: TypeAlias = datetime | date | None
"""Alias for Limit listing of jobs to those that are updated before specified date (e.g. '2014-01-01')"""
