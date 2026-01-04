from typing import TypeAlias

from .implicit_collection_jobs_state_summary import ImplicitCollectionJobsStateSummary
from .job_state_summary import JobStateSummary
from .workflow_invocation_state_summary import WorkflowInvocationStateSummary

__all__ = ["AnonymousArrayItem199"]

AnonymousArrayItem199: TypeAlias = ImplicitCollectionJobsStateSummary | JobStateSummary | WorkflowInvocationStateSummary
