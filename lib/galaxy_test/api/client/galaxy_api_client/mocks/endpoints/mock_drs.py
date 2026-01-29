from typing import TYPE_CHECKING, Any

from ...models.drs_download_param_run_as import DrsDownloadParamRunAs
from ...models.drs_object import DrsObject
from ...models.drs_v_1_objects_access_get_access_url_param_run_as import DrsV1ObjectsAccessGetAccessUrlParamRunAs
from ...models.drs_v_1_objects_access_get_access_url_param_run_as_2 import DrsV1ObjectsAccessGetAccessUrlParamRunAs2
from ...models.drs_v_1_objects_get_object_param_run_as import DrsV1ObjectsGetObjectParamRunAs
from ...models.drs_v_1_objects_get_object_param_run_as_2 import DrsV1ObjectsGetObjectParamRunAs2
from ...models.service import Service

if TYPE_CHECKING:
    pass


class MockDrsClient:
    """
    Mock implementation of DrsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestDrsClient(MockDrsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def drs_download(
        self,
        object_id: str,
        run_as: DrsDownloadParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDrsClient.drs_download() not implemented. Override this method in your test subclass."
        )

    async def drs_v1_objects_get_object(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs | None = None,
    ) -> DrsObject:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDrsClient.drs_v1_objects_get_object() not implemented. Override this method in your test subclass."
        )

    async def drs_v1_objects_get_object_2(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs2 | None = None,
    ) -> DrsObject:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDrsClient.drs_v1_objects_get_object_2() not implemented. Override this method in your test subclass."
        )

    async def drs_v1_objects_access_get_access_url(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDrsClient.drs_v1_objects_access_get_access_url() not implemented. Override this method in your test subclass."
        )

    async def drs_v1_objects_access_get_access_url_2(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs2 | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDrsClient.drs_v1_objects_access_get_access_url_2() not implemented. Override this method in your test subclass."
        )

    async def drs_v1_service_info_service_info(
        self,
    ) -> Service:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDrsClient.drs_v1_service_info_service_info() not implemented. Override this method in your test subclass."
        )
