from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core import HttpNotImplementedError
from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.async_file import AsyncFile
from ..models.create_page_payload import CreatePagePayload
from ..models.page_details import PageDetails
from ..models.page_summary import PageSummary
from ..models.page_summary_list import PageSummaryList
from ..models.pages_create_param_run_as import PagesCreateParamRunAs
from ..models.pages_delete_param_run_as import PagesDeleteParamRunAs
from ..models.pages_disable_link_access_disable_link_access_param_run_as import (
    PagesDisableLinkAccessDisableLinkAccessParamRunAs,
)
from ..models.pages_enable_link_access_enable_link_access_param_run_as import (
    PagesEnableLinkAccessEnableLinkAccessParamRunAs,
)
from ..models.pages_index_param_run_as import PagesIndexParamRunAs
from ..models.pages_index_param_search import PagesIndexParamSearch
from ..models.pages_index_param_user_id import PagesIndexParamUserId
from ..models.pages_prepare_download_prepare_pdf_param_run_as import PagesPrepareDownloadPreparePdfParamRunAs
from ..models.pages_publish_publish_param_run_as import PagesPublishPublishParamRunAs
from ..models.pages_share_with_users_share_with_users_param_run_as import PagesShareWithUsersShareWithUsersParamRunAs
from ..models.pages_sharing_sharing_param_run_as import PagesSharingSharingParamRunAs
from ..models.pages_show_param_run_as import PagesShowParamRunAs
from ..models.pages_show_pdf_param_run_as import PagesShowPdfParamRunAs
from ..models.pages_slug_set_slug_param_run_as import PagesSlugSetSlugParamRunAs
from ..models.pages_undelete_undelete_param_run_as import PagesUndeleteUndeleteParamRunAs
from ..models.pages_unpublish_unpublish_param_run_as import PagesUnpublishUnpublishParamRunAs
from ..models.pages_update_param_run_as import PagesUpdateParamRunAs
from ..models.set_slug_payload import SetSlugPayload
from ..models.share_with_payload import ShareWithPayload
from ..models.share_with_status import ShareWithStatus
from ..models.sharing_status import SharingStatus
from ..models.update_page_payload import UpdatePagePayload


