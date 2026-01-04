from typing import TypeAlias

__all__ = ["JobsIndexParamImplicitCollectionJobsId"]

JobsIndexParamImplicitCollectionJobsId: TypeAlias = str | None
"""Alias for Limit listing of jobs to those that match the specified implicit collection job ID. If none, jobs from any implicit collection execution (or from no implicit collection execution) may be returned."""
