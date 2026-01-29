from typing import TYPE_CHECKING

from ...models.create_link_feedback import CreateLinkFeedback
from ...models.create_link_incoming import CreateLinkIncoming
from ...models.display_application import DisplayApplication
from ...models.display_applications_create_link_create_link_param_run_as import (
    DisplayApplicationsCreateLinkCreateLinkParamRunAs,
)
from ...models.display_applications_reload_reload_param_run_as import DisplayApplicationsReloadReloadParamRunAs
from ...models.display_applications_reload_reload_request_body import DisplayApplicationsReloadReloadRequestBody
from ...models.reload_feedback import ReloadFeedback

if TYPE_CHECKING:
    pass


class MockDisplayApplicationsClient:
    """
    Mock implementation of DisplayApplicationsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestDisplayApplicationsClient(MockDisplayApplicationsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def display_applications_index(
        self,
    ) -> list[DisplayApplication]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDisplayApplicationsClient.display_applications_index() not implemented. Override this method in your test subclass."
        )

    async def display_applications_create_link_create_link(
        self,
        body: CreateLinkIncoming,
        run_as: DisplayApplicationsCreateLinkCreateLinkParamRunAs | None = None,
    ) -> CreateLinkFeedback:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDisplayApplicationsClient.display_applications_create_link_create_link() not implemented. Override this method in your test subclass."
        )

    async def display_applications_reload_reload(
        self,
        run_as: DisplayApplicationsReloadReloadParamRunAs | None = None,
        body: DisplayApplicationsReloadReloadRequestBody | None = None,
    ) -> ReloadFeedback:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDisplayApplicationsClient.display_applications_reload_reload() not implemented. Override this method in your test subclass."
        )
