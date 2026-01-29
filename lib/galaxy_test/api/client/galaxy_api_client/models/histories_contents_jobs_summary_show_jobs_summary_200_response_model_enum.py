from enum import Enum, unique

__all__ = ["HistoriesContentsJobsSummaryShowJobsSummary200ResponseModelEnum"]


@unique
class HistoriesContentsJobsSummaryShowJobsSummary200ResponseModelEnum(str, Enum):
    """
    Discriminator enum for HistoriesContentsJobsSummaryShowJobsSummary200Response union
    types.

    Args:
        Job (str)                : Value for JOB
        ImplicitCollectionJobs (str)
                                 : Value for IMPLICITCOLLECTIONJOBS
        WorkflowInvocation (str) : Value for WORKFLOWINVOCATION
    """

    JOB = "Job"
    IMPLICITCOLLECTIONJOBS = "ImplicitCollectionJobs"
    WORKFLOWINVOCATION = "WorkflowInvocation"
