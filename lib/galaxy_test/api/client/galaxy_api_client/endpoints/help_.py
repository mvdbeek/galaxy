from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.help_forum_search_response import HelpForumSearchResponse
from ..models.help_forum_search_search_forum_param_run_as import HelpForumSearchSearchForumParamRunAs


@runtime_checkable
class Help_ClientProtocol(Protocol):
    """Protocol defining the interface of Help_Client for dependency injection."""

    async def help_forum_search_search_forum(
        self,
        query: str,
        run_as: HelpForumSearchSearchForumParamRunAs | None = None,
    ) -> HelpForumSearchResponse: ...

    async def help_forum_search_search_forum(
        self,
        query: str,
        run_as: HelpForumSearchSearchForumParamRunAs | None = None,
    ) -> HelpForumSearchResponse: ...


class Help_Client(Help_ClientProtocol):
    """Client for help endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def help_forum_search_search_forum(
        self,
        query: str,
        run_as: HelpForumSearchSearchForumParamRunAs | None = None,
    ) -> HelpForumSearchResponse:
        """
        Search the Galaxy Help forum.

        **Warning**: This API is unstable and may change without notice.

        Args:
            query (str)              : Search query to use for searching the Galaxy Help forum.
            run-as (HelpForumSearchSearchForumParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HelpForumSearchResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/help/forum/search"

        params: dict[str, Any] = {
            "query": DataclassSerializer.serialize(query),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), HelpForumSearchResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def help_forum_search_search_forum(
        self,
        query: str,
        run_as: HelpForumSearchSearchForumParamRunAs | None = None,
    ) -> HelpForumSearchResponse:
        """
        Search the Galaxy Help forum.

        **Warning**: This API is unstable and may change without notice.

        Args:
            query (str)              : Search query to use for searching the Galaxy Help forum.
            run-as (HelpForumSearchSearchForumParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HelpForumSearchResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/help/forum/search"

        params: dict[str, Any] = {
            "query": DataclassSerializer.serialize(query),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), HelpForumSearchResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
