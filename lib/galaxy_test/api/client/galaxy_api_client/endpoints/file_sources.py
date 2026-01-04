from typing import Any, cast
from uuid import UUID

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
from ..models.file_sources_instances_update_request_body_2 import FileSourcesInstancesUpdateRequestBody2
from ..models.file_sources_template_oauth_2_param_run_as import FileSourcesTemplateOauth2ParamRunAs
from ..models.file_sources_templates_index_param_run_as import FileSourcesTemplatesIndexParamRunAs
from ..models.file_sources_test_instances_update_param_run_as import FileSourcesTestInstancesUpdateParamRunAs
from ..models.file_sources_test_instances_update_request_body_2 import FileSourcesTestInstancesUpdateRequestBody2
from ..models.file_sources_test_new_instance_configuration_param_run_as import (
    FileSourcesTestNewInstanceConfigurationParamRunAs,
)
from ..models.o_auth_2_info import OAuth2Info
from ..models.plugin_status import PluginStatus
from ..models.user_file_source_model import UserFileSourceModel


class FileSourcesClient:
    """Client for file_sources endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def file_sources_instances_index_2_2(
        self,
        run_as: FileSourcesInstancesIndexParamRunAs | None = None,
    ) -> list[UserFileSourceModel]:
        """
        Get a list of persisted file source instances defined by the requesting user.

        Args:
            run-as (Optional[FileSourcesInstancesIndexParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[UserFileSourceModel], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_instances_index_2_2(
        self,
        run_as: FileSourcesInstancesIndexParamRunAs | None = None,
    ) -> list[UserFileSourceModel]:
        """
        Get a list of persisted file source instances defined by the requesting user.

        Args:
            run-as (Optional[FileSourcesInstancesIndexParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[UserFileSourceModel], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_create_instance_2_2(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesCreateInstanceParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Create a user-bound file source.

        Args:
            run-as (Optional[FileSourcesCreateInstanceParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateInstancePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserFileSourceModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_create_instance_2_2(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesCreateInstanceParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Create a user-bound file source.

        Args:
            run-as (Optional[FileSourcesCreateInstanceParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateInstancePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserFileSourceModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_test_new_instance_configuration_2_2(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesTestNewInstanceConfigurationParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test payload for creating user-bound file source.

        Args:
            run-as (Optional[FileSourcesTestNewInstanceConfigurationParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateInstancePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(PluginStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_test_new_instance_configuration_2_2(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesTestNewInstanceConfigurationParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test payload for creating user-bound file source.

        Args:
            run-as (Optional[FileSourcesTestNewInstanceConfigurationParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateInstancePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(PluginStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_instances_purge_2_2(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesPurgeParamRunAs | None = None,
    ) -> None:
        """
        Purge user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (Optional[FileSourcesInstancesPurgeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_instances_purge_2_2(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesPurgeParamRunAs | None = None,
    ) -> None:
        """
        Purge user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (Optional[FileSourcesInstancesPurgeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_instances_get_2_2(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesGetParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Get a persisted user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (Optional[FileSourcesInstancesGetParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserFileSourceModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserFileSourceModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_instances_get_2_2(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesGetParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Get a persisted user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (Optional[FileSourcesInstancesGetParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserFileSourceModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserFileSourceModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_instances_update_2_2(
        self,
        uuid_: UUID,
        body: FileSourcesInstancesUpdateRequestBody2,
        run_as: FileSourcesInstancesUpdateParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Update or upgrade user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (Optional[FileSourcesInstancesUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (FileSourcesInstancesUpdateRequestBody2)
                                     : Request body. (json)

        Returns:
            UserFileSourceModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: FileSourcesInstancesUpdateRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserFileSourceModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_instances_update_2_2(
        self,
        uuid_: UUID,
        body: FileSourcesInstancesUpdateRequestBody2,
        run_as: FileSourcesInstancesUpdateParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Update or upgrade user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (Optional[FileSourcesInstancesUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (FileSourcesInstancesUpdateRequestBody2)
                                     : Request body. (json)

        Returns:
            UserFileSourceModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: FileSourcesInstancesUpdateRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserFileSourceModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_instances_test_instance_2_2(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesTestInstanceParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test a file source instance and return status.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (Optional[FileSourcesInstancesTestInstanceParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances/{uuid_}/test"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(PluginStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_instances_test_instance_2_2(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesTestInstanceParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test a file source instance and return status.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (Optional[FileSourcesInstancesTestInstanceParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances/{uuid_}/test"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(PluginStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_test_instances_update_2_2(
        self,
        uuid_: UUID,
        body: FileSourcesTestInstancesUpdateRequestBody2,
        run_as: FileSourcesTestInstancesUpdateParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test updating or upgrading user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (Optional[FileSourcesTestInstancesUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (FileSourcesTestInstancesUpdateRequestBody2)
                                     : Request body. (json)

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances/{uuid_}/test"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: FileSourcesTestInstancesUpdateRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(PluginStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_test_instances_update_2_2(
        self,
        uuid_: UUID,
        body: FileSourcesTestInstancesUpdateRequestBody2,
        run_as: FileSourcesTestInstancesUpdateParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test updating or upgrading user file source instance.

        Args:
            uuid (UUID)              : The UUID index for a persisted UserFileSourceStore
                                       object.
            run-as (Optional[FileSourcesTestInstancesUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (FileSourcesTestInstancesUpdateRequestBody2)
                                     : Request body. (json)

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_instances/{uuid_}/test"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: FileSourcesTestInstancesUpdateRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(PluginStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_templates_index_2_2(
        self,
        run_as: FileSourcesTemplatesIndexParamRunAs | None = None,
    ) -> FileSourceTemplateSummaries:
        """
        Get a list of file source templates available to build user defined file sources from

        Args:
            run-as (Optional[FileSourcesTemplatesIndexParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(FileSourceTemplateSummaries, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_templates_index_2_2(
        self,
        run_as: FileSourcesTemplatesIndexParamRunAs | None = None,
    ) -> FileSourceTemplateSummaries:
        """
        Get a list of file source templates available to build user defined file sources from

        Args:
            run-as (Optional[FileSourcesTemplatesIndexParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(FileSourceTemplateSummaries, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_template_oauth2_2_2(
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
            run-as (Optional[FileSourcesTemplateOauth2ParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            OAuth2Info: OAuth2 authorization url to redirect user to prior to creation.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_templates/{template_id}/{template_version}/oauth2"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(OAuth2Info, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def file_sources_template_oauth2_2_2(
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
            run-as (Optional[FileSourcesTemplateOauth2ParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            OAuth2Info: OAuth2 authorization url to redirect user to prior to creation.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_source_templates/{template_id}/{template_version}/oauth2"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(OAuth2Info, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
