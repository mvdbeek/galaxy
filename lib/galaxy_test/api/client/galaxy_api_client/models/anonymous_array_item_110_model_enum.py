from enum import Enum, unique

__all__ = ["AnonymousArrayItem110ModelEnum"]


@unique
class AnonymousArrayItem110ModelEnum(str, Enum):
    """
    Discriminator enum for AnonymousArrayItem110 union types.

    Args:
        Job (str)                : Value for JOB
        ImplicitCollectionJobs (str)
                                 : Value for IMPLICITCOLLECTIONJOBS
        WorkflowInvocation (str) : Value for WORKFLOWINVOCATION
    """

    JOB = "Job"
    IMPLICITCOLLECTIONJOBS = "ImplicitCollectionJobs"
    WORKFLOWINVOCATION = "WorkflowInvocation"
