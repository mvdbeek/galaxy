from typing import TYPE_CHECKING

from ...models.item_tags_payload import ItemTagsPayload
from ...models.tags_update_param_run_as import TagsUpdateParamRunAs

if TYPE_CHECKING:
    pass


class MockTagsClient:
    """
    Mock implementation of TagsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestTagsClient(MockTagsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def tags_update(
        self,
        body: ItemTagsPayload,
        run_as: TagsUpdateParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockTagsClient.tags_update() not implemented. Override this method in your test subclass."
        )
