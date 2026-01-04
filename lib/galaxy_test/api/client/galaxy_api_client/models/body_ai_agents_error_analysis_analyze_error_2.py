from dataclasses import dataclass

from .error_details import ErrorDetails
from .job_id import JobId

__all__ = ["BodyAiAgentsErrorAnalysisAnalyzeError2"]


@dataclass
class BodyAiAgentsErrorAnalysisAnalyzeError2:
    """
    BodyAiAgentsErrorAnalysisAnalyzeError2 dataclass.

    Args:
        query (str)              : Description of the error or problem
        error_details (Optional[ErrorDetails])
                                 : Additional error details
        job_id (Optional[JobId]) : The encoded ID of the job associated with this workflow
                                   invocation step.
    """

    query: str  # Description of the error or problem
    error_details: ErrorDetails | None = None  # Additional error details
    job_id: JobId | None = None  # The encoded ID of the job associated with this workflow invocation step.
