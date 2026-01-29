from typing import TYPE_CHECKING

from ...models.context_index_param_run_as import ContextIndexParamRunAs
from ...models.context_response import ContextResponse

if TYPE_CHECKING:
    pass


class MockContextClient:
    """
    Mock implementation of ContextClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestContextClient(MockContextClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def context_index(
        self,
        run_as: ContextIndexParamRunAs | None = None,
    ) -> ContextResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockContextClient.context_index() not implemented. Override this method in your test subclass."
        )
