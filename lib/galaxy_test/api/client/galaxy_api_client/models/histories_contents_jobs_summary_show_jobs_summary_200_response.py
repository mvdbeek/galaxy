from dataclasses import dataclass
from typing import Annotated, TypeAlias

from .implicit_collection_jobs_state_summary import ImplicitCollectionJobsStateSummary
from .job_state_summary import JobStateSummary
from .workflow_invocation_state_summary import WorkflowInvocationStateSummary

__all__ = [
    "HistoriesContentsJobsSummaryShowJobsSummary200Response",
    "HistoriesContentsJobsSummaryShowJobsSummary200ResponseDiscriminator",
]


@dataclass(frozen=True)
class HistoriesContentsJobsSummaryShowJobsSummary200ResponseDiscriminator:
    """Discriminator metadata for HistoriesContentsJobsSummaryShowJobsSummary200Response union."""

    property_name: str = "model"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("ImplicitCollectionJobs", "ImplicitCollectionJobsStateSummary"),
        ("Job", "JobStateSummary"),
        ("WorkflowInvocation", "WorkflowInvocationStateSummary"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .implicit_collection_jobs_state_summary import ImplicitCollectionJobsStateSummary
        from .job_state_summary import JobStateSummary
        from .workflow_invocation_state_summary import WorkflowInvocationStateSummary

        return {
            "ImplicitCollectionJobs": ImplicitCollectionJobsStateSummary,
            "Job": JobStateSummary,
            "WorkflowInvocation": WorkflowInvocationStateSummary,
        }


HistoriesContentsJobsSummaryShowJobsSummary200Response: TypeAlias = Annotated[
    JobStateSummary | ImplicitCollectionJobsStateSummary | WorkflowInvocationStateSummary,
    HistoriesContentsJobsSummaryShowJobsSummary200ResponseDiscriminator(),
]
