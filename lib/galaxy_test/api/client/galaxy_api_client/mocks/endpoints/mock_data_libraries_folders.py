from typing import TYPE_CHECKING, Any

from ...models.create_library_file_payload import CreateLibraryFilePayload
from ...models.create_library_folder_payload import CreateLibraryFolderPayload
from ...models.data_libraries_folders_contents_create_param_run_as import DataLibrariesFoldersContentsCreateParamRunAs
from ...models.data_libraries_folders_contents_index_param_include_deleted import (
    DataLibrariesFoldersContentsIndexParamIncludeDeleted,
)
from ...models.data_libraries_folders_contents_index_param_run_as import DataLibrariesFoldersContentsIndexParamRunAs
from ...models.data_libraries_folders_contents_index_param_search_text import (
    DataLibrariesFoldersContentsIndexParamSearchText,
)
from ...models.data_libraries_folders_contents_index_param_sort_desc import (
    DataLibrariesFoldersContentsIndexParamSortDesc,
)
from ...models.data_libraries_folders_create_param_run_as import DataLibrariesFoldersCreateParamRunAs
from ...models.data_libraries_folders_delete_param_run_as import DataLibrariesFoldersDeleteParamRunAs
from ...models.data_libraries_folders_delete_param_undelete import DataLibrariesFoldersDeleteParamUndelete
from ...models.data_libraries_folders_permissions_get_permissions_200_response import (
    DataLibrariesFoldersPermissionsGetPermissions200Response,
)
from ...models.data_libraries_folders_permissions_get_permissions_param_q import (
    DataLibrariesFoldersPermissionsGetPermissionsParamQ,
)
from ...models.data_libraries_folders_permissions_get_permissions_param_run_as import (
    DataLibrariesFoldersPermissionsGetPermissionsParamRunAs,
)
from ...models.data_libraries_folders_permissions_get_permissions_param_scope import (
    DataLibrariesFoldersPermissionsGetPermissionsParamScope,
)
from ...models.data_libraries_folders_permissions_set_permissions_param_action import (
    DataLibrariesFoldersPermissionsSetPermissionsParamAction,
)
from ...models.data_libraries_folders_permissions_set_permissions_param_run_as import (
    DataLibrariesFoldersPermissionsSetPermissionsParamRunAs,
)
from ...models.data_libraries_folders_show_param_run_as import DataLibrariesFoldersShowParamRunAs
from ...models.data_libraries_folders_update_param_run_as import DataLibrariesFoldersUpdateParamRunAs
from ...models.data_libraries_folders_update_param_run_as_2 import DataLibrariesFoldersUpdateParamRunAs2
from ...models.library_folder_contents_index_result import LibraryFolderContentsIndexResult
from ...models.library_folder_current_permissions import LibraryFolderCurrentPermissions
from ...models.library_folder_details import LibraryFolderDetails
from ...models.library_folder_permissions_payload import LibraryFolderPermissionsPayload
from ...models.update_library_folder_payload import UpdateLibraryFolderPayload

if TYPE_CHECKING:
    pass


class MockDataLibrariesFoldersClient:
    """
    Mock implementation of DataLibrariesFoldersClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestDataLibrariesFoldersClient(MockDataLibrariesFoldersClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

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
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDataLibrariesFoldersClient.data_libraries_folders_contents_index() not implemented. Override this method in your test subclass."
        )

    async def data_libraries_folders_contents_create(
        self,
        folder_id: str,
        body: CreateLibraryFilePayload,
        run_as: DataLibrariesFoldersContentsCreateParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDataLibrariesFoldersClient.data_libraries_folders_contents_create() not implemented. Override this method in your test subclass."
        )

    async def data_libraries_folders_delete(
        self,
        id_: str,
        undelete: DataLibrariesFoldersDeleteParamUndelete | None = None,
        run_as: DataLibrariesFoldersDeleteParamRunAs | None = None,
    ) -> LibraryFolderDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDataLibrariesFoldersClient.data_libraries_folders_delete() not implemented. Override this method in your test subclass."
        )

    async def data_libraries_folders_show(
        self,
        id_: str,
        run_as: DataLibrariesFoldersShowParamRunAs | None = None,
    ) -> LibraryFolderDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDataLibrariesFoldersClient.data_libraries_folders_show() not implemented. Override this method in your test subclass."
        )

    async def data_libraries_folders_update(
        self,
        id_: str,
        body: UpdateLibraryFolderPayload,
        run_as: DataLibrariesFoldersUpdateParamRunAs | None = None,
    ) -> LibraryFolderDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDataLibrariesFoldersClient.data_libraries_folders_update() not implemented. Override this method in your test subclass."
        )

    async def data_libraries_folders_create(
        self,
        id_: str,
        body: CreateLibraryFolderPayload,
        run_as: DataLibrariesFoldersCreateParamRunAs | None = None,
    ) -> LibraryFolderDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDataLibrariesFoldersClient.data_libraries_folders_create() not implemented. Override this method in your test subclass."
        )

    async def data_libraries_folders_update_2(
        self,
        id_: str,
        body: UpdateLibraryFolderPayload,
        run_as: DataLibrariesFoldersUpdateParamRunAs2 | None = None,
    ) -> LibraryFolderDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDataLibrariesFoldersClient.data_libraries_folders_update_2() not implemented. Override this method in your test subclass."
        )

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
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDataLibrariesFoldersClient.data_libraries_folders_permissions_get_permissions() not implemented. Override this method in your test subclass."
        )

    async def data_libraries_folders_permissions_set_permissions(
        self,
        id_: str,
        body: LibraryFolderPermissionsPayload,
        action: DataLibrariesFoldersPermissionsSetPermissionsParamAction | None = None,
        run_as: DataLibrariesFoldersPermissionsSetPermissionsParamRunAs | None = None,
    ) -> LibraryFolderCurrentPermissions:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDataLibrariesFoldersClient.data_libraries_folders_permissions_set_permissions() not implemented. Override this method in your test subclass."
        )