@runtime_checkable
class PagesClientProtocol(Protocol):
    """Protocol defining the interface of PagesClient for dependency injection."""

    async def pages_index(
        self,
        deleted: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        search: PagesIndexParamSearch | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        sort_by: str | None = None,
        sort_desc: bool | None = None,
        user_id: PagesIndexParamUserId | None = None,
        run_as: PagesIndexParamRunAs | None = None,
    ) -> PageSummaryList: ...

    async def pages_index(
        self,
        deleted: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        search: PagesIndexParamSearch | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        sort_by: str | None = None,
        sort_desc: bool | None = None,
        user_id: PagesIndexParamUserId | None = None,
        run_as: PagesIndexParamRunAs | None = None,
    ) -> PageSummaryList: ...

    async def pages_create(
        self,
        body: CreatePagePayload,
        run_as: PagesCreateParamRunAs | None = None,
    ) -> PageSummary: ...

    async def pages_create(
        self,
        body: CreatePagePayload,
        run_as: PagesCreateParamRunAs | None = None,
    ) -> PageSummary: ...

    async def pages_delete(
        self,
        id_: str,
        run_as: PagesDeleteParamRunAs | None = None,
    ) -> None: ...

    async def pages_delete(
        self,
        id_: str,
        run_as: PagesDeleteParamRunAs | None = None,
    ) -> None: ...

    async def pages_show(
        self,
        id_: str,
        run_as: PagesShowParamRunAs | None = None,
    ) -> PageDetails: ...

    async def pages_show(
        self,
        id_: str,
        run_as: PagesShowParamRunAs | None = None,
    ) -> PageDetails: ...

    async def pages_update(
        self,
        id_: str,
        body: UpdatePagePayload,
        run_as: PagesUpdateParamRunAs | None = None,
    ) -> PageSummary: ...

    async def pages_update(
        self,
        id_: str,
        body: UpdatePagePayload,
        run_as: PagesUpdateParamRunAs | None = None,
    ) -> PageSummary: ...

    async def pages_show_pdf(
        self,
        id_: str,
        run_as: PagesShowPdfParamRunAs | None = None,
    ) -> Any: ...

    async def pages_show_pdf(
        self,
        id_: str,
        run_as: PagesShowPdfParamRunAs | None = None,
    ) -> Any: ...

    async def pages_disable_link_access_disable_link_access(
        self,
        id_: str,
        run_as: PagesDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def pages_disable_link_access_disable_link_access(
        self,
        id_: str,
        run_as: PagesDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def pages_enable_link_access_enable_link_access(
        self,
        id_: str,
        run_as: PagesEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def pages_enable_link_access_enable_link_access(
        self,
        id_: str,
        run_as: PagesEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def pages_prepare_download_prepare_pdf(
        self,
        id_: str,
        run_as: PagesPrepareDownloadPreparePdfParamRunAs | None = None,
    ) -> AsyncFile: ...

    async def pages_prepare_download_prepare_pdf(
        self,
        id_: str,
        run_as: PagesPrepareDownloadPreparePdfParamRunAs | None = None,
    ) -> AsyncFile: ...

    async def pages_publish_publish(
        self,
        id_: str,
        run_as: PagesPublishPublishParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def pages_publish_publish(
        self,
        id_: str,
        run_as: PagesPublishPublishParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def pages_share_with_users_share_with_users(
        self,
        id_: str,
        body: ShareWithPayload,
        run_as: PagesShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus: ...

    async def pages_share_with_users_share_with_users(
        self,
        id_: str,
        body: ShareWithPayload,
        run_as: PagesShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus: ...

    async def pages_sharing_sharing(
        self,
        id_: str,
        run_as: PagesSharingSharingParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def pages_sharing_sharing(
        self,
        id_: str,
        run_as: PagesSharingSharingParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def pages_slug_set_slug(
        self,
        id_: str,
        body: SetSlugPayload,
        run_as: PagesSlugSetSlugParamRunAs | None = None,
    ) -> None: ...

    async def pages_slug_set_slug(
        self,
        id_: str,
        body: SetSlugPayload,
        run_as: PagesSlugSetSlugParamRunAs | None = None,
    ) -> None: ...

    async def pages_undelete_undelete(
        self,
        id_: str,
        run_as: PagesUndeleteUndeleteParamRunAs | None = None,
    ) -> None: ...

    async def pages_undelete_undelete(
        self,
        id_: str,
        run_as: PagesUndeleteUndeleteParamRunAs | None = None,
    ) -> None: ...

    async def pages_unpublish_unpublish(
        self,
        id_: str,
        run_as: PagesUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus: ...

    async def pages_unpublish_unpublish(
        self,
        id_: str,
        run_as: PagesUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus: ...


class PagesClient(PagesClientProtocol):
    """Client for pages endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def pages_index(
        self,
        deleted: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        search: PagesIndexParamSearch | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        sort_by: str | None = None,
        sort_desc: bool | None = None,
        user_id: PagesIndexParamUserId | None = None,
        run_as: PagesIndexParamRunAs | None = None,
    ) -> PageSummaryList:
        """
        Lists all Pages viewable by the user.

        Get a list with summary information of all Pages available to the user.

        Args:
            deleted (bool | None)    : Whether to include deleted pages in the result.
            limit (int | None)       :
            offset (int | None)      :
            search (PagesIndexParamSearch | None)
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
                                       Tags Available  `title` : The page's title.  `slug` : The
                                       page's slug. (The tag `s` can be used a short hand alias
                                       for this tag to filter on this attribute.)  `tag` : The
                                       page's tags. (The tag `t` can be used a short hand alias
                                       for this tag to filter on this attribute.)  `user` : The
                                       page's owner's username. (The tag `u` can be used a short
                                       hand alias for this tag to filter on this attribute.)  ##
                                       Free Text  Free text search terms will be searched
                                       against the following attributes of the Pages: `title`,
                                       `slug`, `tag`, `user`.
            show_own (bool | None)   :
            show_published (bool | None)
                                     :
            show_shared (bool | None):
            sort_by (str | None)     : Sort page index by this specified attribute on the page
                                       model
            sort_desc (bool | None)  : Sort in descending order?
            user_id (PagesIndexParamUserId | None)
                                     :
            run-as (PagesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            PageSummaryList: A list with summary page information.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/pages"

        params: dict[str, Any] = {
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"search": DataclassSerializer.serialize(search)} if search is not None else {}),
            **({"show_own": DataclassSerializer.serialize(show_own)} if show_own is not None else {}),
            **({"show_published": DataclassSerializer.serialize(show_published)} if show_published is not None else {}),
            **({"show_shared": DataclassSerializer.serialize(show_shared)} if show_shared is not None else {}),
            **({"sort_by": DataclassSerializer.serialize(sort_by)} if sort_by is not None else {}),
            **({"sort_desc": DataclassSerializer.serialize(sort_desc)} if sort_desc is not None else {}),
            **({"user_id": DataclassSerializer.serialize(user_id)} if user_id is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PageSummaryList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_index(
        self,
        deleted: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        search: PagesIndexParamSearch | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        sort_by: str | None = None,
        sort_desc: bool | None = None,
        user_id: PagesIndexParamUserId | None = None,
        run_as: PagesIndexParamRunAs | None = None,
    ) -> PageSummaryList:
        """
        Lists all Pages viewable by the user.

        Get a list with summary information of all Pages available to the user.

        Args:
            deleted (bool | None)    : Whether to include deleted pages in the result.
            limit (int | None)       :
            offset (int | None)      :
            search (PagesIndexParamSearch | None)
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
                                       Tags Available  `title` : The page's title.  `slug` : The
                                       page's slug. (The tag `s` can be used a short hand alias
                                       for this tag to filter on this attribute.)  `tag` : The
                                       page's tags. (The tag `t` can be used a short hand alias
                                       for this tag to filter on this attribute.)  `user` : The
                                       page's owner's username. (The tag `u` can be used a short
                                       hand alias for this tag to filter on this attribute.)  ##
                                       Free Text  Free text search terms will be searched
                                       against the following attributes of the Pages: `title`,
                                       `slug`, `tag`, `user`.
            show_own (bool | None)   :
            show_published (bool | None)
                                     :
            show_shared (bool | None):
            sort_by (str | None)     : Sort page index by this specified attribute on the page
                                       model
            sort_desc (bool | None)  : Sort in descending order?
            user_id (PagesIndexParamUserId | None)
                                     :
            run-as (PagesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            PageSummaryList: A list with summary page information.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/pages"

        params: dict[str, Any] = {
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"search": DataclassSerializer.serialize(search)} if search is not None else {}),
            **({"show_own": DataclassSerializer.serialize(show_own)} if show_own is not None else {}),
            **({"show_published": DataclassSerializer.serialize(show_published)} if show_published is not None else {}),
            **({"show_shared": DataclassSerializer.serialize(show_shared)} if show_shared is not None else {}),
            **({"sort_by": DataclassSerializer.serialize(sort_by)} if sort_by is not None else {}),
            **({"sort_desc": DataclassSerializer.serialize(sort_desc)} if sort_desc is not None else {}),
            **({"user_id": DataclassSerializer.serialize(user_id)} if user_id is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PageSummaryList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_create(
        self,
        body: CreatePagePayload,
        run_as: PagesCreateParamRunAs | None = None,
    ) -> PageSummary:
        """
        Create a page and return summary information.

        Creates a new Page.

        Args:
            run-as (PagesCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreatePagePayload) : Request body. (json)

        Returns:
            PageSummary: The page summary information.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/pages"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreatePagePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PageSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_create(
        self,
        body: CreatePagePayload,
        run_as: PagesCreateParamRunAs | None = None,
    ) -> PageSummary:
        """
        Create a page and return summary information.

        Creates a new Page.

        Args:
            run-as (PagesCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreatePagePayload) : Request body. (json)

        Returns:
            PageSummary: The page summary information.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/pages"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreatePagePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PageSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_delete(
        self,
        id_: str,
        run_as: PagesDeleteParamRunAs | None = None,
    ) -> None:
        """
        Marks the specific Page as deleted.

        Marks the Page with the given ID as deleted.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_delete(
        self,
        id_: str,
        run_as: PagesDeleteParamRunAs | None = None,
    ) -> None:
        """
        Marks the specific Page as deleted.

        Marks the Page with the given ID as deleted.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_show(
        self,
        id_: str,
        run_as: PagesShowParamRunAs | None = None,
    ) -> PageDetails:
        """
        Return a page summary and the content of the last revision.

        Return summary information about a specific Page and the content of the last revision.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            PageDetails: The page summary information.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PageDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_show(
        self,
        id_: str,
        run_as: PagesShowParamRunAs | None = None,
    ) -> PageDetails:
        """
        Return a page summary and the content of the last revision.

        Return summary information about a specific Page and the content of the last revision.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            PageDetails: The page summary information.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PageDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_update(
        self,
        id_: str,
        body: UpdatePagePayload,
        run_as: PagesUpdateParamRunAs | None = None,
    ) -> PageSummary:
        """
        Update a page and return summary information.

        Updates an existing Page.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdatePagePayload) : Request body. (json)

        Returns:
            PageSummary: The page summary information.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UpdatePagePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PageSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_update(
        self,
        id_: str,
        body: UpdatePagePayload,
        run_as: PagesUpdateParamRunAs | None = None,
    ) -> PageSummary:
        """
        Update a page and return summary information.

        Updates an existing Page.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdatePagePayload) : Request body. (json)

        Returns:
            PageSummary: The page summary information.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UpdatePagePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PageSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_show_pdf(
        self,
        id_: str,
        run_as: PagesShowPdfParamRunAs | None = None,
    ) -> Any:
        """
        Return a PDF document of the last revision of the Page.

        Return a PDF document of the last revision of the Page.  This feature may not be
        available in this Galaxy.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesShowPdfParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: PDF document with the last revision of the page.

        Raises:
            HttpError:
                HTTPError: 501: PDF conversion service not available.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}.pdf"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(Any, response.json())
            case 501:
                raise HttpNotImplementedError(response=response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_show_pdf(
        self,
        id_: str,
        run_as: PagesShowPdfParamRunAs | None = None,
    ) -> Any:
        """
        Return a PDF document of the last revision of the Page.

        Return a PDF document of the last revision of the Page.  This feature may not be
        available in this Galaxy.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesShowPdfParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: PDF document with the last revision of the page.

        Raises:
            HttpError:
                HTTPError: 501: PDF conversion service not available.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}.pdf"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(Any, response.json())
            case 501:
                raise HttpNotImplementedError(response=response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_disable_link_access_disable_link_access(
        self,
        id_: str,
        run_as: PagesDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item inaccessible by a URL link.

        Makes this item inaccessible by a URL link and return the current sharing status.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesDisableLinkAccessDisableLinkAccessParamRunAs | None)
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

        url = f"{self.base_url}/api/pages/{id_}/disable_link_access"

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

    async def pages_disable_link_access_disable_link_access(
        self,
        id_: str,
        run_as: PagesDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item inaccessible by a URL link.

        Makes this item inaccessible by a URL link and return the current sharing status.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesDisableLinkAccessDisableLinkAccessParamRunAs | None)
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

        url = f"{self.base_url}/api/pages/{id_}/disable_link_access"

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

    async def pages_enable_link_access_enable_link_access(
        self,
        id_: str,
        run_as: PagesEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item accessible by a URL link.

        Makes this item accessible by a URL link and return the current sharing status.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesEnableLinkAccessEnableLinkAccessParamRunAs | None)
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

        url = f"{self.base_url}/api/pages/{id_}/enable_link_access"

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

    async def pages_enable_link_access_enable_link_access(
        self,
        id_: str,
        run_as: PagesEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item accessible by a URL link.

        Makes this item accessible by a URL link and return the current sharing status.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesEnableLinkAccessEnableLinkAccessParamRunAs | None)
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

        url = f"{self.base_url}/api/pages/{id_}/enable_link_access"

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

    async def pages_prepare_download_prepare_pdf(
        self,
        id_: str,
        run_as: PagesPrepareDownloadPreparePdfParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Return a PDF document of the last revision of the Page.

        Return a STS download link for this page to be downloaded as a PDF.  This feature may
        not be available in this Galaxy.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesPrepareDownloadPreparePdfParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncFile: Short term storage reference for async monitoring of this download.

        Raises:
            HttpError:
                HTTPError: 501: PDF conversion service not available.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}/prepare_download"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AsyncFile)
            case 501:
                raise HttpNotImplementedError(response=response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_prepare_download_prepare_pdf(
        self,
        id_: str,
        run_as: PagesPrepareDownloadPreparePdfParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Return a PDF document of the last revision of the Page.

        Return a STS download link for this page to be downloaded as a PDF.  This feature may
        not be available in this Galaxy.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesPrepareDownloadPreparePdfParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncFile: Short term storage reference for async monitoring of this download.

        Raises:
            HttpError:
                HTTPError: 501: PDF conversion service not available.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}/prepare_download"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AsyncFile)
            case 501:
                raise HttpNotImplementedError(response=response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_publish_publish(
        self,
        id_: str,
        run_as: PagesPublishPublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item public and accessible by a URL link.

        Makes this item publicly available by a URL link and return the current sharing status.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesPublishPublishParamRunAs | None)
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

        url = f"{self.base_url}/api/pages/{id_}/publish"

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

    async def pages_publish_publish(
        self,
        id_: str,
        run_as: PagesPublishPublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item public and accessible by a URL link.

        Makes this item publicly available by a URL link and return the current sharing status.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesPublishPublishParamRunAs | None)
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

        url = f"{self.base_url}/api/pages/{id_}/publish"

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

    async def pages_share_with_users_share_with_users(
        self,
        id_: str,
        body: ShareWithPayload,
        run_as: PagesShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus:
        """
        Share this item with specific users.

        Shares this item with specific users and return the current sharing status.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesShareWithUsersShareWithUsersParamRunAs | None)
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

        url = f"{self.base_url}/api/pages/{id_}/share_with_users"

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

    async def pages_share_with_users_share_with_users(
        self,
        id_: str,
        body: ShareWithPayload,
        run_as: PagesShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus:
        """
        Share this item with specific users.

        Shares this item with specific users and return the current sharing status.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesShareWithUsersShareWithUsersParamRunAs | None)
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

        url = f"{self.base_url}/api/pages/{id_}/share_with_users"

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

    async def pages_sharing_sharing(
        self,
        id_: str,
        run_as: PagesSharingSharingParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Get the current sharing status of the given Page.

        Return the sharing status of the item.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesSharingSharingParamRunAs | None)
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

        url = f"{self.base_url}/api/pages/{id_}/sharing"

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

    async def pages_sharing_sharing(
        self,
        id_: str,
        run_as: PagesSharingSharingParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Get the current sharing status of the given Page.

        Return the sharing status of the item.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesSharingSharingParamRunAs | None)
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

        url = f"{self.base_url}/api/pages/{id_}/sharing"

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

    async def pages_slug_set_slug(
        self,
        id_: str,
        body: SetSlugPayload,
        run_as: PagesSlugSetSlugParamRunAs | None = None,
    ) -> None:
        """
        Set a new slug for this shared item.

        Sets a new slug to access this item by URL. The new slug must be unique.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesSlugSetSlugParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SetSlugPayload)    : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}/slug"

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

    async def pages_slug_set_slug(
        self,
        id_: str,
        body: SetSlugPayload,
        run_as: PagesSlugSetSlugParamRunAs | None = None,
    ) -> None:
        """
        Set a new slug for this shared item.

        Sets a new slug to access this item by URL. The new slug must be unique.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesSlugSetSlugParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SetSlugPayload)    : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}/slug"

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

    async def pages_undelete_undelete(
        self,
        id_: str,
        run_as: PagesUndeleteUndeleteParamRunAs | None = None,
    ) -> None:
        """
        Undelete the specific Page.

        Marks the Page with the given ID as undeleted.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesUndeleteUndeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_undelete_undelete(
        self,
        id_: str,
        run_as: PagesUndeleteUndeleteParamRunAs | None = None,
    ) -> None:
        """
        Undelete the specific Page.

        Marks the Page with the given ID as undeleted.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesUndeleteUndeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/pages/{id_}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def pages_unpublish_unpublish(
        self,
        id_: str,
        run_as: PagesUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Removes this item from the published list.

        Removes this item from the published list and return the current sharing status.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesUnpublishUnpublishParamRunAs | None)
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

        url = f"{self.base_url}/api/pages/{id_}/unpublish"

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

    async def pages_unpublish_unpublish(
        self,
        id_: str,
        run_as: PagesUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Removes this item from the published list.

        Removes this item from the published list and return the current sharing status.

        Args:
            id (str)                 : The ID of the Page.
            run-as (PagesUnpublishUnpublishParamRunAs | None)
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

        url = f"{self.base_url}/api/pages/{id_}/unpublish"

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
