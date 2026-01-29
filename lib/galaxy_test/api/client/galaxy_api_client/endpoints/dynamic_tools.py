from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.dynamic_tools_build_build_param_run_as import DynamicToolsBuildBuildParamRunAs
from ..models.dynamic_tools_create_param_run_as import DynamicToolsCreateParamRunAs
from ..models.dynamic_tools_create_request_body_2 import DynamicToolsCreateRequestBody2
from ..models.dynamic_tools_delete_200_response_2 import DynamicToolsDelete200Response2
from ..models.dynamic_tools_delete_param_dynamic_tool_id import DynamicToolsDeleteParamDynamicToolId
from ..models.dynamic_tools_delete_param_run_as import DynamicToolsDeleteParamRunAs
from ..models.dynamic_tools_index_param_run_as import DynamicToolsIndexParamRunAs
from ..models.dynamic_tools_runtime_model_runtime_model_param_run_as import (
    DynamicToolsRuntimeModelRuntimeModelParamRunAs,
)
from ..models.dynamic_tools_show_param_dynamic_tool_id import DynamicToolsShowParamDynamicToolId
from ..models.dynamic_tools_show_param_run_as import DynamicToolsShowParamRunAs
from ..models.dynamic_unprivileged_tool_create_payload import DynamicUnprivilegedToolCreatePayload
from ..models.unprivileged_tool_response import UnprivilegedToolResponse


