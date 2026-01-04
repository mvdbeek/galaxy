from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport

from ..models.drs_download_param_run_as import DrsDownloadParamRunAs
from ..models.drs_object import DrsObject
from ..models.drs_v_1_objects_access_get_access_url_param_run_as import DrsV1ObjectsAccessGetAccessUrlParamRunAs
from ..models.drs_v_1_objects_get_object_param_run_as import DrsV1ObjectsGetObjectParamRunAs
from ..models.service import Service


class DrsClient:
    """Client for drs endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def drs_download_2_2(
        self,
        object_id: str,
        run_as: DrsDownloadParamRunAs | None = None,
    ) -> None:
        """
        Download

        Args:
            object_id (str)          : The ID of the group
            run-as (Optional[DrsDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/drs_download/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def drs_download_2_2(
        self,
        object_id: str,
        run_as: DrsDownloadParamRunAs | None = None,
    ) -> None:
        """
        Download

        Args:
            object_id (str)          : The ID of the group
            run-as (Optional[DrsDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/drs_download/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def drs_v1_objects_get_object_2_2(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs | None = None,
    ) -> DrsObject:
        """
        Get Object

        Args:
            object_id (str)          : The ID of the group
            run-as (Optional[DrsV1ObjectsGetObjectParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DrsObject: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DrsObject, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def drs_v1_objects_get_object_2_2(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs | None = None,
    ) -> DrsObject:
        """
        Get Object

        Args:
            object_id (str)          : The ID of the group
            run-as (Optional[DrsV1ObjectsGetObjectParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DrsObject: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DrsObject, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def drs_v1_objects_get_object_3_2(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs | None = None,
    ) -> DrsObject:
        """
        Get Object

        Args:
            object_id (str)          : The ID of the group
            run-as (Optional[DrsV1ObjectsGetObjectParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DrsObject: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DrsObject, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def drs_v1_objects_get_object_3_2(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs | None = None,
    ) -> DrsObject:
        """
        Get Object

        Args:
            object_id (str)          : The ID of the group
            run-as (Optional[DrsV1ObjectsGetObjectParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DrsObject: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DrsObject, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def drs_v1_objects_access_get_access_url_2_2(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs | None = None,
    ) -> Any:
        """
        Get Access Url

        Args:
            object_id (str)          : The ID of the group
            access_id (str)          : The access ID of the access method for objects, unused in
                                       Galaxy.
            run-as (Optional[DrsV1ObjectsAccessGetAccessUrlParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}/access/{access_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def drs_v1_objects_access_get_access_url_2_2(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs | None = None,
    ) -> Any:
        """
        Get Access Url

        Args:
            object_id (str)          : The ID of the group
            access_id (str)          : The access ID of the access method for objects, unused in
                                       Galaxy.
            run-as (Optional[DrsV1ObjectsAccessGetAccessUrlParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}/access/{access_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def drs_v1_objects_access_get_access_url_3_2(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs | None = None,
    ) -> Any:
        """
        Get Access Url

        Args:
            object_id (str)          : The ID of the group
            access_id (str)          : The access ID of the access method for objects, unused in
                                       Galaxy.
            run-as (Optional[DrsV1ObjectsAccessGetAccessUrlParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}/access/{access_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def drs_v1_objects_access_get_access_url_3_2(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs | None = None,
    ) -> Any:
        """
        Get Access Url

        Args:
            object_id (str)          : The ID of the group
            access_id (str)          : The access ID of the access method for objects, unused in
                                       Galaxy.
            run-as (Optional[DrsV1ObjectsAccessGetAccessUrlParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}/access/{access_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def drs_v1_service_info_service_info_2_2(
        self,
    ) -> Service:
        """
        Service Info

        Returns:
            Service: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/ga4gh/drs/v1/service-info"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(Service, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def drs_v1_service_info_service_info_2_2(
        self,
    ) -> Service:
        """
        Service Info

        Returns:
            Service: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/ga4gh/drs/v1/service-info"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(Service, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
