from dataclasses import dataclass

from .name import Name
from .queue import Queue

__all__ = ["AsyncTaskResultSummary"]


@dataclass
class AsyncTaskResultSummary:
    """
    AsyncTaskResultSummary dataclass.

    Args:
        id_ (str)                : Celery AsyncResult ID for this task
        ignored (bool)           : Indicated whether the Celery AsyncResult will be
                                   available for retrieval
        name (Optional[Name])    : The name of the creator.
        queue (Optional[Queue])  :
    """

    id_: str  # Celery AsyncResult ID for this task
    ignored: bool  # Indicated whether the Celery AsyncResult will be available for retrieval
    name: Name | None = None  # The name of the creator.
    queue: Queue | None = None
