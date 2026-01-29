from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.drs_download_param_run_as import DrsDownloadParamRunAs
from ..models.drs_object import DrsObject
from ..models.drs_v_1_objects_access_get_access_url_param_run_as import DrsV1ObjectsAccessGetAccessUrlParamRunAs
from ..models.drs_v_1_objects_access_get_access_url_param_run_as_2 import DrsV1ObjectsAccessGetAccessUrlParamRunAs2
from ..models.drs_v_1_objects_get_object_param_run_as import DrsV1ObjectsGetObjectParamRunAs
from ..models.drs_v_1_objects_get_object_param_run_as_2 import DrsV1ObjectsGetObjectParamRunAs2
from ..models.service import Service


@runtime_checkable
class DrsClientProtocol(Protocol):
    """Protocol defining the interface of DrsClient for dependency injection."""

    async def drs_download(
        self,
        object_id: str,
        run_as: DrsDownloadParamRunAs | None = None,
    ) -> None: ...

    async def drs_download(
        self,
        object_id: str,
        run_as: DrsDownloadParamRunAs | None = None,
    ) -> None: ...

    async def drs_v1_objects_get_object(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs | None = None,
    ) -> DrsObject: ...

    async def drs_v1_objects_get_object(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs | None = None,
    ) -> DrsObject: ...

    async def drs_v1_objects_get_object_2(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs2 | None = None,
    ) -> DrsObject: ...

    async def drs_v1_objects_get_object_2(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs2 | None = None,
    ) -> DrsObject: ...

    async def drs_v1_objects_access_get_access_url(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def drs_v1_objects_access_get_access_url(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def drs_v1_objects_access_get_access_url_2(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs2 | None = None,
    ) -> dict[str, Any]: ...

    async def drs_v1_objects_access_get_access_url_2(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs2 | None = None,
    ) -> dict[str, Any]: ...

    async def drs_v1_service_info_service_info(
        self,
    ) -> Service: ...

    async def drs_v1_service_info_service_info(
        self,
    ) -> Service: ...


class DrsClient(DrsClientProtocol):
    """Client for drs endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def drs_download(
        self,
        object_id: str,
        run_as: DrsDownloadParamRunAs | None = None,
    ) -> None:
        """
        Download

        Args:
            object_id (str)          : The ID of the group
            run-as (DrsDownloadParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        object_id = DataclassSerializer.serialize(object_id)

        url = f"{self.base_url}/api/drs_download/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def drs_download(
        self,
        object_id: str,
        run_as: DrsDownloadParamRunAs | None = None,
    ) -> None:
        """
        Download

        Args:
            object_id (str)          : The ID of the group
            run-as (DrsDownloadParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        object_id = DataclassSerializer.serialize(object_id)

        url = f"{self.base_url}/api/drs_download/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def drs_v1_objects_get_object(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs | None = None,
    ) -> DrsObject:
        """
        Get Object

        Args:
            object_id (str)          : The ID of the group
            run-as (DrsV1ObjectsGetObjectParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DrsObject: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        object_id = DataclassSerializer.serialize(object_id)

        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DrsObject)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def drs_v1_objects_get_object(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs | None = None,
    ) -> DrsObject:
        """
        Get Object

        Args:
            object_id (str)          : The ID of the group
            run-as (DrsV1ObjectsGetObjectParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DrsObject: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        object_id = DataclassSerializer.serialize(object_id)

        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DrsObject)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def drs_v1_objects_get_object_2(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs2 | None = None,
    ) -> DrsObject:
        """
        Get Object

        Args:
            object_id (str)          : The ID of the group
            run-as (DrsV1ObjectsGetObjectParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DrsObject: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        object_id = DataclassSerializer.serialize(object_id)

        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DrsObject)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def drs_v1_objects_get_object_2(
        self,
        object_id: str,
        run_as: DrsV1ObjectsGetObjectParamRunAs2 | None = None,
    ) -> DrsObject:
        """
        Get Object

        Args:
            object_id (str)          : The ID of the group
            run-as (DrsV1ObjectsGetObjectParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DrsObject: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        object_id = DataclassSerializer.serialize(object_id)

        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DrsObject)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def drs_v1_objects_access_get_access_url(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Get Access Url

        Args:
            object_id (str)          : The ID of the group
            access_id (str)          : The access ID of the access method for objects, unused in
                                       Galaxy.
            run-as (DrsV1ObjectsAccessGetAccessUrlParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        object_id = DataclassSerializer.serialize(object_id)
        access_id = DataclassSerializer.serialize(access_id)

        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}/access/{access_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def drs_v1_objects_access_get_access_url(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Get Access Url

        Args:
            object_id (str)          : The ID of the group
            access_id (str)          : The access ID of the access method for objects, unused in
                                       Galaxy.
            run-as (DrsV1ObjectsAccessGetAccessUrlParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        object_id = DataclassSerializer.serialize(object_id)
        access_id = DataclassSerializer.serialize(access_id)

        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}/access/{access_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def drs_v1_objects_access_get_access_url_2(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs2 | None = None,
    ) -> dict[str, Any]:
        """
        Get Access Url

        Args:
            object_id (str)          : The ID of the group
            access_id (str)          : The access ID of the access method for objects, unused in
                                       Galaxy.
            run-as (DrsV1ObjectsAccessGetAccessUrlParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        object_id = DataclassSerializer.serialize(object_id)
        access_id = DataclassSerializer.serialize(access_id)

        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}/access/{access_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def drs_v1_objects_access_get_access_url_2(
        self,
        object_id: str,
        access_id: str,
        run_as: DrsV1ObjectsAccessGetAccessUrlParamRunAs2 | None = None,
    ) -> dict[str, Any]:
        """
        Get Access Url

        Args:
            object_id (str)          : The ID of the group
            access_id (str)          : The access ID of the access method for objects, unused in
                                       Galaxy.
            run-as (DrsV1ObjectsAccessGetAccessUrlParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        object_id = DataclassSerializer.serialize(object_id)
        access_id = DataclassSerializer.serialize(access_id)

        url = f"{self.base_url}/ga4gh/drs/v1/objects/{object_id}/access/{access_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def drs_v1_service_info_service_info(
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
                return structure_from_dict(response.json(), Service)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def drs_v1_service_info_service_info(
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
                return structure_from_dict(response.json(), Service)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
