from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.create_metrics_payload import CreateMetricsPayload
from ..models.metrics_create_param_run_as import MetricsCreateParamRunAs


@runtime_checkable
class MetricsClientProtocol(Protocol):
    """Protocol defining the interface of MetricsClient for dependency injection."""

    async def metrics_create(
        self,
        body: CreateMetricsPayload,
        run_as: MetricsCreateParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def metrics_create(
        self,
        body: CreateMetricsPayload,
        run_as: MetricsCreateParamRunAs | None = None,
    ) -> dict[str, Any]: ...


class MetricsClient(MetricsClientProtocol):
    """Client for metrics endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def metrics_create(
        self,
        body: CreateMetricsPayload,
        run_as: MetricsCreateParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Records a collection of metrics.

        Record any metrics sent and return some status object.

        Args:
            run-as (MetricsCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateMetricsPayload)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/metrics"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateMetricsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def metrics_create(
        self,
        body: CreateMetricsPayload,
        run_as: MetricsCreateParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Records a collection of metrics.

        Record any metrics sent and return some status object.

        Args:
            run-as (MetricsCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateMetricsPayload)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/metrics"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateMetricsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
