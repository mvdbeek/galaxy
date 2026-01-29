from typing import cast
from uuid import UUID

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport

from ..models.task_result import TaskResult
from ..models.task_state import TaskState


class TasksClient:
    """Client for tasks endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def tasks_result_get_result_2_2(
        self,
        task_id: UUID,
    ) -> TaskResult:
        """
        Get result message for task ID

        If the task is still running, pending, or is waiting for retry then the result is an
        empty string. If the task failed, the result is an error message.

        Args:
            task_id (UUID)           :

        Returns:
            TaskResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tasks/{task_id}/result"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(TaskResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tasks_result_get_result_2_2(
        self,
        task_id: UUID,
    ) -> TaskResult:
        """
        Get result message for task ID

        If the task is still running, pending, or is waiting for retry then the result is an
        empty string. If the task failed, the result is an error message.

        Args:
            task_id (UUID)           :

        Returns:
            TaskResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tasks/{task_id}/result"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(TaskResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tasks_state_state_2_2(
        self,
        task_id: UUID,
    ) -> TaskState:
        """
        Determine state of task ID

        Args:
            task_id (UUID)           :

        Returns:
            TaskState: String indicating task state.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tasks/{task_id}/state"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(TaskState, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tasks_state_state_2_2(
        self,
        task_id: UUID,
    ) -> TaskState:
        """
        Determine state of task ID

        Args:
            task_id (UUID)           :

        Returns:
            TaskState: String indicating task state.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tasks/{task_id}/state"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(TaskState, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
