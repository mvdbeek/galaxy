from typing import TYPE_CHECKING

from ...models.set_slug_payload import SetSlugPayload
from ...models.share_with_payload import ShareWithPayload
from ...models.share_with_status import ShareWithStatus
from ...models.sharing_status import SharingStatus
from ...models.visualization_create_payload import VisualizationCreatePayload
from ...models.visualization_create_response import VisualizationCreateResponse
from ...models.visualization_show_response import VisualizationShowResponse
from ...models.visualization_summary_list import VisualizationSummaryList
from ...models.visualization_update_payload import VisualizationUpdatePayload
from ...models.visualizations_create_param_import_id import VisualizationsCreateParamImportId
from ...models.visualizations_create_param_run_as import VisualizationsCreateParamRunAs
from ...models.visualizations_disable_link_access_disable_link_access_param_run_as import (
    VisualizationsDisableLinkAccessDisableLinkAccessParamRunAs,
)
from ...models.visualizations_enable_link_access_enable_link_access_param_run_as import (
    VisualizationsEnableLinkAccessEnableLinkAccessParamRunAs,
)
from ...models.visualizations_index_param_limit import VisualizationsIndexParamLimit
from ...models.visualizations_index_param_offset import VisualizationsIndexParamOffset
from ...models.visualizations_index_param_run_as import VisualizationsIndexParamRunAs
from ...models.visualizations_index_param_search import VisualizationsIndexParamSearch
from ...models.visualizations_index_param_user_id import VisualizationsIndexParamUserId
from ...models.visualizations_publish_publish_param_run_as import VisualizationsPublishPublishParamRunAs
from ...models.visualizations_share_with_users_share_with_users_param_run_as import (
    VisualizationsShareWithUsersShareWithUsersParamRunAs,
)
from ...models.visualizations_sharing_sharing_param_run_as import VisualizationsSharingSharingParamRunAs
from ...models.visualizations_show_param_run_as import VisualizationsShowParamRunAs
from ...models.visualizations_slug_set_slug_param_run_as import VisualizationsSlugSetSlugParamRunAs
from ...models.visualizations_unpublish_unpublish_param_run_as import VisualizationsUnpublishUnpublishParamRunAs
from ...models.visualizations_update_200_response import VisualizationsUpdate200Response
from ...models.visualizations_update_param_run_as import VisualizationsUpdateParamRunAs

if TYPE_CHECKING:
    pass


class MockVisualizationsClient:
    """
    Mock implementation of VisualizationsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestVisualizationsClient(MockVisualizationsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

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
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockVisualizationsClient.visualizations_index() not implemented. Override this method in your test subclass."
        )

    async def visualizations_create(
        self,
        body: VisualizationCreatePayload,
        import_id: VisualizationsCreateParamImportId | None = None,
        run_as: VisualizationsCreateParamRunAs | None = None,
    ) -> VisualizationCreateResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockVisualizationsClient.visualizations_create() not implemented. Override this method in your test subclass."
        )

    async def visualizations_show(
        self,
        id_: str,
        run_as: VisualizationsShowParamRunAs | None = None,
    ) -> VisualizationShowResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockVisualizationsClient.visualizations_show() not implemented. Override this method in your test subclass."
        )

    async def visualizations_update(
        self,
        id_: str,
        body: VisualizationUpdatePayload,
        run_as: VisualizationsUpdateParamRunAs | None = None,
    ) -> VisualizationsUpdate200Response | None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockVisualizationsClient.visualizations_update() not implemented. Override this method in your test subclass."
        )

    async def visualizations_disable_link_access_disable_link_access(
        self,
        id_: str,
        run_as: VisualizationsDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockVisualizationsClient.visualizations_disable_link_access_disable_link_access() not implemented. Override this method in your test subclass."
        )

    async def visualizations_enable_link_access_enable_link_access(
        self,
        id_: str,
        run_as: VisualizationsEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockVisualizationsClient.visualizations_enable_link_access_enable_link_access() not implemented. Override this method in your test subclass."
        )

    async def visualizations_publish_publish(
        self,
        id_: str,
        run_as: VisualizationsPublishPublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockVisualizationsClient.visualizations_publish_publish() not implemented. Override this method in your test subclass."
        )

    async def visualizations_share_with_users_share_with_users(
        self,
        id_: str,
        body: ShareWithPayload,
        run_as: VisualizationsShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockVisualizationsClient.visualizations_share_with_users_share_with_users() not implemented. Override this method in your test subclass."
        )

    async def visualizations_sharing_sharing(
        self,
        id_: str,
        run_as: VisualizationsSharingSharingParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockVisualizationsClient.visualizations_sharing_sharing() not implemented. Override this method in your test subclass."
        )

    async def visualizations_slug_set_slug(
        self,
        id_: str,
        body: SetSlugPayload,
        run_as: VisualizationsSlugSetSlugParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockVisualizationsClient.visualizations_slug_set_slug() not implemented. Override this method in your test subclass."
        )

    async def visualizations_unpublish_unpublish(
        self,
        id_: str,
        run_as: VisualizationsUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockVisualizationsClient.visualizations_unpublish_unpublish() not implemented. Override this method in your test subclass."
        )
