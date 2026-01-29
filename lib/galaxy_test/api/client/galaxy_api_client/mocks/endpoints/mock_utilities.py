from typing import TYPE_CHECKING, Any

from ...models.utilities_proxy_param_run_as import UtilitiesProxyParamRunAs
from ...models.utilities_proxy_param_run_as_2 import UtilitiesProxyParamRunAs2

if TYPE_CHECKING:
    pass


class MockUtilitiesClient:
    """
    Mock implementation of UtilitiesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestUtilitiesClient(MockUtilitiesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def utilities_proxy(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUtilitiesClient.utilities_proxy() not implemented. Override this method in your test subclass."
        )

    async def utilities_proxy_2(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs2 | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUtilitiesClient.utilities_proxy_2() not implemented. Override this method in your test subclass."
        )
