from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.create_library_file_payload import CreateLibraryFilePayload
from ..models.create_library_folder_payload import CreateLibraryFolderPayload
from ..models.data_libraries_folders_contents_create_param_run_as import DataLibrariesFoldersContentsCreateParamRunAs
from ..models.data_libraries_folders_contents_index_param_include_deleted import (
    DataLibrariesFoldersContentsIndexParamIncludeDeleted,
)
from ..models.data_libraries_folders_contents_index_param_run_as import DataLibrariesFoldersContentsIndexParamRunAs
from ..models.data_libraries_folders_contents_index_param_search_text import (
    DataLibrariesFoldersContentsIndexParamSearchText,
)
from ..models.data_libraries_folders_contents_index_param_sort_desc import (
    DataLibrariesFoldersContentsIndexParamSortDesc,
)
from ..models.data_libraries_folders_create_param_run_as import DataLibrariesFoldersCreateParamRunAs
from ..models.data_libraries_folders_delete_param_run_as import DataLibrariesFoldersDeleteParamRunAs
from ..models.data_libraries_folders_delete_param_undelete import DataLibrariesFoldersDeleteParamUndelete
from ..models.data_libraries_folders_permissions_get_permissions_200_response import (
    DataLibrariesFoldersPermissionsGetPermissions200Response,
)
from ..models.data_libraries_folders_permissions_get_permissions_param_q import (
    DataLibrariesFoldersPermissionsGetPermissionsParamQ,
)
from ..models.data_libraries_folders_permissions_get_permissions_param_run_as import (
    DataLibrariesFoldersPermissionsGetPermissionsParamRunAs,
)
from ..models.data_libraries_folders_permissions_get_permissions_param_scope import (
    DataLibrariesFoldersPermissionsGetPermissionsParamScope,
)
from ..models.data_libraries_folders_permissions_set_permissions_param_action import (
    DataLibrariesFoldersPermissionsSetPermissionsParamAction,
)
from ..models.data_libraries_folders_permissions_set_permissions_param_run_as import (
    DataLibrariesFoldersPermissionsSetPermissionsParamRunAs,
)
from ..models.data_libraries_folders_show_param_run_as import DataLibrariesFoldersShowParamRunAs
from ..models.data_libraries_folders_update_param_run_as import DataLibrariesFoldersUpdateParamRunAs
from ..models.data_libraries_folders_update_param_run_as_2 import DataLibrariesFoldersUpdateParamRunAs2
from ..models.library_folder_contents_index_result import LibraryFolderContentsIndexResult
from ..models.library_folder_current_permissions import LibraryFolderCurrentPermissions
from ..models.library_folder_details import LibraryFolderDetails
from ..models.library_folder_permissions_payload import LibraryFolderPermissionsPayload
from ..models.update_library_folder_payload import UpdateLibraryFolderPayload


