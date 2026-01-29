from dataclasses import dataclass

from .async_task_result_summary import AsyncTaskResultSummary

__all__ = ["JobCreateResponse"]


@dataclass
class JobCreateResponse:
    """
    JobCreateResponse dataclass.

    Args:
        task_result (AsyncTaskResultSummary)
                                 :
        tool_request_id (str)    :
    """

    task_result: AsyncTaskResultSummary
    tool_request_id: str
