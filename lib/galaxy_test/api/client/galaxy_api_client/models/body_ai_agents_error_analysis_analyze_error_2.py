from dataclasses import dataclass

from .body_ai_agents_error_analysis_analyze_error_error_details import BodyAiAgentsErrorAnalysisAnalyzeErrorErrorDetails
from .body_ai_agents_error_analysis_analyze_error_job_id import BodyAiAgentsErrorAnalysisAnalyzeErrorJobId

__all__ = ["BodyAiAgentsErrorAnalysisAnalyzeError2"]


@dataclass
class BodyAiAgentsErrorAnalysisAnalyzeError2:
    """
    BodyAiAgentsErrorAnalysisAnalyzeError2 dataclass

    Args:
        query (str)              : Description of the error or problem
        error_details (BodyAiAgentsErrorAnalysisAnalyzeErrorErrorDetails | None)
                                 : Additional error details
        job_id (BodyAiAgentsErrorAnalysisAnalyzeErrorJobId | None)
                                 : Job ID for context
    """

    query: str  # Description of the error or problem
    error_details: BodyAiAgentsErrorAnalysisAnalyzeErrorErrorDetails | None = None  # Additional error details
    job_id: BodyAiAgentsErrorAnalysisAnalyzeErrorJobId | None = None  # Job ID for context

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "error_details": "error_details",
            "job_id": "job_id",
            "query": "query",
        }
        key_transform_with_dump = {
            "error_details": "error_details",
            "job_id": "job_id",
            "query": "query",
        }