@runtime_checkable
class DataLibrariesFoldersClientProtocol(Protocol):
    """Protocol defining the interface of DataLibrariesFoldersClient for dependency injection."""

    async def data_libraries_folders_contents_index(
        self,
        folder_id: str,
        limit: int | None = None,
        offset: int | None = None,
        search_text: DataLibrariesFoldersContentsIndexParamSearchText | None = None,
        include_deleted: DataLibrariesFoldersContentsIndexParamIncludeDeleted | None = None,
        order_by: str | None = None,
        sort_desc: DataLibrariesFoldersContentsIndexParamSortDesc | None = None,
        run_as: DataLibrariesFoldersContentsIndexParamRunAs | None = None,
    ) -> LibraryFolderContentsIndexResult: ...

    async def data_libraries_folders_contents_index(
        self,
        folder_id: str,
        limit: int | None = None,
        offset: int | None = None,
        search_text: DataLibrariesFoldersContentsIndexParamSearchText | None = None,
        include_deleted: DataLibrariesFoldersContentsIndexParamIncludeDeleted | None = None,
        order_by: str | None = None,
        sort_desc: DataLibrariesFoldersContentsIndexParamSortDesc | None = None,
        run_as: DataLibrariesFoldersContentsIndexParamRunAs | None = None,
    ) -> LibraryFolderContentsIndexResult: ...

    async def data_libraries_folders_contents_create(
        self,
        folder_id: str,
        body: CreateLibraryFilePayload,
        run_as: DataLibrariesFoldersContentsCreateParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def data_libraries_folders_contents_create(
        self,
        folder_id: str,
        body: CreateLibraryFilePayload,
        run_as: DataLibrariesFoldersContentsCreateParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def data_libraries_folders_delete(
        self,
        id_: str,
        undelete: DataLibrariesFoldersDeleteParamUndelete | None = None,
        run_as: DataLibrariesFoldersDeleteParamRunAs | None = None,
    ) -> LibraryFolderDetails: ...

    async def data_libraries_folders_delete(
        self,
        id_: str,
        undelete: DataLibrariesFoldersDeleteParamUndelete | None = None,
        run_as: DataLibrariesFoldersDeleteParamRunAs | None = None,
    ) -> LibraryFolderDetails: ...

    async def data_libraries_folders_show(
        self,
        id_: str,
        run_as: DataLibrariesFoldersShowParamRunAs | None = None,
    ) -> LibraryFolderDetails: ...

    async def data_libraries_folders_show(
        self,
        id_: str,
        run_as: DataLibrariesFoldersShowParamRunAs | None = None,
    ) -> LibraryFolderDetails: ...

    async def data_libraries_folders_update(
        self,
        id_: str,
        body: UpdateLibraryFolderPayload,
        run_as: DataLibrariesFoldersUpdateParamRunAs | None = None,
    ) -> LibraryFolderDetails: ...

    async def data_libraries_folders_update(
        self,
        id_: str,
        body: UpdateLibraryFolderPayload,
        run_as: DataLibrariesFoldersUpdateParamRunAs | None = None,
    ) -> LibraryFolderDetails: ...

    async def data_libraries_folders_create(
        self,
        id_: str,
        body: CreateLibraryFolderPayload,
        run_as: DataLibrariesFoldersCreateParamRunAs | None = None,
    ) -> LibraryFolderDetails: ...

    async def data_libraries_folders_create(
        self,
        id_: str,
        body: CreateLibraryFolderPayload,
        run_as: DataLibrariesFoldersCreateParamRunAs | None = None,
    ) -> LibraryFolderDetails: ...

    async def data_libraries_folders_update_2(
        self,
        id_: str,
        body: UpdateLibraryFolderPayload,
        run_as: DataLibrariesFoldersUpdateParamRunAs2 | None = None,
    ) -> LibraryFolderDetails: ...

    async def data_libraries_folders_update_2(
        self,
        id_: str,
        body: UpdateLibraryFolderPayload,
        run_as: DataLibrariesFoldersUpdateParamRunAs2 | None = None,
    ) -> LibraryFolderDetails: ...

    async def data_libraries_folders_permissions_get_permissions(
        self,
        id_: str,
        scope: DataLibrariesFoldersPermissionsGetPermissionsParamScope | None = None,
        page: int | None = None,
        page_limit: int | None = None,
        q: DataLibrariesFoldersPermissionsGetPermissionsParamQ | None = None,
        run_as: DataLibrariesFoldersPermissionsGetPermissionsParamRunAs | None = None,
    ) -> DataLibrariesFoldersPermissionsGetPermissions200Response: ...

    async def data_libraries_folders_permissions_get_permissions(
        self,
        id_: str,
        scope: DataLibrariesFoldersPermissionsGetPermissionsParamScope | None = None,
        page: int | None = None,
        page_limit: int | None = None,
        q: DataLibrariesFoldersPermissionsGetPermissionsParamQ | None = None,
        run_as: DataLibrariesFoldersPermissionsGetPermissionsParamRunAs | None = None,
    ) -> DataLibrariesFoldersPermissionsGetPermissions200Response: ...

    async def data_libraries_folders_permissions_set_permissions(
        self,
        id_: str,
        body: LibraryFolderPermissionsPayload,
        action: DataLibrariesFoldersPermissionsSetPermissionsParamAction | None = None,
        run_as: DataLibrariesFoldersPermissionsSetPermissionsParamRunAs | None = None,
    ) -> LibraryFolderCurrentPermissions: ...

    async def data_libraries_folders_permissions_set_permissions(
        self,
        id_: str,
        body: LibraryFolderPermissionsPayload,
        action: DataLibrariesFoldersPermissionsSetPermissionsParamAction | None = None,
        run_as: DataLibrariesFoldersPermissionsSetPermissionsParamRunAs | None = None,
    ) -> LibraryFolderCurrentPermissions: ...


class DataLibrariesFoldersClient(DataLibrariesFoldersClientProtocol):
    """Client for data libraries folders endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def data_libraries_folders_contents_index(
        self,
        folder_id: str,
        limit: int | None = None,
        offset: int | None = None,
        search_text: DataLibrariesFoldersContentsIndexParamSearchText | None = None,
        include_deleted: DataLibrariesFoldersContentsIndexParamIncludeDeleted | None = None,
        order_by: str | None = None,
        sort_desc: DataLibrariesFoldersContentsIndexParamSortDesc | None = None,
        run_as: DataLibrariesFoldersContentsIndexParamRunAs | None = None,
    ) -> LibraryFolderContentsIndexResult:
        """
        Returns a list of a folder's contents (files and sub-folders) with additional metadata
        about the folder.

        Returns a list of a folder's contents (files and sub-folders).  Additional metadata for
        the folder is provided in the response as a separate object containing data for
        breadcrumb path building, permissions and other folder's details.  *Note*: When sorting,
        folders always have priority (they show-up before any dataset regardless of the
        sorting).  **Security note**: - Accessing a library folder or sub-folder requires only
        access to the parent library. - Deleted folders can only be accessed by admins or users
        with `MODIFY` permission. - Datasets may be public, private or restricted (to a group of
        users). Listing deleted datasets has the same requirements as folders.

        Args:
            folder_id (str)          : The encoded identifier of the library folder.
            limit (int | None)       : Maximum number of contents to return.
            offset (int | None)      : Return contents from this specified position. For
                                       example, if ``limit`` is set to 100 and ``offset`` to
                                       200, contents between position 200-299 will be returned.
            search_text (DataLibrariesFoldersContentsIndexParamSearchText | None)
                                     : Used to filter the contents. Only the folders and files
                                       which name contains this text will be returned.
            include_deleted (DataLibrariesFoldersContentsIndexParamIncludeDeleted | None)
                                     : Returns also deleted contents. Deleted contents can only
                                       be retrieved by Administrators or users with
            order_by (str | None)    : Sort results by specified field.
            sort_desc (DataLibrariesFoldersContentsIndexParamSortDesc | None)
                                     : Sort results in descending order.
            run-as (DataLibrariesFoldersContentsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibraryFolderContentsIndexResult: The contents of the folder that match the query
                                              parameters.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        folder_id = DataclassSerializer.serialize(folder_id)

        url = f"{self.base_url}/api/folders/{folder_id}/contents"

        params: dict[str, Any] = {
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"search_text": DataclassSerializer.serialize(search_text)} if search_text is not None else {}),
            **(
                {"include_deleted": DataclassSerializer.serialize(include_deleted)}
                if include_deleted is not None
                else {}
            ),
            **({"order_by": DataclassSerializer.serialize(order_by)} if order_by is not None else {}),
            **({"sort_desc": DataclassSerializer.serialize(sort_desc)} if sort_desc is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderContentsIndexResult)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_contents_index(
        self,
        folder_id: str,
        limit: int | None = None,
        offset: int | None = None,
        search_text: DataLibrariesFoldersContentsIndexParamSearchText | None = None,
        include_deleted: DataLibrariesFoldersContentsIndexParamIncludeDeleted | None = None,
        order_by: str | None = None,
        sort_desc: DataLibrariesFoldersContentsIndexParamSortDesc | None = None,
        run_as: DataLibrariesFoldersContentsIndexParamRunAs | None = None,
    ) -> LibraryFolderContentsIndexResult:
        """
        Returns a list of a folder's contents (files and sub-folders) with additional metadata
        about the folder.

        Returns a list of a folder's contents (files and sub-folders).  Additional metadata for
        the folder is provided in the response as a separate object containing data for
        breadcrumb path building, permissions and other folder's details.  *Note*: When sorting,
        folders always have priority (they show-up before any dataset regardless of the
        sorting).  **Security note**: - Accessing a library folder or sub-folder requires only
        access to the parent library. - Deleted folders can only be accessed by admins or users
        with `MODIFY` permission. - Datasets may be public, private or restricted (to a group of
        users). Listing deleted datasets has the same requirements as folders.

        Args:
            folder_id (str)          : The encoded identifier of the library folder.
            limit (int | None)       : Maximum number of contents to return.
            offset (int | None)      : Return contents from this specified position. For
                                       example, if ``limit`` is set to 100 and ``offset`` to
                                       200, contents between position 200-299 will be returned.
            search_text (DataLibrariesFoldersContentsIndexParamSearchText | None)
                                     : Used to filter the contents. Only the folders and files
                                       which name contains this text will be returned.
            include_deleted (DataLibrariesFoldersContentsIndexParamIncludeDeleted | None)
                                     : Returns also deleted contents. Deleted contents can only
                                       be retrieved by Administrators or users with
            order_by (str | None)    : Sort results by specified field.
            sort_desc (DataLibrariesFoldersContentsIndexParamSortDesc | None)
                                     : Sort results in descending order.
            run-as (DataLibrariesFoldersContentsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibraryFolderContentsIndexResult: The contents of the folder that match the query
                                              parameters.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        folder_id = DataclassSerializer.serialize(folder_id)

        url = f"{self.base_url}/api/folders/{folder_id}/contents"

        params: dict[str, Any] = {
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"search_text": DataclassSerializer.serialize(search_text)} if search_text is not None else {}),
            **(
                {"include_deleted": DataclassSerializer.serialize(include_deleted)}
                if include_deleted is not None
                else {}
            ),
            **({"order_by": DataclassSerializer.serialize(order_by)} if order_by is not None else {}),
            **({"sort_desc": DataclassSerializer.serialize(sort_desc)} if sort_desc is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderContentsIndexResult)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_contents_create(
        self,
        folder_id: str,
        body: CreateLibraryFilePayload,
        run_as: DataLibrariesFoldersContentsCreateParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Creates a new library file from an existing HDA/HDCA.

        Args:
            folder_id (str)          : The encoded identifier of the library folder.
            run-as (DataLibrariesFoldersContentsCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateLibraryFilePayload)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        folder_id = DataclassSerializer.serialize(folder_id)

        url = f"{self.base_url}/api/folders/{folder_id}/contents"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateLibraryFilePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_contents_create(
        self,
        folder_id: str,
        body: CreateLibraryFilePayload,
        run_as: DataLibrariesFoldersContentsCreateParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Creates a new library file from an existing HDA/HDCA.

        Args:
            folder_id (str)          : The encoded identifier of the library folder.
            run-as (DataLibrariesFoldersContentsCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateLibraryFilePayload)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        folder_id = DataclassSerializer.serialize(folder_id)

        url = f"{self.base_url}/api/folders/{folder_id}/contents"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateLibraryFilePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_delete(
        self,
        id_: str,
        undelete: DataLibrariesFoldersDeleteParamUndelete | None = None,
        run_as: DataLibrariesFoldersDeleteParamRunAs | None = None,
    ) -> LibraryFolderDetails:
        """
        Marks the specified library folder as deleted (or undeleted).

        Marks the specified library folder as deleted (or undeleted).

        Args:
            id (str)                 : The encoded identifier of the library folder.
            undelete (DataLibrariesFoldersDeleteParamUndelete | None)
                                     : Whether to restore a deleted library folder.
            run-as (DataLibrariesFoldersDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibraryFolderDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}"

        params: dict[str, Any] = {
            **({"undelete": DataclassSerializer.serialize(undelete)} if undelete is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_delete(
        self,
        id_: str,
        undelete: DataLibrariesFoldersDeleteParamUndelete | None = None,
        run_as: DataLibrariesFoldersDeleteParamRunAs | None = None,
    ) -> LibraryFolderDetails:
        """
        Marks the specified library folder as deleted (or undeleted).

        Marks the specified library folder as deleted (or undeleted).

        Args:
            id (str)                 : The encoded identifier of the library folder.
            undelete (DataLibrariesFoldersDeleteParamUndelete | None)
                                     : Whether to restore a deleted library folder.
            run-as (DataLibrariesFoldersDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibraryFolderDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}"

        params: dict[str, Any] = {
            **({"undelete": DataclassSerializer.serialize(undelete)} if undelete is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_show(
        self,
        id_: str,
        run_as: DataLibrariesFoldersShowParamRunAs | None = None,
    ) -> LibraryFolderDetails:
        """
        Displays information about a particular library folder.

        Returns detailed information about the library folder with the given ID.

        Args:
            id (str)                 : The encoded identifier of the library folder.
            run-as (DataLibrariesFoldersShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibraryFolderDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_show(
        self,
        id_: str,
        run_as: DataLibrariesFoldersShowParamRunAs | None = None,
    ) -> LibraryFolderDetails:
        """
        Displays information about a particular library folder.

        Returns detailed information about the library folder with the given ID.

        Args:
            id (str)                 : The encoded identifier of the library folder.
            run-as (DataLibrariesFoldersShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibraryFolderDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_update(
        self,
        id_: str,
        body: UpdateLibraryFolderPayload,
        run_as: DataLibrariesFoldersUpdateParamRunAs | None = None,
    ) -> LibraryFolderDetails:
        """
        Update

        Updates the information of an existing library folder.

        Args:
            id (str)                 : The encoded identifier of the library folder.
            run-as (DataLibrariesFoldersUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateLibraryFolderPayload)
                                     : Request body. (json)

        Returns:
            LibraryFolderDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UpdateLibraryFolderPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PATCH", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_update(
        self,
        id_: str,
        body: UpdateLibraryFolderPayload,
        run_as: DataLibrariesFoldersUpdateParamRunAs | None = None,
    ) -> LibraryFolderDetails:
        """
        Update

        Updates the information of an existing library folder.

        Args:
            id (str)                 : The encoded identifier of the library folder.
            run-as (DataLibrariesFoldersUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateLibraryFolderPayload)
                                     : Request body. (json)

        Returns:
            LibraryFolderDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UpdateLibraryFolderPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PATCH", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_create(
        self,
        id_: str,
        body: CreateLibraryFolderPayload,
        run_as: DataLibrariesFoldersCreateParamRunAs | None = None,
    ) -> LibraryFolderDetails:
        """
        Create a new library folder underneath the one specified by the ID.

        Returns detailed information about the newly created library folder.

        Args:
            id (str)                 : The encoded identifier of the library folder.
            run-as (DataLibrariesFoldersCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateLibraryFolderPayload)
                                     : Request body. (json)

        Returns:
            LibraryFolderDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateLibraryFolderPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_create(
        self,
        id_: str,
        body: CreateLibraryFolderPayload,
        run_as: DataLibrariesFoldersCreateParamRunAs | None = None,
    ) -> LibraryFolderDetails:
        """
        Create a new library folder underneath the one specified by the ID.

        Returns detailed information about the newly created library folder.

        Args:
            id (str)                 : The encoded identifier of the library folder.
            run-as (DataLibrariesFoldersCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateLibraryFolderPayload)
                                     : Request body. (json)

        Returns:
            LibraryFolderDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateLibraryFolderPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_update_2(
        self,
        id_: str,
        body: UpdateLibraryFolderPayload,
        run_as: DataLibrariesFoldersUpdateParamRunAs2 | None = None,
    ) -> LibraryFolderDetails:
        """
        Updates the information of an existing library folder.

        Updates the information of an existing library folder.

        Args:
            id (str)                 : The encoded identifier of the library folder.
            run-as (DataLibrariesFoldersUpdateParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateLibraryFolderPayload)
                                     : Request body. (json)

        Returns:
            LibraryFolderDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UpdateLibraryFolderPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_update_2(
        self,
        id_: str,
        body: UpdateLibraryFolderPayload,
        run_as: DataLibrariesFoldersUpdateParamRunAs2 | None = None,
    ) -> LibraryFolderDetails:
        """
        Updates the information of an existing library folder.

        Updates the information of an existing library folder.

        Args:
            id (str)                 : The encoded identifier of the library folder.
            run-as (DataLibrariesFoldersUpdateParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateLibraryFolderPayload)
                                     : Request body. (json)

        Returns:
            LibraryFolderDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UpdateLibraryFolderPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_permissions_get_permissions(
        self,
        id_: str,
        scope: DataLibrariesFoldersPermissionsGetPermissionsParamScope | None = None,
        page: int | None = None,
        page_limit: int | None = None,
        q: DataLibrariesFoldersPermissionsGetPermissionsParamQ | None = None,
        run_as: DataLibrariesFoldersPermissionsGetPermissionsParamRunAs | None = None,
    ) -> DataLibrariesFoldersPermissionsGetPermissions200Response:
        """
        Gets the current or available permissions of a particular library folder.

        Gets the current or available permissions of a particular library. The results can be
        paginated and additionally filtered by a query.

        Args:
            id (str)                 : The encoded identifier of the library folder.
            scope (DataLibrariesFoldersPermissionsGetPermissionsParamScope | None)
                                     : The scope of the permissions to retrieve. Either the
                                       `current` permissions or the `available`.
            page (int | None)        : The page number to retrieve when paginating the available
                                       roles.
            page_limit (int | None)  : The maximum number of permissions per page when
                                       paginating.
            q (DataLibrariesFoldersPermissionsGetPermissionsParamQ | None)
                                     : Optional search text to retrieve only the roles matching
                                       this query.
            run-as (DataLibrariesFoldersPermissionsGetPermissionsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DataLibrariesFoldersPermissionsGetPermissions200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}/permissions"

        params: dict[str, Any] = {
            **({"scope": DataclassSerializer.serialize(scope)} if scope is not None else {}),
            **({"page": DataclassSerializer.serialize(page)} if page is not None else {}),
            **({"page_limit": DataclassSerializer.serialize(page_limit)} if page_limit is not None else {}),
            **({"q": DataclassSerializer.serialize(q)} if q is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DataLibrariesFoldersPermissionsGetPermissions200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_permissions_get_permissions(
        self,
        id_: str,
        scope: DataLibrariesFoldersPermissionsGetPermissionsParamScope | None = None,
        page: int | None = None,
        page_limit: int | None = None,
        q: DataLibrariesFoldersPermissionsGetPermissionsParamQ | None = None,
        run_as: DataLibrariesFoldersPermissionsGetPermissionsParamRunAs | None = None,
    ) -> DataLibrariesFoldersPermissionsGetPermissions200Response:
        """
        Gets the current or available permissions of a particular library folder.

        Gets the current or available permissions of a particular library. The results can be
        paginated and additionally filtered by a query.

        Args:
            id (str)                 : The encoded identifier of the library folder.
            scope (DataLibrariesFoldersPermissionsGetPermissionsParamScope | None)
                                     : The scope of the permissions to retrieve. Either the
                                       `current` permissions or the `available`.
            page (int | None)        : The page number to retrieve when paginating the available
                                       roles.
            page_limit (int | None)  : The maximum number of permissions per page when
                                       paginating.
            q (DataLibrariesFoldersPermissionsGetPermissionsParamQ | None)
                                     : Optional search text to retrieve only the roles matching
                                       this query.
            run-as (DataLibrariesFoldersPermissionsGetPermissionsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DataLibrariesFoldersPermissionsGetPermissions200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}/permissions"

        params: dict[str, Any] = {
            **({"scope": DataclassSerializer.serialize(scope)} if scope is not None else {}),
            **({"page": DataclassSerializer.serialize(page)} if page is not None else {}),
            **({"page_limit": DataclassSerializer.serialize(page_limit)} if page_limit is not None else {}),
            **({"q": DataclassSerializer.serialize(q)} if q is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DataLibrariesFoldersPermissionsGetPermissions200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_permissions_set_permissions(
        self,
        id_: str,
        body: LibraryFolderPermissionsPayload,
        action: DataLibrariesFoldersPermissionsSetPermissionsParamAction | None = None,
        run_as: DataLibrariesFoldersPermissionsSetPermissionsParamRunAs | None = None,
    ) -> LibraryFolderCurrentPermissions:
        """
        Sets the permissions to manage a library folder.

        Sets the permissions to manage a library folder.

        Args:
            id (str)                 : The encoded identifier of the library folder.
            action (DataLibrariesFoldersPermissionsSetPermissionsParamAction | None)
                                     : Indicates what action should be performed on the Library.
                                       Currently only `set_permissions` is supported.
            run-as (DataLibrariesFoldersPermissionsSetPermissionsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (LibraryFolderPermissionsPayload)
                                     : Request body. (json)

        Returns:
            LibraryFolderCurrentPermissions: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}/permissions"

        params: dict[str, Any] = {
            **({"action": DataclassSerializer.serialize(action)} if action is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: LibraryFolderPermissionsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderCurrentPermissions)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def data_libraries_folders_permissions_set_permissions(
        self,
        id_: str,
        body: LibraryFolderPermissionsPayload,
        action: DataLibrariesFoldersPermissionsSetPermissionsParamAction | None = None,
        run_as: DataLibrariesFoldersPermissionsSetPermissionsParamRunAs | None = None,
    ) -> LibraryFolderCurrentPermissions:
        """
        Sets the permissions to manage a library folder.

        Sets the permissions to manage a library folder.

        Args:
            id (str)                 : The encoded identifier of the library folder.
            action (DataLibrariesFoldersPermissionsSetPermissionsParamAction | None)
                                     : Indicates what action should be performed on the Library.
                                       Currently only `set_permissions` is supported.
            run-as (DataLibrariesFoldersPermissionsSetPermissionsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (LibraryFolderPermissionsPayload)
                                     : Request body. (json)

        Returns:
            LibraryFolderCurrentPermissions: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/folders/{id_}/permissions"

        params: dict[str, Any] = {
            **({"action": DataclassSerializer.serialize(action)} if action is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: LibraryFolderPermissionsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryFolderCurrentPermissions)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
