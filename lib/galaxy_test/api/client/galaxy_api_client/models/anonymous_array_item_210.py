from typing import TypeAlias

from .encoded_job_details import EncodedJobDetails
from .job_summary import JobSummary
from .show_full_job_response import ShowFullJobResponse

__all__ = ["AnonymousArrayItem210"]

AnonymousArrayItem210: TypeAlias = EncodedJobDetails | JobSummary | ShowFullJobResponse
