from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    pass


class MockShortTermStorageClient:
    """
    Mock implementation of ShortTermStorageClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestShortTermStorageClient(MockShortTermStorageClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def short_term_storage_serve(
        self,
        storage_request_id: UUID,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockShortTermStorageClient.short_term_storage_serve() not implemented. Override this method in your test subclass."
        )

    async def short_term_storage_ready_is_ready(
        self,
        storage_request_id: UUID,
    ) -> bool:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockShortTermStorageClient.short_term_storage_ready_is_ready() not implemented. Override this method in your test subclass."
        )
