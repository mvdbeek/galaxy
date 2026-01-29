from typing import TYPE_CHECKING, Any

from ...models.create_metrics_payload import CreateMetricsPayload
from ...models.metrics_create_param_run_as import MetricsCreateParamRunAs

if TYPE_CHECKING:
    pass


class MockMetricsClient:
    """
    Mock implementation of MetricsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestMetricsClient(MockMetricsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def metrics_create(
        self,
        body: CreateMetricsPayload,
        run_as: MetricsCreateParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockMetricsClient.metrics_create() not implemented. Override this method in your test subclass."
        )
