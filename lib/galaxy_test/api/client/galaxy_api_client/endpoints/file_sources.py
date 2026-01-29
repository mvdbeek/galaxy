from typing import Any, Protocol, runtime_checkable
from uuid import UUID

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.create_instance_payload import CreateInstancePayload
from ..models.file_source_template_summaries import FileSourceTemplateSummaries
from ..models.file_sources_create_instance_param_run_as import FileSourcesCreateInstanceParamRunAs
from ..models.file_sources_instances_get_param_run_as import FileSourcesInstancesGetParamRunAs
from ..models.file_sources_instances_index_param_run_as import FileSourcesInstancesIndexParamRunAs
from ..models.file_sources_instances_purge_param_run_as import FileSourcesInstancesPurgeParamRunAs
from ..models.file_sources_instances_test_instance_param_run_as import FileSourcesInstancesTestInstanceParamRunAs
from ..models.file_sources_instances_update_param_run_as import FileSourcesInstancesUpdateParamRunAs
from ..models.file_sources_instances_update_request_body import FileSourcesInstancesUpdateRequestBody
from ..models.file_sources_template_oauth_2_param_run_as import FileSourcesTemplateOauth2ParamRunAs
from ..models.file_sources_templates_index_param_run_as import FileSourcesTemplatesIndexParamRunAs
from ..models.file_sources_test_instances_update_param_run_as import FileSourcesTestInstancesUpdateParamRunAs
from ..models.file_sources_test_instances_update_request_body import FileSourcesTestInstancesUpdateRequestBody
from ..models.file_sources_test_new_instance_configuration_param_run_as import (
    FileSourcesTestNewInstanceConfigurationParamRunAs,
)
from ..models.o_auth_2_info import OAuth2Info
from ..models.plugin_status import PluginStatus
from ..models.user_file_source_model import UserFileSourceModel


@runtime_checkable
class FileSourcesClientProtocol(Protocol):
    """Protocol defining the interface of FileSourcesClient for dependency injection."""

    async def file_sources_instances_index(
        self,
        run_as: FileSourcesInstancesIndexParamRunAs | None = None,
    ) -> list[UserFileSourceModel]: ...

    async def file_sources_instances_index(
        self,
        run_as: FileSourcesInstancesIndexParamRunAs | None = None,
    ) -> list[UserFileSourceModel]: ...

    async def file_sources_create_instance(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesCreateInstanceParamRunAs | None = None,
    ) -> UserFileSourceModel: ...

    async def file_sources_create_instance(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesCreateInstanceParamRunAs | None = None,
    ) -> UserFileSourceModel: ...

    async def file_sources_test_new_instance_configuration(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesTestNewInstanceConfigurationParamRunAs | None = None,
    ) -> PluginStatus: ...

    async def file_sources_test_new_instance_configuration(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesTestNewInstanceConfigurationParamRunAs | None = None,
    ) -> PluginStatus: ...

    async def file_sources_instances_purge(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesPurgeParamRunAs | None = None,
    ) -> None: ...

    async def file_sources_instances_purge(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesPurgeParamRunAs | None = None,
    ) -> None: ...

    async def file_sources_instances_get(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesGetParamRunAs | None = None,
    ) -> UserFileSourceModel: ...

    async def file_sources_instances_get(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesGetParamRunAs | None = None,
    ) -> UserFileSourceModel: ...

    async def file_sources_instances_update(
        self,
        uuid_: UUID,
        body: FileSourcesInstancesUpdateRequestBody,
        run_as: FileSourcesInstancesUpdateParamRunAs | None = None,
    ) -> UserFileSourceModel: ...

    async def file_sources_instances_update(
        self,
        uuid_: UUID,
        body: FileSourcesInstancesUpdateRequestBody,
        run_as: FileSourcesInstancesUpdateParamRunAs | None = None,
    ) -> UserFileSourceModel: ...

    async def file_sources_instances_test_instance(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesTestInstanceParamRunAs | None = None,
    ) -> PluginStatus: ...

    async def file_sources_instances_test_instance(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesTestInstanceParamRunAs | None = None,
    ) -> PluginStatus: ...

    async def file_sources_test_instances_update(
        self,
        uuid_: UUID,
        body: FileSourcesTestInstancesUpdateRequestBody,
        run_as: FileSourcesTestInstancesUpdateParamRunAs | None = None,
    ) -> PluginStatus: ...

    async def file_sources_test_instances_update(
        self,
        uuid_: UUID,
        body: FileSourcesTestInstancesUpdateRequestBody,
        run_as: FileSourcesTestInstancesUpdateParamRunAs | None = None,
    ) -> PluginStatus: ...

    async def file_sources_templates_index(
        self,
        run_as: FileSourcesTemplatesIndexParamRunAs | None = None,
    ) -> FileSourceTemplateSummaries: ...

    async def file_sources_templates_index(
        self,
        run_as: FileSourcesTemplatesIndexParamRunAs | None = None,
    ) -> FileSourceTemplateSummaries: ...

    async def file_sources_template_oauth2(
        self,
        template_id: str,
        template_version: int,
        run_as: FileSourcesTemplateOauth2ParamRunAs | None = None,
    ) -> OAuth2Info: ...

    async def file_sources_template_oauth2(
        self,
        template_id: str,
        template_version: int,
        run_as: FileSourcesTemplateOauth2ParamRunAs | None = None,
    ) -> OAuth2Info: ...


