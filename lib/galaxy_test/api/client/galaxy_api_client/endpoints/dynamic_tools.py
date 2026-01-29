from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.dynamic_tools_build_build_param_run_as import DynamicToolsBuildBuildParamRunAs
from ..models.dynamic_tools_create_param_run_as import DynamicToolsCreateParamRunAs
from ..models.dynamic_tools_create_param_run_as_2 import DynamicToolsCreateParamRunAs2
from ..models.dynamic_tools_create_request_body import DynamicToolsCreateRequestBody
from ..models.dynamic_tools_delete_200_response import DynamicToolsDelete200Response
from ..models.dynamic_tools_delete_param_dynamic_tool_id import DynamicToolsDeleteParamDynamicToolId
from ..models.dynamic_tools_delete_param_run_as import DynamicToolsDeleteParamRunAs
from ..models.dynamic_tools_delete_param_run_as_2 import DynamicToolsDeleteParamRunAs2
from ..models.dynamic_tools_index_param_run_as import DynamicToolsIndexParamRunAs
from ..models.dynamic_tools_runtime_model_runtime_model_param_run_as import (
    DynamicToolsRuntimeModelRuntimeModelParamRunAs,
)
from ..models.dynamic_tools_show_param_dynamic_tool_id import DynamicToolsShowParamDynamicToolId
from ..models.dynamic_tools_show_param_run_as import DynamicToolsShowParamRunAs
from ..models.dynamic_unprivileged_tool_create_payload import DynamicUnprivilegedToolCreatePayload
from ..models.unprivileged_tool_response import UnprivilegedToolResponse


