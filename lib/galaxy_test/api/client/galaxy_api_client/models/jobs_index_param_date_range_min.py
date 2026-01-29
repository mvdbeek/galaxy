from datetime import date, datetime
from typing import TypeAlias

__all__ = ["JobsIndexParamDateRangeMin"]

JobsIndexParamDateRangeMin: TypeAlias = date | datetime | None
"""Alias for Limit listing of jobs to those that are updated after specified date (e.g. '2014-01-01')"""
