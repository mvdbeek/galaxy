from dataclasses import dataclass
from uuid import UUID

from .async_task_result_summary import AsyncTaskResultSummary

__all__ = ["AsyncFile"]


@dataclass
class AsyncFile:
    """
    AsyncFile dataclass.

    Args:
        storage_request_id (UUID):
        task (AsyncTaskResultSummary)
                                 :
    """

    storage_request_id: UUID
    task: AsyncTaskResultSummary
