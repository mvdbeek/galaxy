from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.set_slug_payload import SetSlugPayload
from ..models.share_with_payload import ShareWithPayload
from ..models.share_with_status import ShareWithStatus
from ..models.sharing_status import SharingStatus
from ..models.visualization_create_payload import VisualizationCreatePayload
from ..models.visualization_create_response import VisualizationCreateResponse
from ..models.visualization_show_response import VisualizationShowResponse
from ..models.visualization_summary_list import VisualizationSummaryList
from ..models.visualization_update_payload import VisualizationUpdatePayload
from ..models.visualizations_create_param_import_id import VisualizationsCreateParamImportId
from ..models.visualizations_create_param_run_as import VisualizationsCreateParamRunAs
from ..models.visualizations_disable_link_access_disable_link_access_param_run_as import (
    VisualizationsDisableLinkAccessDisableLinkAccessParamRunAs,
)
from ..models.visualizations_enable_link_access_enable_link_access_param_run_as import (
    VisualizationsEnableLinkAccessEnableLinkAccessParamRunAs,
)
from ..models.visualizations_index_param_limit import VisualizationsIndexParamLimit
from ..models.visualizations_index_param_offset import VisualizationsIndexParamOffset
from ..models.visualizations_index_param_run_as import VisualizationsIndexParamRunAs
from ..models.visualizations_index_param_search import VisualizationsIndexParamSearch
from ..models.visualizations_index_param_user_id import VisualizationsIndexParamUserId
from ..models.visualizations_publish_publish_param_run_as import VisualizationsPublishPublishParamRunAs
from ..models.visualizations_share_with_users_share_with_users_param_run_as import (
    VisualizationsShareWithUsersShareWithUsersParamRunAs,
)
from ..models.visualizations_sharing_sharing_param_run_as import VisualizationsSharingSharingParamRunAs
from ..models.visualizations_show_param_run_as import VisualizationsShowParamRunAs
from ..models.visualizations_slug_set_slug_param_run_as import VisualizationsSlugSetSlugParamRunAs
from ..models.visualizations_unpublish_unpublish_param_run_as import VisualizationsUnpublishUnpublishParamRunAs
from ..models.visualizations_update_200_response import VisualizationsUpdate200Response
from ..models.visualizations_update_param_run_as import VisualizationsUpdateParamRunAs


