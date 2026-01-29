from typing import TypeAlias

from .encoded_job_details import EncodedJobDetails
from .job_summary import JobSummary
from .show_full_job_response import ShowFullJobResponse

__all__ = ["AnonymousArrayItem115"]

AnonymousArrayItem115: TypeAlias = ShowFullJobResponse | EncodedJobDetails | JobSummary
