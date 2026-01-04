from typing import TypeAlias

from .async_task_result_summary import AsyncTaskResultSummary
from .notification_created_response import NotificationCreatedResponse

__all__ = ["NotificationsSendNotification200Response2"]

NotificationsSendNotification200Response2: TypeAlias = AsyncTaskResultSummary | NotificationCreatedResponse