class DynamicToolsClient:
    """Client for dynamic_tools endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def dynamic_tools_index_2_2(
        self,
    ) -> Any:
        """
        Index

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dynamic_tools"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_index_2_2(
        self,
    ) -> Any:
        """
        Index

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dynamic_tools"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_create_2_2(
        self,
        body: DynamicToolsCreateRequestBody2,
        run_as: DynamicToolsCreateParamRunAs | None = None,
    ) -> Any:
        """
        Create

        Args:
            run-as (Optional[DynamicToolsCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicToolsCreateRequestBody2)
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dynamic_tools"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DynamicToolsCreateRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_create_2_2(
        self,
        body: DynamicToolsCreateRequestBody2,
        run_as: DynamicToolsCreateParamRunAs | None = None,
    ) -> Any:
        """
        Create

        Args:
            run-as (Optional[DynamicToolsCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicToolsCreateRequestBody2)
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dynamic_tools"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DynamicToolsCreateRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_delete_2_2(
        self,
        dynamic_tool_id: DynamicToolsDeleteParamDynamicToolId,
        run_as: DynamicToolsDeleteParamRunAs | None = None,
    ) -> DynamicToolsDelete200Response2:
        """
        Delete

        DELETE /api/dynamic_tools/{encoded_dynamic_tool_id|tool_uuid}  Deactivate the specified
        dynamic tool. Deactivated tools will not be loaded into the toolbox.

        Args:
            dynamic_tool_id (DynamicToolsDeleteParamDynamicToolId)
                                     :
            run-as (Optional[DynamicToolsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DynamicToolsDelete200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dynamic_tools/{dynamic_tool_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DynamicToolsDelete200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_delete_2_2(
        self,
        dynamic_tool_id: DynamicToolsDeleteParamDynamicToolId,
        run_as: DynamicToolsDeleteParamRunAs | None = None,
    ) -> DynamicToolsDelete200Response2:
        """
        Delete

        DELETE /api/dynamic_tools/{encoded_dynamic_tool_id|tool_uuid}  Deactivate the specified
        dynamic tool. Deactivated tools will not be loaded into the toolbox.

        Args:
            dynamic_tool_id (DynamicToolsDeleteParamDynamicToolId)
                                     :
            run-as (Optional[DynamicToolsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DynamicToolsDelete200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dynamic_tools/{dynamic_tool_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DynamicToolsDelete200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_show_2_2(
        self,
        dynamic_tool_id: DynamicToolsShowParamDynamicToolId,
    ) -> Any:
        """
        Show

        Args:
            dynamic_tool_id (DynamicToolsShowParamDynamicToolId)
                                     :

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dynamic_tools/{dynamic_tool_id}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_show_2_2(
        self,
        dynamic_tool_id: DynamicToolsShowParamDynamicToolId,
    ) -> Any:
        """
        Show

        Args:
            dynamic_tool_id (DynamicToolsShowParamDynamicToolId)
                                     :

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dynamic_tools/{dynamic_tool_id}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_index_3_2(
        self,
        active: bool | None = True,
        run_as: DynamicToolsIndexParamRunAs | None = None,
    ) -> list[UnprivilegedToolResponse]:
        """
        Index

        Args:
            active (Optional[bool])  :
            run-as (Optional[DynamicToolsIndexParamRunAs])
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
            **({"active": active} if active is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[UnprivilegedToolResponse], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_index_3_2(
        self,
        active: bool | None = True,
        run_as: DynamicToolsIndexParamRunAs | None = None,
    ) -> list[UnprivilegedToolResponse]:
        """
        Index

        Args:
            active (Optional[bool])  :
            run-as (Optional[DynamicToolsIndexParamRunAs])
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
            **({"active": active} if active is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[UnprivilegedToolResponse], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_create_3_2(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsCreateParamRunAs | None = None,
    ) -> UnprivilegedToolResponse:
        """
        Create

        Args:
            run-as (Optional[DynamicToolsCreateParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DynamicUnprivilegedToolCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UnprivilegedToolResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_create_3_2(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsCreateParamRunAs | None = None,
    ) -> UnprivilegedToolResponse:
        """
        Create

        Args:
            run-as (Optional[DynamicToolsCreateParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DynamicUnprivilegedToolCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UnprivilegedToolResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_build_build_2_2(
        self,
        history_id: str,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsBuildBuildParamRunAs | None = None,
    ) -> Any:
        """
        Build

        Args:
            history_id (str)         :
            run-as (Optional[DynamicToolsBuildBuildParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicUnprivilegedToolCreatePayload)
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools/build"

        params: dict[str, Any] = {
            "history_id": history_id,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DynamicUnprivilegedToolCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_build_build_2_2(
        self,
        history_id: str,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsBuildBuildParamRunAs | None = None,
    ) -> Any:
        """
        Build

        Args:
            history_id (str)         :
            run-as (Optional[DynamicToolsBuildBuildParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicUnprivilegedToolCreatePayload)
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools/build"

        params: dict[str, Any] = {
            "history_id": history_id,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DynamicUnprivilegedToolCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_runtime_model_runtime_model_2_2(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsRuntimeModelRuntimeModelParamRunAs | None = None,
    ) -> Any:
        """
        Runtime Model

        Args:
            run-as (Optional[DynamicToolsRuntimeModelRuntimeModelParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicUnprivilegedToolCreatePayload)
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools/runtime_model"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DynamicUnprivilegedToolCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_runtime_model_runtime_model_2_2(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsRuntimeModelRuntimeModelParamRunAs | None = None,
    ) -> Any:
        """
        Runtime Model

        Args:
            run-as (Optional[DynamicToolsRuntimeModelRuntimeModelParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DynamicUnprivilegedToolCreatePayload)
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools/runtime_model"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DynamicUnprivilegedToolCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_delete_3_2(
        self,
        uuid_: str,
        run_as: DynamicToolsDeleteParamRunAs | None = None,
    ) -> Any:
        """
        Delete

        DELETE /api/unprivileged_tools/{encoded_dynamic_tool_id|tool_uuid}  Deactivate the
        specified dynamic tool. Deactivated tools will not be loaded into the toolbox.

        Args:
            uuid (str)               :
            run-as (Optional[DynamicToolsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_delete_3_2(
        self,
        uuid_: str,
        run_as: DynamicToolsDeleteParamRunAs | None = None,
    ) -> Any:
        """
        Delete

        DELETE /api/unprivileged_tools/{encoded_dynamic_tool_id|tool_uuid}  Deactivate the
        specified dynamic tool. Deactivated tools will not be loaded into the toolbox.

        Args:
            uuid (str)               :
            run-as (Optional[DynamicToolsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_show_3_2(
        self,
        uuid_: str,
        run_as: DynamicToolsShowParamRunAs | None = None,
    ) -> UnprivilegedToolResponse:
        """
        Show

        Args:
            uuid (str)               :
            run-as (Optional[DynamicToolsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UnprivilegedToolResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UnprivilegedToolResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dynamic_tools_show_3_2(
        self,
        uuid_: str,
        run_as: DynamicToolsShowParamRunAs | None = None,
    ) -> UnprivilegedToolResponse:
        """
        Show

        Args:
            uuid (str)               :
            run-as (Optional[DynamicToolsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UnprivilegedToolResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/unprivileged_tools/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UnprivilegedToolResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
