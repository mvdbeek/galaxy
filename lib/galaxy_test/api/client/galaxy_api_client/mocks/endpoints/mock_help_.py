from typing import TYPE_CHECKING

from ...models.help_forum_search_response import HelpForumSearchResponse
from ...models.help_forum_search_search_forum_param_run_as import HelpForumSearchSearchForumParamRunAs

if TYPE_CHECKING:
    pass


class MockHelp_Client:
    """
    Mock implementation of Help_Client for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestHelp_Client(MockHelp_Client):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def help_forum_search_search_forum(
        self,
        query: str,
        run_as: HelpForumSearchSearchForumParamRunAs | None = None,
    ) -> HelpForumSearchResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHelp_Client.help_forum_search_search_forum() not implemented. Override this method in your test subclass."
        )
