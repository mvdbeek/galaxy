from typing import TypeAlias

from .async_task_result_summary import AsyncTaskResultSummary
from .notification_created_response import NotificationCreatedResponse

__all__ = ["NotificationsSendNotification200Response"]

NotificationsSendNotification200Response: TypeAlias = NotificationCreatedResponse | AsyncTaskResultSummary