@runtime_checkable
class VisualizationsClientProtocol(Protocol):
    """Protocol defining the interface of VisualizationsClient for dependency injection."""

    async def visualizations_index(
        self,
        deleted: bool | None = None,
        limit: VisualizationsIndexParamLimit | None = None,
        offset: VisualizationsIndexParamOffset | None = None,
        user_id: VisualizationsIndexParamUserId | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        sort_by: str | None = None,
        sort_desc: bool | None = None,
        search: VisualizationsIndexParamSearch | None = None,
        run_as: VisualizationsIndexParamRunAs | None = None,
    ) -> VisualizationSummaryList: ...

    async def visualizations_index(
        self,
        deleted: bool | None = None,
        limit: VisualizationsIndexParamLimit | None = None,
        offset: VisualizationsIndexParamOffset | None = None,
        user_id: VisualizationsIndexParamUserId | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        sort_by: str | None = None,
        sort_desc: bool | None = None,
        search: VisualizationsIndexParamSearch | None = None,
        run_as: VisualizationsIndexParamRunAs | None = None,
    ) -> VisualizationSummaryList: ...

    async def visualizations_create(
        self,
        body: VisualizationCreatePayload,
        import_id: VisualizationsCreateParamImportId | None = None,
        run_as: VisualizationsCreateParamRunAs | None = None,
    ) -> VisualizationCreateResponse: ...

    async def visualizations_create(
        self,
        body: VisualizationCreatePayload,
        import_id: VisualizationsCreateParamImportId | None = None,
        run_as: VisualizationsCreateParamRunAs | None = None,
    ) -> VisualizationCreateResponse: ...

    async def visualizations_show(
        self,
        id_: str,
        run_as: VisualizationsShowParamRunAs | None = None,
    ) -> VisualizationShowResponse: ...

    async def visualizations_show(
        self,
        id_: str,
        run_as: VisualizationsShowParamRunAs | None = None,
    ) -> VisualizationShowResponse: ...

    async def visualizations_update(
        self,
        id_: str,
        body: VisualizationUpdatePayload,
        run_as: VisualizationsUpdateParamRunAs | None = None,
    ) -> VisualizationsUpdate200Response | None: ...

    async def visualizations_update(
        self,
        id_: str,
        body: VisualizationUpdatePayload,
        run_as: VisualizationsUpdateParamRunAs | None = None,
    ) -> VisualizationsUpdate200Response | None: ...

    async def visualizations_disable_link_access_disable_link_access(
        self,
        id_: str,
        run_as: VisualizationsDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def visualizations_disable_link_access_disable_link_access(
        self,
        id_: str,
        run_as: VisualizationsDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def visualizations_enable_link_access_enable_link_access(
        self,
        id_: str,
        run_as: VisualizationsEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def visualizations_enable_link_access_enable_link_access(
        self,
        id_: str,
        run_as: VisualizationsEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def visualizations_publish_publish(
        self,
        id_: str,
        run_as: VisualizationsPublishPublishParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def visualizations_publish_publish(
        self,
        id_: str,
        run_as: VisualizationsPublishPublishParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def visualizations_share_with_users_share_with_users(
        self,
        id_: str,
        body: ShareWithPayload,
        run_as: VisualizationsShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus: ...

    async def visualizations_share_with_users_share_with_users(
        self,
        id_: str,
        body: ShareWithPayload,
        run_as: VisualizationsShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus: ...

    async def visualizations_sharing_sharing(
        self,
        id_: str,
        run_as: VisualizationsSharingSharingParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def visualizations_sharing_sharing(
        self,
        id_: str,
        run_as: VisualizationsSharingSharingParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def visualizations_slug_set_slug(
        self,
        id_: str,
        body: SetSlugPayload,
        run_as: VisualizationsSlugSetSlugParamRunAs | None = None,
    ) -> None: ...

    async def visualizations_slug_set_slug(
        self,
        id_: str,
        body: SetSlugPayload,
        run_as: VisualizationsSlugSetSlugParamRunAs | None = None,
    ) -> None: ...

    async def visualizations_unpublish_unpublish(
        self,
        id_: str,
        run_as: VisualizationsUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def visualizations_unpublish_unpublish(
        self,
        id_: str,
        run_as: VisualizationsUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus: ...


class VisualizationsClient(VisualizationsClientProtocol):
    """Client for visualizations endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def visualizations_index(
        self,
        deleted: bool | None = None,
        limit: VisualizationsIndexParamLimit | None = None,
        offset: VisualizationsIndexParamOffset | None = None,
        user_id: VisualizationsIndexParamUserId | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        sort_by: str | None = None,
        sort_desc: bool | None = None,
        search: VisualizationsIndexParamSearch | None = None,
        run_as: VisualizationsIndexParamRunAs | None = None,
    ) -> VisualizationSummaryList:
        """
        Returns visualizations for the current user.

        Args:
            deleted (bool | None)    : Whether to include deleted visualizations in the result.
            limit (VisualizationsIndexParamLimit | None)
                                     : The maximum number of items to return.
            offset (VisualizationsIndexParamOffset | None)
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            user_id (VisualizationsIndexParamUserId | None)
                                     :
            show_own (bool | None)   :
            show_published (bool | None)
                                     :
            show_shared (bool | None):
            sort_by (str | None)     : Sort visualization index by this specified attribute on
                                       the visualization model
            sort_desc (bool | None)  : Sort in descending order?
            search (VisualizationsIndexParamSearch | None)
                                     : A mix of free text and GitHub-style tags used to filter
                                       the index operation.  ## Query Structure  GitHub-style
                                       filter tags (not be confused with Galaxy tags) are tags
                                       of the form `<tag_name>:<text_no_spaces>` or
                                       `<tag_name>:'<text with potential spaces>'`. The tag name
                                       *generally* (but not exclusively) corresponds to the name
                                       of an attribute on the model being indexed (i.e. a column
                                       in the database).  If the tag is quoted, the attribute
                                       will be filtered exactly. If the tag is unquoted,
                                       generally a partial match will be used to filter the
                                       query (i.e. in terms of the implementation this means the
                                       database operation `ILIKE` will typically be used).  Once
                                       the tagged filters are extracted from the search query,
                                       the remaining text is just used to search various
                                       documented attributes of the object.  ## GitHub-style
                                       Tags Available  `title` : The visualization's title.
                                       `slug` : The visualization's slug. (The tag `s` can be
                                       used a short hand alias for this tag to filter on this
                                       attribute.)  `tag` : The visualization's tags. (The tag
                                       `t` can be used a short hand alias for this tag to filter
                                       on this attribute.)  `user` : The visualization's owner's
                                       username. (The tag `u` can be used a short hand alias for
                                       this tag to filter on this attribute.)  ## Free Text
                                       Free text search terms will be searched against the
                                       following attributes of the Visualizations: `title`,
                                       `slug`, `tag`, `type`.
            run-as (VisualizationsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            VisualizationSummaryList: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/visualizations"

        params: dict[str, Any] = {
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"user_id": DataclassSerializer.serialize(user_id)} if user_id is not None else {}),
            **({"show_own": DataclassSerializer.serialize(show_own)} if show_own is not None else {}),
            **({"show_published": DataclassSerializer.serialize(show_published)} if show_published is not None else {}),
            **({"show_shared": DataclassSerializer.serialize(show_shared)} if show_shared is not None else {}),
            **({"sort_by": DataclassSerializer.serialize(sort_by)} if sort_by is not None else {}),
            **({"sort_desc": DataclassSerializer.serialize(sort_desc)} if sort_desc is not None else {}),
            **({"search": DataclassSerializer.serialize(search)} if search is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), VisualizationSummaryList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_index(
        self,
        deleted: bool | None = None,
        limit: VisualizationsIndexParamLimit | None = None,
        offset: VisualizationsIndexParamOffset | None = None,
        user_id: VisualizationsIndexParamUserId | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        sort_by: str | None = None,
        sort_desc: bool | None = None,
        search: VisualizationsIndexParamSearch | None = None,
        run_as: VisualizationsIndexParamRunAs | None = None,
    ) -> VisualizationSummaryList:
        """
        Returns visualizations for the current user.

        Args:
            deleted (bool | None)    : Whether to include deleted visualizations in the result.
            limit (VisualizationsIndexParamLimit | None)
                                     : The maximum number of items to return.
            offset (VisualizationsIndexParamOffset | None)
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            user_id (VisualizationsIndexParamUserId | None)
                                     :
            show_own (bool | None)   :
            show_published (bool | None)
                                     :
            show_shared (bool | None):
            sort_by (str | None)     : Sort visualization index by this specified attribute on
                                       the visualization model
            sort_desc (bool | None)  : Sort in descending order?
            search (VisualizationsIndexParamSearch | None)
                                     : A mix of free text and GitHub-style tags used to filter
                                       the index operation.  ## Query Structure  GitHub-style
                                       filter tags (not be confused with Galaxy tags) are tags
                                       of the form `<tag_name>:<text_no_spaces>` or
                                       `<tag_name>:'<text with potential spaces>'`. The tag name
                                       *generally* (but not exclusively) corresponds to the name
                                       of an attribute on the model being indexed (i.e. a column
                                       in the database).  If the tag is quoted, the attribute
                                       will be filtered exactly. If the tag is unquoted,
                                       generally a partial match will be used to filter the
                                       query (i.e. in terms of the implementation this means the
                                       database operation `ILIKE` will typically be used).  Once
                                       the tagged filters are extracted from the search query,
                                       the remaining text is just used to search various
                                       documented attributes of the object.  ## GitHub-style
                                       Tags Available  `title` : The visualization's title.
                                       `slug` : The visualization's slug. (The tag `s` can be
                                       used a short hand alias for this tag to filter on this
                                       attribute.)  `tag` : The visualization's tags. (The tag
                                       `t` can be used a short hand alias for this tag to filter
                                       on this attribute.)  `user` : The visualization's owner's
                                       username. (The tag `u` can be used a short hand alias for
                                       this tag to filter on this attribute.)  ## Free Text
                                       Free text search terms will be searched against the
                                       following attributes of the Visualizations: `title`,
                                       `slug`, `tag`, `type`.
            run-as (VisualizationsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            VisualizationSummaryList: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/visualizations"

        params: dict[str, Any] = {
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"user_id": DataclassSerializer.serialize(user_id)} if user_id is not None else {}),
            **({"show_own": DataclassSerializer.serialize(show_own)} if show_own is not None else {}),
            **({"show_published": DataclassSerializer.serialize(show_published)} if show_published is not None else {}),
            **({"show_shared": DataclassSerializer.serialize(show_shared)} if show_shared is not None else {}),
            **({"sort_by": DataclassSerializer.serialize(sort_by)} if sort_by is not None else {}),
            **({"sort_desc": DataclassSerializer.serialize(sort_desc)} if sort_desc is not None else {}),
            **({"search": DataclassSerializer.serialize(search)} if search is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), VisualizationSummaryList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_create(
        self,
        body: VisualizationCreatePayload,
        import_id: VisualizationsCreateParamImportId | None = None,
        run_as: VisualizationsCreateParamRunAs | None = None,
    ) -> VisualizationCreateResponse:
        """
        Create a new visualization.

        Creates a new visualization using the given payload and does not require the import_id
        field. If import_id given, it imports a copy of an existing visualization into the
        user's workspace and does not require the rest of the payload.

        Args:
            import_id (VisualizationsCreateParamImportId | None)
                                     : The encoded database identifier of the Visualization to
                                       import.
            run-as (VisualizationsCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (VisualizationCreatePayload)
                                     : Request body. (json)

        Returns:
            VisualizationCreateResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/visualizations"

        params: dict[str, Any] = {
            **({"import_id": DataclassSerializer.serialize(import_id)} if import_id is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: VisualizationCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), VisualizationCreateResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_create(
        self,
        body: VisualizationCreatePayload,
        import_id: VisualizationsCreateParamImportId | None = None,
        run_as: VisualizationsCreateParamRunAs | None = None,
    ) -> VisualizationCreateResponse:
        """
        Create a new visualization.

        Creates a new visualization using the given payload and does not require the import_id
        field. If import_id given, it imports a copy of an existing visualization into the
        user's workspace and does not require the rest of the payload.

        Args:
            import_id (VisualizationsCreateParamImportId | None)
                                     : The encoded database identifier of the Visualization to
                                       import.
            run-as (VisualizationsCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (VisualizationCreatePayload)
                                     : Request body. (json)

        Returns:
            VisualizationCreateResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/visualizations"

        params: dict[str, Any] = {
            **({"import_id": DataclassSerializer.serialize(import_id)} if import_id is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: VisualizationCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), VisualizationCreateResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_show(
        self,
        id_: str,
        run_as: VisualizationsShowParamRunAs | None = None,
    ) -> VisualizationShowResponse:
        """
        Get a visualization by ID.

        Return the visualization.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            VisualizationShowResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), VisualizationShowResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_show(
        self,
        id_: str,
        run_as: VisualizationsShowParamRunAs | None = None,
    ) -> VisualizationShowResponse:
        """
        Get a visualization by ID.

        Return the visualization.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            VisualizationShowResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), VisualizationShowResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_update(
        self,
        id_: str,
        body: VisualizationUpdatePayload,
        run_as: VisualizationsUpdateParamRunAs | None = None,
    ) -> VisualizationsUpdate200Response | None:
        """
        Update a visualization.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (VisualizationUpdatePayload)
                                     : Request body. (json)

        Returns:
            VisualizationsUpdate200Response | None: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: VisualizationUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return (
                    structure_from_dict(response.json(), VisualizationsUpdate200Response)
                    if response.json() is not None
                    else None
                )
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_update(
        self,
        id_: str,
        body: VisualizationUpdatePayload,
        run_as: VisualizationsUpdateParamRunAs | None = None,
    ) -> VisualizationsUpdate200Response | None:
        """
        Update a visualization.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (VisualizationUpdatePayload)
                                     : Request body. (json)

        Returns:
            VisualizationsUpdate200Response | None: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: VisualizationUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return (
                    structure_from_dict(response.json(), VisualizationsUpdate200Response)
                    if response.json() is not None
                    else None
                )
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_disable_link_access_disable_link_access(
        self,
        id_: str,
        run_as: VisualizationsDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item inaccessible by a URL link.

        Makes this item inaccessible by a URL link and return the current sharing status.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsDisableLinkAccessDisableLinkAccessParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/disable_link_access"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), SharingStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_disable_link_access_disable_link_access(
        self,
        id_: str,
        run_as: VisualizationsDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item inaccessible by a URL link.

        Makes this item inaccessible by a URL link and return the current sharing status.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsDisableLinkAccessDisableLinkAccessParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/disable_link_access"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), SharingStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_enable_link_access_enable_link_access(
        self,
        id_: str,
        run_as: VisualizationsEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item accessible by a URL link.

        Makes this item accessible by a URL link and return the current sharing status.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsEnableLinkAccessEnableLinkAccessParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/enable_link_access"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), SharingStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_enable_link_access_enable_link_access(
        self,
        id_: str,
        run_as: VisualizationsEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item accessible by a URL link.

        Makes this item accessible by a URL link and return the current sharing status.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsEnableLinkAccessEnableLinkAccessParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/enable_link_access"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), SharingStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_publish_publish(
        self,
        id_: str,
        run_as: VisualizationsPublishPublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item public and accessible by a URL link.

        Makes this item publicly available by a URL link and return the current sharing status.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsPublishPublishParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/publish"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), SharingStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_publish_publish(
        self,
        id_: str,
        run_as: VisualizationsPublishPublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item public and accessible by a URL link.

        Makes this item publicly available by a URL link and return the current sharing status.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsPublishPublishParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/publish"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), SharingStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_share_with_users_share_with_users(
        self,
        id_: str,
        body: ShareWithPayload,
        run_as: VisualizationsShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus:
        """
        Share this item with specific users.

        Shares this item with specific users and return the current sharing status.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsShareWithUsersShareWithUsersParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ShareWithPayload)  : Request body. (json)

        Returns:
            ShareWithStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/share_with_users"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ShareWithPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ShareWithStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_share_with_users_share_with_users(
        self,
        id_: str,
        body: ShareWithPayload,
        run_as: VisualizationsShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus:
        """
        Share this item with specific users.

        Shares this item with specific users and return the current sharing status.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsShareWithUsersShareWithUsersParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ShareWithPayload)  : Request body. (json)

        Returns:
            ShareWithStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/share_with_users"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ShareWithPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ShareWithStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_sharing_sharing(
        self,
        id_: str,
        run_as: VisualizationsSharingSharingParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Get the current sharing status of the given Visualization.

        Return the sharing status of the item.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsSharingSharingParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/sharing"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), SharingStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_sharing_sharing(
        self,
        id_: str,
        run_as: VisualizationsSharingSharingParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Get the current sharing status of the given Visualization.

        Return the sharing status of the item.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsSharingSharingParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/sharing"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), SharingStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_slug_set_slug(
        self,
        id_: str,
        body: SetSlugPayload,
        run_as: VisualizationsSlugSetSlugParamRunAs | None = None,
    ) -> None:
        """
        Set a new slug for this shared item.

        Sets a new slug to access this item by URL. The new slug must be unique.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsSlugSetSlugParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SetSlugPayload)    : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/slug"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: SetSlugPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_slug_set_slug(
        self,
        id_: str,
        body: SetSlugPayload,
        run_as: VisualizationsSlugSetSlugParamRunAs | None = None,
    ) -> None:
        """
        Set a new slug for this shared item.

        Sets a new slug to access this item by URL. The new slug must be unique.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsSlugSetSlugParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SetSlugPayload)    : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/slug"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: SetSlugPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_unpublish_unpublish(
        self,
        id_: str,
        run_as: VisualizationsUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Removes this item from the published list.

        Removes this item from the published list and return the current sharing status.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsUnpublishUnpublishParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/unpublish"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), SharingStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def visualizations_unpublish_unpublish(
        self,
        id_: str,
        run_as: VisualizationsUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Removes this item from the published list.

        Removes this item from the published list and return the current sharing status.

        Args:
            id (str)                 : The encoded database identifier of the Visualization.
            run-as (VisualizationsUnpublishUnpublishParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/visualizations/{id_}/unpublish"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), SharingStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
