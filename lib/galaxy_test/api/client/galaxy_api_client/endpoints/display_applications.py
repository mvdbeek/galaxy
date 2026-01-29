from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.create_link_feedback import CreateLinkFeedback
from ..models.create_link_incoming import CreateLinkIncoming
from ..models.display_application import DisplayApplication
from ..models.display_applications_create_link_create_link_param_run_as import (
    DisplayApplicationsCreateLinkCreateLinkParamRunAs,
)
from ..models.display_applications_reload_reload_param_run_as import DisplayApplicationsReloadReloadParamRunAs
from ..models.display_applications_reload_reload_request_body import DisplayApplicationsReloadReloadRequestBody
from ..models.reload_feedback import ReloadFeedback


@runtime_checkable
class DisplayApplicationsClientProtocol(Protocol):
    """Protocol defining the interface of DisplayApplicationsClient for dependency injection."""

    async def display_applications_index(
        self,
    ) -> list[DisplayApplication]: ...

    async def display_applications_index(
        self,
    ) -> list[DisplayApplication]: ...

    async def display_applications_create_link_create_link(
        self,
        body: CreateLinkIncoming,
        run_as: DisplayApplicationsCreateLinkCreateLinkParamRunAs | None = None,
    ) -> CreateLinkFeedback: ...

    async def display_applications_create_link_create_link(
        self,
        body: CreateLinkIncoming,
        run_as: DisplayApplicationsCreateLinkCreateLinkParamRunAs | None = None,
    ) -> CreateLinkFeedback: ...

    async def display_applications_reload_reload(
        self,
        run_as: DisplayApplicationsReloadReloadParamRunAs | None = None,
        body: DisplayApplicationsReloadReloadRequestBody | None = None,
    ) -> ReloadFeedback: ...

    async def display_applications_reload_reload(
        self,
        run_as: DisplayApplicationsReloadReloadParamRunAs | None = None,
        body: DisplayApplicationsReloadReloadRequestBody | None = None,
    ) -> ReloadFeedback: ...


class DisplayApplicationsClient(DisplayApplicationsClientProtocol):
    """Client for display_applications endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def display_applications_index(
        self,
    ) -> list[DisplayApplication]:
        """
        Returns the list of display applications.

        Returns the list of display applications.

        Returns:
            List[DisplayApplication]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/display_applications"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[DisplayApplication])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def display_applications_index(
        self,
    ) -> list[DisplayApplication]:
        """
        Returns the list of display applications.

        Returns the list of display applications.

        Returns:
            List[DisplayApplication]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/display_applications"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[DisplayApplication])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def display_applications_create_link_create_link(
        self,
        body: CreateLinkIncoming,
        run_as: DisplayApplicationsCreateLinkCreateLinkParamRunAs | None = None,
    ) -> CreateLinkFeedback:
        """
        Creates a link for display applications.

        Creates a link for display applications.

        Args:
            run-as (DisplayApplicationsCreateLinkCreateLinkParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateLinkIncoming): Request body. (json)

        Returns:
            CreateLinkFeedback: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/display_applications/create_link"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateLinkIncoming = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CreateLinkFeedback)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def display_applications_create_link_create_link(
        self,
        body: CreateLinkIncoming,
        run_as: DisplayApplicationsCreateLinkCreateLinkParamRunAs | None = None,
    ) -> CreateLinkFeedback:
        """
        Creates a link for display applications.

        Creates a link for display applications.

        Args:
            run-as (DisplayApplicationsCreateLinkCreateLinkParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateLinkIncoming): Request body. (json)

        Returns:
            CreateLinkFeedback: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/display_applications/create_link"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateLinkIncoming = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CreateLinkFeedback)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def display_applications_reload_reload(
        self,
        run_as: DisplayApplicationsReloadReloadParamRunAs | None = None,
        body: DisplayApplicationsReloadReloadRequestBody | None = None,
    ) -> ReloadFeedback:
        """
        Reloads the list of display applications.

        Reloads the list of display applications.

        Args:
            run-as (DisplayApplicationsReloadReloadParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DisplayApplicationsReloadReloadRequestBody | None)
                                     : Request body. (json)

        Returns:
            ReloadFeedback: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/display_applications/reload"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DisplayApplicationsReloadReloadRequestBody | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ReloadFeedback)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def display_applications_reload_reload(
        self,
        run_as: DisplayApplicationsReloadReloadParamRunAs | None = None,
        body: DisplayApplicationsReloadReloadRequestBody | None = None,
    ) -> ReloadFeedback:
        """
        Reloads the list of display applications.

        Reloads the list of display applications.

        Args:
            run-as (DisplayApplicationsReloadReloadParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DisplayApplicationsReloadReloadRequestBody | None)
                                     : Request body. (json)

        Returns:
            ReloadFeedback: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/display_applications/reload"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DisplayApplicationsReloadReloadRequestBody | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ReloadFeedback)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
