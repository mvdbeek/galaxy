from enum import Enum, unique

__all__ = ["AnonymousArrayItem111ModelEnum"]


@unique
class AnonymousArrayItem111ModelEnum(str, Enum):
    """
    Discriminator enum for AnonymousArrayItem111 union types.

    Args:
        Job (str)                : Value for JOB
        ImplicitCollectionJobs (str)
                                 : Value for IMPLICITCOLLECTIONJOBS
        WorkflowInvocation (str) : Value for WORKFLOWINVOCATION
    """

    JOB = "Job"
    IMPLICITCOLLECTIONJOBS = "ImplicitCollectionJobs"
    WORKFLOWINVOCATION = "WorkflowInvocation"
