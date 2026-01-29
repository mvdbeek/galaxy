from typing import TYPE_CHECKING, Any

from ...models.forms_delete_param_run_as import FormsDeleteParamRunAs
from ...models.forms_undelete_undelete_param_run_as import FormsUndeleteUndeleteParamRunAs

if TYPE_CHECKING:
    pass


class MockFormsClient:
    """
    Mock implementation of FormsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestFormsClient(MockFormsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def forms_delete(
        self,
        id_: str,
        run_as: FormsDeleteParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockFormsClient.forms_delete() not implemented. Override this method in your test subclass."
        )

    async def forms_undelete_undelete(
        self,
        id_: str,
        run_as: FormsUndeleteUndeleteParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockFormsClient.forms_undelete_undelete() not implemented. Override this method in your test subclass."
        )
