from typing import TypeAlias

from .implicit_collection_jobs_state_summary import ImplicitCollectionJobsStateSummary
from .job_state_summary import JobStateSummary
from .workflow_invocation_state_summary import WorkflowInvocationStateSummary

__all__ = ["HistoriesContentsJobsSummaryShowJobsSummary200Response2"]

HistoriesContentsJobsSummaryShowJobsSummary200Response2: TypeAlias = (
    ImplicitCollectionJobsStateSummary | JobStateSummary | WorkflowInvocationStateSummary
)
