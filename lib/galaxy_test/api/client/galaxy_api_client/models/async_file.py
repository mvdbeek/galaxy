from dataclasses import dataclass
from uuid import UUID

from .async_task_result_summary import AsyncTaskResultSummary

__all__ = ["AsyncFile"]


@dataclass
class AsyncFile:
    """
    AsyncFile dataclass

    Args:
        storage_request_id (UUID):
        task (AsyncTaskResultSummary)
                                 :
    """

    storage_request_id: UUID
    task: AsyncTaskResultSummary

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "storage_request_id": "storage_request_id",
            "task": "task",
        }
        key_transform_with_dump = {
            "storage_request_id": "storage_request_id",
            "task": "task",
        }
