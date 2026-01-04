from typing import TypeAlias

from .encoded_job_details import EncodedJobDetails
from .show_full_job_response import ShowFullJobResponse

__all__ = ["JobsShow200Response2"]

JobsShow200Response2: TypeAlias = EncodedJobDetails | ShowFullJobResponse
