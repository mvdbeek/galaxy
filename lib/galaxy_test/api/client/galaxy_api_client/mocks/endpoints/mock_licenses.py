from typing import TYPE_CHECKING, Any

from ...models.license_metadata_model import LicenseMetadataModel

if TYPE_CHECKING:
    pass


class MockLicensesClient:
    """
    Mock implementation of LicensesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestLicensesClient(MockLicensesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def licenses_index(
        self,
    ) -> list[LicenseMetadataModel]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLicensesClient.licenses_index() not implemented. Override this method in your test subclass."
        )

    async def licenses_get(
        self,
        id_: dict[str, Any],
    ) -> LicenseMetadataModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLicensesClient.licenses_get() not implemented. Override this method in your test subclass."
        )
