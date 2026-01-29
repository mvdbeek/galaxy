from typing import TYPE_CHECKING

from ...models.generate_tour_response import GenerateTourResponse
from ...models.tour_details import TourDetails
from ...models.tour_list import TourList
from ...models.tours_generate_generate_tour_param_run_as import ToursGenerateGenerateTourParamRunAs
from ...models.tours_update_tour_param_run_as import ToursUpdateTourParamRunAs

if TYPE_CHECKING:
    pass


class MockToursClient:
    """
    Mock implementation of ToursClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestToursClient(MockToursClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def tours_index(
        self,
    ) -> TourList:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToursClient.tours_index() not implemented. Override this method in your test subclass."
        )

    async def tours_generate_generate_tour(
        self,
        tool_id: str,
        tool_version: str,
        performs_upload: bool | None = None,
        run_as: ToursGenerateGenerateTourParamRunAs | None = None,
    ) -> GenerateTourResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToursClient.tours_generate_generate_tour() not implemented. Override this method in your test subclass."
        )

    async def tours_show(
        self,
        tour_id: str,
    ) -> TourDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToursClient.tours_show() not implemented. Override this method in your test subclass."
        )

    async def tours_update_tour(
        self,
        tour_id: str,
        run_as: ToursUpdateTourParamRunAs | None = None,
    ) -> TourDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToursClient.tours_update_tour() not implemented. Override this method in your test subclass."
        )
