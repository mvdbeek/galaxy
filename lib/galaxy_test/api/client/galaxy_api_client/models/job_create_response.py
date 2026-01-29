from dataclasses import dataclass

from .async_task_result_summary import AsyncTaskResultSummary

__all__ = ["JobCreateResponse"]


@dataclass
class JobCreateResponse:
    """
    JobCreateResponse dataclass

    Args:
        task_result (AsyncTaskResultSummary)
                                 :
        tool_request_id (str)    :
    """

    task_result: AsyncTaskResultSummary
    tool_request_id: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "task_result": "task_result",
            "tool_request_id": "tool_request_id",
        }
        key_transform_with_dump = {
            "task_result": "task_result",
            "tool_request_id": "tool_request_id",
        }
