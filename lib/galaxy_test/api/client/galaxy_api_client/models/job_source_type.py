from enum import Enum, unique

__all__ = ["JobSourceType"]


@unique
class JobSourceType(str, Enum):
    """
    Available types of job sources (model classes) that produce dataset collections.

    Args:
        Job (str)                : Value for JOB
        ImplicitCollectionJobs (str)
                                 : Value for IMPLICITCOLLECTIONJOBS
        WorkflowInvocation (str) : Value for WORKFLOWINVOCATION
    """

    JOB = "Job"
    IMPLICITCOLLECTIONJOBS = "ImplicitCollectionJobs"
    WORKFLOWINVOCATION = "WorkflowInvocation"