@runtime_checkable
class DynamicToolsClientProtocol(Protocol):
    """Protocol defining the interface of DynamicToolsClient for dependency injection."""

    async def dynamic_tools_index(
        self,
    ) -> dict[str, Any]: ...

    async def dynamic_tools_index(
        self,
    ) -> dict[str, Any]: ...

    async def dynamic_tools_create(
        self,
        body: DynamicToolsCreateRequestBody,
        run_as: DynamicToolsCreateParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def dynamic_tools_create(
        self,
        body: DynamicToolsCreateRequestBody,
        run_as: DynamicToolsCreateParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def dynamic_tools_delete(
        self,
        dynamic_tool_id: DynamicToolsDeleteParamDynamicToolId,
        run_as: DynamicToolsDeleteParamRunAs | None = None,
    ) -> DynamicToolsDelete200Response: ...

    async def dynamic_tools_delete(
        self,
        dynamic_tool_id: DynamicToolsDeleteParamDynamicToolId,
        run_as: DynamicToolsDeleteParamRunAs | None = None,
    ) -> DynamicToolsDelete200Response: ...

    async def dynamic_tools_show(
        self,
        dynamic_tool_id: DynamicToolsShowParamDynamicToolId,
    ) -> dict[str, Any]: ...

    async def dynamic_tools_show(
        self,
        dynamic_tool_id: DynamicToolsShowParamDynamicToolId,
    ) -> dict[str, Any]: ...

    async def dynamic_tools_index_2(
        self,
        active: bool | None = None,
        run_as: DynamicToolsIndexParamRunAs | None = None,
    ) -> list[UnprivilegedToolResponse]: ...

    async def dynamic_tools_index_2(
        self,
        active: bool | None = None,
        run_as: DynamicToolsIndexParamRunAs | None = None,
    ) -> list[UnprivilegedToolResponse]: ...

    async def dynamic_tools_create_2(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsCreateParamRunAs2 | None = None,
    ) -> UnprivilegedToolResponse: ...

    async def dynamic_tools_create_2(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsCreateParamRunAs2 | None = None,
    ) -> UnprivilegedToolResponse: ...

    async def dynamic_tools_build_build(
        self,
        history_id: str,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsBuildBuildParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def dynamic_tools_build_build(
        self,
        history_id: str,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsBuildBuildParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def dynamic_tools_runtime_model_runtime_model(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsRuntimeModelRuntimeModelParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def dynamic_tools_runtime_model_runtime_model(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsRuntimeModelRuntimeModelParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def dynamic_tools_delete_2(
        self,
        uuid_: str,
        run_as: DynamicToolsDeleteParamRunAs2 | None = None,
    ) -> dict[str, Any]: ...

    async def dynamic_tools_delete_2(
        self,
        uuid_: str,
        run_as: DynamicToolsDeleteParamRunAs2 | None = None,
    ) -> dict[str, Any]: ...

    async def dynamic_tools_show_2(
        self,
        uuid_: str,
        run_as: DynamicToolsShowParamRunAs | None = None,
    ) -> UnprivilegedToolResponse: ...

    async def dynamic_tools_show_2(
        self,
        uuid_: str,
        run_as: DynamicToolsShowParamRunAs | None = None,
    ) -> UnprivilegedToolResponse: ...


class DynamicToolsClient(DynamicToolsClientProtocol):
    """Client for dynamic_tools endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def dynamic_tools_index(
        self,
    ) -> dict[str, Any]:
        """
        Index

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dynamic_tools"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_index(
        self,
    ) -> dict[str, Any]:
        """
        Index

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dynamic_tools"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_create(
        self,
        body: DynamicToolsCreateRequestBody,
        run_as: DynamicToolsCreateParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Create

        Args:
            run-as (DynamicToolsCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicToolsCreateRequestBody)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dynamic_tools"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DynamicToolsCreateRequestBody = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_create(
        self,
        body: DynamicToolsCreateRequestBody,
        run_as: DynamicToolsCreateParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Create

        Args:
            run-as (DynamicToolsCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicToolsCreateRequestBody)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dynamic_tools"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DynamicToolsCreateRequestBody = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_delete(
        self,
        dynamic_tool_id: DynamicToolsDeleteParamDynamicToolId,
        run_as: DynamicToolsDeleteParamRunAs | None = None,
    ) -> DynamicToolsDelete200Response:
        """
        Delete

        DELETE /api/dynamic_tools/{encoded_dynamic_tool_id|tool_uuid}  Deactivate the specified
        dynamic tool. Deactivated tools will not be loaded into the toolbox.

        Args:
            dynamic_tool_id (DynamicToolsDeleteParamDynamicToolId)
                                     :
            run-as (DynamicToolsDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DynamicToolsDelete200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dynamic_tool_id = DataclassSerializer.serialize(dynamic_tool_id)

        url = f"{self.base_url}/api/dynamic_tools/{dynamic_tool_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DynamicToolsDelete200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_delete(
        self,
        dynamic_tool_id: DynamicToolsDeleteParamDynamicToolId,
        run_as: DynamicToolsDeleteParamRunAs | None = None,
    ) -> DynamicToolsDelete200Response:
        """
        Delete

        DELETE /api/dynamic_tools/{encoded_dynamic_tool_id|tool_uuid}  Deactivate the specified
        dynamic tool. Deactivated tools will not be loaded into the toolbox.

        Args:
            dynamic_tool_id (DynamicToolsDeleteParamDynamicToolId)
                                     :
            run-as (DynamicToolsDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DynamicToolsDelete200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dynamic_tool_id = DataclassSerializer.serialize(dynamic_tool_id)

        url = f"{self.base_url}/api/dynamic_tools/{dynamic_tool_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DynamicToolsDelete200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_show(
        self,
        dynamic_tool_id: DynamicToolsShowParamDynamicToolId,
    ) -> dict[str, Any]:
        """
        Show

        Args:
            dynamic_tool_id (DynamicToolsShowParamDynamicToolId)
                                     :

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dynamic_tool_id = DataclassSerializer.serialize(dynamic_tool_id)

        url = f"{self.base_url}/api/dynamic_tools/{dynamic_tool_id}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_show(
        self,
        dynamic_tool_id: DynamicToolsShowParamDynamicToolId,
    ) -> dict[str, Any]:
        """
        Show

        Args:
            dynamic_tool_id (DynamicToolsShowParamDynamicToolId)
                                     :

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dynamic_tool_id = DataclassSerializer.serialize(dynamic_tool_id)

        url = f"{self.base_url}/api/dynamic_tools/{dynamic_tool_id}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_index_2(
        self,
        active: bool | None = None,
        run_as: DynamicToolsIndexParamRunAs | None = None,
    ) -> list[UnprivilegedToolResponse]:
        """
        Index

        Args:
            active (bool | None)     :
            run-as (DynamicToolsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UnprivilegedToolResponse]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools"

        params: dict[str, Any] = {
            **({"active": DataclassSerializer.serialize(active)} if active is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[UnprivilegedToolResponse])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_index_2(
        self,
        active: bool | None = None,
        run_as: DynamicToolsIndexParamRunAs | None = None,
    ) -> list[UnprivilegedToolResponse]:
        """
        Index

        Args:
            active (bool | None)     :
            run-as (DynamicToolsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UnprivilegedToolResponse]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools"

        params: dict[str, Any] = {
            **({"active": DataclassSerializer.serialize(active)} if active is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[UnprivilegedToolResponse])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_create_2(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsCreateParamRunAs2 | None = None,
    ) -> UnprivilegedToolResponse:
        """
        Create

        Args:
            run-as (DynamicToolsCreateParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicUnprivilegedToolCreatePayload)
                                     : Request body. (json)

        Returns:
            UnprivilegedToolResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DynamicUnprivilegedToolCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UnprivilegedToolResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_create_2(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsCreateParamRunAs2 | None = None,
    ) -> UnprivilegedToolResponse:
        """
        Create

        Args:
            run-as (DynamicToolsCreateParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicUnprivilegedToolCreatePayload)
                                     : Request body. (json)

        Returns:
            UnprivilegedToolResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DynamicUnprivilegedToolCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UnprivilegedToolResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_build_build(
        self,
        history_id: str,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsBuildBuildParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Build

        Args:
            history_id (str)         :
            run-as (DynamicToolsBuildBuildParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicUnprivilegedToolCreatePayload)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools/build"

        params: dict[str, Any] = {
            "history_id": DataclassSerializer.serialize(history_id),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DynamicUnprivilegedToolCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_build_build(
        self,
        history_id: str,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsBuildBuildParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Build

        Args:
            history_id (str)         :
            run-as (DynamicToolsBuildBuildParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicUnprivilegedToolCreatePayload)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools/build"

        params: dict[str, Any] = {
            "history_id": DataclassSerializer.serialize(history_id),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DynamicUnprivilegedToolCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_runtime_model_runtime_model(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsRuntimeModelRuntimeModelParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Runtime Model

        Args:
            run-as (DynamicToolsRuntimeModelRuntimeModelParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicUnprivilegedToolCreatePayload)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools/runtime_model"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DynamicUnprivilegedToolCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_runtime_model_runtime_model(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsRuntimeModelRuntimeModelParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Runtime Model

        Args:
            run-as (DynamicToolsRuntimeModelRuntimeModelParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicUnprivilegedToolCreatePayload)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools/runtime_model"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DynamicUnprivilegedToolCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_delete_2(
        self,
        uuid_: str,
        run_as: DynamicToolsDeleteParamRunAs2 | None = None,
    ) -> dict[str, Any]:
        """
        Delete

        DELETE /api/unprivileged_tools/{encoded_dynamic_tool_id|tool_uuid}  Deactivate the
        specified dynamic tool. Deactivated tools will not be loaded into the toolbox.

        Args:
            uuid (str)               :
            run-as (DynamicToolsDeleteParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/unprivileged_tools/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_delete_2(
        self,
        uuid_: str,
        run_as: DynamicToolsDeleteParamRunAs2 | None = None,
    ) -> dict[str, Any]:
        """
        Delete

        DELETE /api/unprivileged_tools/{encoded_dynamic_tool_id|tool_uuid}  Deactivate the
        specified dynamic tool. Deactivated tools will not be loaded into the toolbox.

        Args:
            uuid (str)               :
            run-as (DynamicToolsDeleteParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/unprivileged_tools/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_show_2(
        self,
        uuid_: str,
        run_as: DynamicToolsShowParamRunAs | None = None,
    ) -> UnprivilegedToolResponse:
        """
        Show

        Args:
            uuid (str)               :
            run-as (DynamicToolsShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UnprivilegedToolResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/unprivileged_tools/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UnprivilegedToolResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def dynamic_tools_show_2(
        self,
        uuid_: str,
        run_as: DynamicToolsShowParamRunAs | None = None,
    ) -> UnprivilegedToolResponse:
        """
        Show

        Args:
            uuid (str)               :
            run-as (DynamicToolsShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UnprivilegedToolResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/unprivileged_tools/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UnprivilegedToolResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