class FileSourcesClient(FileSourcesClientProtocol):
    """Client for file_sources endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def file_sources_instances_index(
        self,
        run_as: FileSourcesInstancesIndexParamRunAs | None = None,
    ) -> list[UserFileSourceModel]:
        """
        Get a list of persisted file source instances defined by the requesting user.

        Args:
            run-as (FileSourcesInstancesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UserFileSourceModel]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[UserFileSourceModel])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_instances_index(
        self,
        run_as: FileSourcesInstancesIndexParamRunAs | None = None,
    ) -> list[UserFileSourceModel]:
        """
        Get a list of persisted file source instances defined by the requesting user.

        Args:
            run-as (FileSourcesInstancesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UserFileSourceModel]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[UserFileSourceModel])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_create_instance(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesCreateInstanceParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Create a user-bound file source.

        Args:
            run-as (FileSourcesCreateInstanceParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateInstancePayload)
                                     : Request body. (json)

        Returns:
            UserFileSourceModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateInstancePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserFileSourceModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_create_instance(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesCreateInstanceParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Create a user-bound file source.

        Args:
            run-as (FileSourcesCreateInstanceParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateInstancePayload)
                                     : Request body. (json)

        Returns:
            UserFileSourceModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateInstancePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserFileSourceModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_test_new_instance_configuration(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesTestNewInstanceConfigurationParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test payload for creating user-bound file source.

        Args:
            run-as (FileSourcesTestNewInstanceConfigurationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateInstancePayload)
                                     : Request body. (json)

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances/test"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateInstancePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PluginStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_test_new_instance_configuration(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesTestNewInstanceConfigurationParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test payload for creating user-bound file source.

        Args:
            run-as (FileSourcesTestNewInstanceConfigurationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateInstancePayload)
                                     : Request body. (json)

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances/test"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateInstancePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PluginStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_instances_purge(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesPurgeParamRunAs | None = None,
    ) -> None:
        """
        Purge user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (FileSourcesInstancesPurgeParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/file_source_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_instances_purge(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesPurgeParamRunAs | None = None,
    ) -> None:
        """
        Purge user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (FileSourcesInstancesPurgeParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/file_source_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_instances_get(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesGetParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Get a persisted user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (FileSourcesInstancesGetParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserFileSourceModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/file_source_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserFileSourceModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_instances_get(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesGetParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Get a persisted user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (FileSourcesInstancesGetParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserFileSourceModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/file_source_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserFileSourceModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_instances_update(
        self,
        uuid_: UUID,
        body: FileSourcesInstancesUpdateRequestBody,
        run_as: FileSourcesInstancesUpdateParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Update or upgrade user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (FileSourcesInstancesUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (FileSourcesInstancesUpdateRequestBody)
                                     : Request body. (json)

        Returns:
            UserFileSourceModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/file_source_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: FileSourcesInstancesUpdateRequestBody = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserFileSourceModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_instances_update(
        self,
        uuid_: UUID,
        body: FileSourcesInstancesUpdateRequestBody,
        run_as: FileSourcesInstancesUpdateParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Update or upgrade user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (FileSourcesInstancesUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (FileSourcesInstancesUpdateRequestBody)
                                     : Request body. (json)

        Returns:
            UserFileSourceModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/file_source_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: FileSourcesInstancesUpdateRequestBody = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserFileSourceModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_instances_test_instance(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesTestInstanceParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test a file source instance and return status.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (FileSourcesInstancesTestInstanceParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/file_source_instances/{uuid_}/test"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PluginStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_instances_test_instance(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesTestInstanceParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test a file source instance and return status.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (FileSourcesInstancesTestInstanceParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/file_source_instances/{uuid_}/test"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PluginStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_test_instances_update(
        self,
        uuid_: UUID,
        body: FileSourcesTestInstancesUpdateRequestBody,
        run_as: FileSourcesTestInstancesUpdateParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test updating or upgrading user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (FileSourcesTestInstancesUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (FileSourcesTestInstancesUpdateRequestBody)
                                     : Request body. (json)

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/file_source_instances/{uuid_}/test"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: FileSourcesTestInstancesUpdateRequestBody = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PluginStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_test_instances_update(
        self,
        uuid_: UUID,
        body: FileSourcesTestInstancesUpdateRequestBody,
        run_as: FileSourcesTestInstancesUpdateParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test updating or upgrading user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (FileSourcesTestInstancesUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (FileSourcesTestInstancesUpdateRequestBody)
                                     : Request body. (json)

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        uuid_ = DataclassSerializer.serialize(uuid_)

        url = f"{self.base_url}/api/file_source_instances/{uuid_}/test"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: FileSourcesTestInstancesUpdateRequestBody = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), PluginStatus)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_templates_index(
        self,
        run_as: FileSourcesTemplatesIndexParamRunAs | None = None,
    ) -> FileSourceTemplateSummaries:
        """
        Get a list of file source templates available to build user defined file sources from

        Args:
            run-as (FileSourcesTemplatesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            FileSourceTemplateSummaries: A list of the configured file source templates.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_templates"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), FileSourceTemplateSummaries)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_templates_index(
        self,
        run_as: FileSourcesTemplatesIndexParamRunAs | None = None,
    ) -> FileSourceTemplateSummaries:
        """
        Get a list of file source templates available to build user defined file sources from

        Args:
            run-as (FileSourcesTemplatesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            FileSourceTemplateSummaries: A list of the configured file source templates.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_templates"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), FileSourceTemplateSummaries)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_template_oauth2(
        self,
        template_id: str,
        template_version: int,
        run_as: FileSourcesTemplateOauth2ParamRunAs | None = None,
    ) -> OAuth2Info:
        """
        Template Oauth2

        Args:
            template_id (str)        : The template ID of the target file source template.
            template_version (int)   : The template version of the target file source template.
            run-as (FileSourcesTemplateOauth2ParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            OAuth2Info: OAuth2 authorization url to redirect user to prior to creation.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        template_id = DataclassSerializer.serialize(template_id)
        template_version = DataclassSerializer.serialize(template_version)

        url = f"{self.base_url}/api/file_source_templates/{template_id}/{template_version}/oauth2"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), OAuth2Info)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def file_sources_template_oauth2(
        self,
        template_id: str,
        template_version: int,
        run_as: FileSourcesTemplateOauth2ParamRunAs | None = None,
    ) -> OAuth2Info:
        """
        Template Oauth2

        Args:
            template_id (str)        : The template ID of the target file source template.
            template_version (int)   : The template version of the target file source template.
            run-as (FileSourcesTemplateOauth2ParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            OAuth2Info: OAuth2 authorization url to redirect user to prior to creation.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        template_id = DataclassSerializer.serialize(template_id)
        template_version = DataclassSerializer.serialize(template_version)

        url = f"{self.base_url}/api/file_source_templates/{template_id}/{template_version}/oauth2"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), OAuth2Info)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
