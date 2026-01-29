from typing import TYPE_CHECKING, Any

from ...models.oauth_2_oauth_2_callback_param_code import Oauth2Oauth2CallbackParamCode
from ...models.oauth_2_oauth_2_callback_param_error import Oauth2Oauth2CallbackParamError
from ...models.oauth_2_oauth_2_callback_param_run_as import Oauth2Oauth2CallbackParamRunAs

if TYPE_CHECKING:
    pass


class MockOauth2Client:
    """
    Mock implementation of Oauth2Client for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestOauth2Client(MockOauth2Client):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def oauth2_oauth2_callback(
        self,
        state: str,
        code: Oauth2Oauth2CallbackParamCode | None = None,
        error: Oauth2Oauth2CallbackParamError | None = None,
        run_as: Oauth2Oauth2CallbackParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockOauth2Client.oauth2_oauth2_callback() not implemented. Override this method in your test subclass."
        )
