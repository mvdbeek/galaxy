from enum import Enum


class JobSourceType(str, Enum):
    IMPLICITCOLLECTIONJOBS = "ImplicitCollectionJobs"
    JOB = "Job"
    WORKFLOWINVOCATION = "WorkflowInvocation"

    def __str__(self) -> str:
        return str(self.value)
