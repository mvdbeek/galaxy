from typing import Any

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.item_tags_payload import ItemTagsPayload
from ..models.tags_update_param_run_as import TagsUpdateParamRunAs


class TagsClient:
    """Client for tags endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def tags_update_2_2(
        self,
        body: ItemTagsPayload,
        run_as: TagsUpdateParamRunAs | None = None,
    ) -> None:
        """
        Apply a new set of tags to an item.

        Replaces the tags associated with an item with the new ones specified in the payload.  -
        The previous tags will be __deleted__. - If no tags are provided in the request body,
        the currently associated tags will also be __deleted__.

        Args:
            run-as (Optional[TagsUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ItemTagsPayload)   : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tags"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ItemTagsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tags_update_2_2(
        self,
        body: ItemTagsPayload,
        run_as: TagsUpdateParamRunAs | None = None,
    ) -> None:
        """
        Apply a new set of tags to an item.

        Replaces the tags associated with an item with the new ones specified in the payload.  -
        The previous tags will be __deleted__. - If no tags are provided in the request body,
        the currently associated tags will also be __deleted__.

        Args:
            run-as (Optional[TagsUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ItemTagsPayload)   : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tags"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ItemTagsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
