from typing import TYPE_CHECKING

from ...models.api_key_response_2 import ApiKeyResponse2

if TYPE_CHECKING:
    pass


class MockAuthenticateClient:
    """
    Mock implementation of AuthenticateClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestAuthenticateClient(MockAuthenticateClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def authenticate_baseauth_get_api_key(
        self,
    ) -> ApiKeyResponse2:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockAuthenticateClient.authenticate_baseauth_get_api_key() not implemented. Override this method in your test subclass."
        )
