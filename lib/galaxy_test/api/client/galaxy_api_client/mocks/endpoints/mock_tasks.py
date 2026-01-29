from typing import TYPE_CHECKING
from uuid import UUID

from ...models.task_result import TaskResult
from ...models.task_state import TaskState

if TYPE_CHECKING:
    pass


class MockTasksClient:
    """
    Mock implementation of TasksClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestTasksClient(MockTasksClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def tasks_result_get_result(
        self,
        task_id: UUID,
    ) -> TaskResult:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockTasksClient.tasks_result_get_result() not implemented. Override this method in your test subclass."
        )

    async def tasks_state_state(
        self,
        task_id: UUID,
    ) -> TaskState:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockTasksClient.tasks_state_state() not implemented. Override this method in your test subclass."
        )
