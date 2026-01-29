from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.job_lock import JobLock
from ..models.job_lock_job_lock_status_param_run_as import JobLockJobLockStatusParamRunAs
from ..models.job_lock_update_job_lock_param_run_as import JobLockUpdateJobLockParamRunAs


@runtime_checkable
class JobLockClientProtocol(Protocol):
    """Protocol defining the interface of JobLockClient for dependency injection."""

    async def job_lock_job_lock_status(
        self,
        run_as: JobLockJobLockStatusParamRunAs | None = None,
    ) -> "JobLock": ...

    async def job_lock_update_job_lock(
        self,
        body: "JobLock",
        run_as: JobLockUpdateJobLockParamRunAs | None = None,
    ) -> "JobLock": ...


class JobLockClient(JobLockClientProtocol):
    """Client for job_lock endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def job_lock_job_lock_status(
        self,
        run_as: JobLockJobLockStatusParamRunAs | None = None,
    ) -> "JobLock":
        """
        Job Lock Status

        Get job lock status.

        Args:
            run-as (JobLockJobLockStatusParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            "JobLock": Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/job_lock"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast("JobLock", response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def job_lock_update_job_lock(
        self,
        body: "JobLock",
        run_as: JobLockUpdateJobLockParamRunAs | None = None,
    ) -> "JobLock":
        """
        Update Job Lock

        Set job lock status.

        Args:
            run-as (JobLockUpdateJobLockParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body ("JobLock")         : Request body. (json)

        Returns:
            "JobLock": Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/job_lock"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: JobLock = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast("JobLock", response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
