from dataclasses import dataclass

from .async_task_result_summary_name import AsyncTaskResultSummaryName
from .async_task_result_summary_queue import AsyncTaskResultSummaryQueue

__all__ = ["AsyncTaskResultSummary"]


@dataclass
class AsyncTaskResultSummary:
    """
    AsyncTaskResultSummary dataclass

    Args:
        id_ (str)                : Celery AsyncResult ID for this task (maps from 'id')
        ignored (bool)           : Indicated whether the Celery AsyncResult will be
                                   available for retrieval
        name (AsyncTaskResultSummaryName | None)
                                 :
        queue (AsyncTaskResultSummaryQueue | None)
                                 :
    """

    id_: str  # Celery AsyncResult ID for this task (maps from 'id')
    ignored: bool  # Indicated whether the Celery AsyncResult will be available for retrieval
    name: AsyncTaskResultSummaryName | None = None
    queue: AsyncTaskResultSummaryQueue | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "ignored": "ignored",
            "name": "name",
            "queue": "queue",
        }
        key_transform_with_dump = {
            "id_": "id",
            "ignored": "ignored",
            "name": "name",
            "queue": "queue",
        }
