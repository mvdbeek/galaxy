from typing import Any, cast
from uuid import UUID

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_216 import AnonymousArrayItem216
from ..models.concrete_object_store_model import ConcreteObjectStoreModel
from ..models.create_instance_payload import CreateInstancePayload
from ..models.object_store_template_summaries import ObjectStoreTemplateSummaries
from ..models.object_stores_create_instance_param_run_as import ObjectStoresCreateInstanceParamRunAs
from ..models.object_stores_index_param_run_as import ObjectStoresIndexParamRunAs
from ..models.object_stores_instances_get_param_run_as import ObjectStoresInstancesGetParamRunAs
from ..models.object_stores_instances_index_param_run_as import ObjectStoresInstancesIndexParamRunAs
from ..models.object_stores_instances_purge_param_run_as import ObjectStoresInstancesPurgeParamRunAs
from ..models.object_stores_instances_test_instance_param_run_as import ObjectStoresInstancesTestInstanceParamRunAs
from ..models.object_stores_instances_update_param_run_as import ObjectStoresInstancesUpdateParamRunAs
from ..models.object_stores_instances_update_request_body_2 import ObjectStoresInstancesUpdateRequestBody2
from ..models.object_stores_show_info_param_run_as import ObjectStoresShowInfoParamRunAs
from ..models.object_stores_templates_index_param_run_as import ObjectStoresTemplatesIndexParamRunAs
from ..models.object_stores_test_instances_update_param_run_as import ObjectStoresTestInstancesUpdateParamRunAs
from ..models.object_stores_test_instances_update_request_body_2 import ObjectStoresTestInstancesUpdateRequestBody2
from ..models.object_stores_test_new_instance_configuration_param_run_as import (
    ObjectStoresTestNewInstanceConfigurationParamRunAs,
)
from ..models.plugin_status import PluginStatus
from ..models.user_concrete_object_store_model import UserConcreteObjectStoreModel


class ObjectStoresClient:
    """Client for object_stores endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def object_stores_instances_index_2_2(
        self,
        run_as: ObjectStoresInstancesIndexParamRunAs | None = None,
    ) -> list[UserConcreteObjectStoreModel]:
        """
        Get a list of persisted object store instances defined by the requesting user.

        Args:
            run-as (Optional[ObjectStoresInstancesIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UserConcreteObjectStoreModel]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[UserConcreteObjectStoreModel], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_instances_index_2_2(
        self,
        run_as: ObjectStoresInstancesIndexParamRunAs | None = None,
    ) -> list[UserConcreteObjectStoreModel]:
        """
        Get a list of persisted object store instances defined by the requesting user.

        Args:
            run-as (Optional[ObjectStoresInstancesIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UserConcreteObjectStoreModel]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[UserConcreteObjectStoreModel], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_create_instance_2_2(
        self,
        body: CreateInstancePayload,
        run_as: ObjectStoresCreateInstanceParamRunAs | None = None,
    ) -> UserConcreteObjectStoreModel:
        """
        Create a user-bound object store.

        Args:
            run-as (Optional[ObjectStoresCreateInstanceParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateInstancePayload)
                                     : Request body. (json)

        Returns:
            UserConcreteObjectStoreModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateInstancePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserConcreteObjectStoreModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_create_instance_2_2(
        self,
        body: CreateInstancePayload,
        run_as: ObjectStoresCreateInstanceParamRunAs | None = None,
    ) -> UserConcreteObjectStoreModel:
        """
        Create a user-bound object store.

        Args:
            run-as (Optional[ObjectStoresCreateInstanceParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateInstancePayload)
                                     : Request body. (json)

        Returns:
            UserConcreteObjectStoreModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateInstancePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserConcreteObjectStoreModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_test_new_instance_configuration_2_2(
        self,
        body: CreateInstancePayload,
        run_as: ObjectStoresTestNewInstanceConfigurationParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test payload for creating user-bound object store.

        Args:
            run-as (Optional[ObjectStoresTestNewInstanceConfigurationParamRunAs])
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
        url = f"{self.base_url}/api/object_store_instances/test"

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

    async def object_stores_test_new_instance_configuration_2_2(
        self,
        body: CreateInstancePayload,
        run_as: ObjectStoresTestNewInstanceConfigurationParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test payload for creating user-bound object store.

        Args:
            run-as (Optional[ObjectStoresTestNewInstanceConfigurationParamRunAs])
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
        url = f"{self.base_url}/api/object_store_instances/test"

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

    async def object_stores_instances_purge_2_2(
        self,
        uuid_: UUID,
        run_as: ObjectStoresInstancesPurgeParamRunAs | None = None,
    ) -> None:
        """
        Purge user object store instance.

        Args:
            uuid (UUID)              : The UUID used to identify a persisted UserObjectStore
                                       object.
            run-as (Optional[ObjectStoresInstancesPurgeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances/{uuid_}"

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

    async def object_stores_instances_purge_2_2(
        self,
        uuid_: UUID,
        run_as: ObjectStoresInstancesPurgeParamRunAs | None = None,
    ) -> None:
        """
        Purge user object store instance.

        Args:
            uuid (UUID)              : The UUID used to identify a persisted UserObjectStore
                                       object.
            run-as (Optional[ObjectStoresInstancesPurgeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances/{uuid_}"

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

    async def object_stores_instances_get_2_2(
        self,
        uuid_: UUID,
        run_as: ObjectStoresInstancesGetParamRunAs | None = None,
    ) -> UserConcreteObjectStoreModel:
        """
        Get a persisted user object store instance.

        Args:
            uuid (UUID)              : The UUID used to identify a persisted UserObjectStore
                                       object.
            run-as (Optional[ObjectStoresInstancesGetParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserConcreteObjectStoreModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserConcreteObjectStoreModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_instances_get_2_2(
        self,
        uuid_: UUID,
        run_as: ObjectStoresInstancesGetParamRunAs | None = None,
    ) -> UserConcreteObjectStoreModel:
        """
        Get a persisted user object store instance.

        Args:
            uuid (UUID)              : The UUID used to identify a persisted UserObjectStore
                                       object.
            run-as (Optional[ObjectStoresInstancesGetParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserConcreteObjectStoreModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserConcreteObjectStoreModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_instances_update_2_2(
        self,
        uuid_: UUID,
        body: ObjectStoresInstancesUpdateRequestBody2,
        run_as: ObjectStoresInstancesUpdateParamRunAs | None = None,
    ) -> UserConcreteObjectStoreModel:
        """
        Update or upgrade user object store instance.

        Args:
            uuid (UUID)              : The UUID used to identify a persisted UserObjectStore
                                       object.
            run-as (Optional[ObjectStoresInstancesUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ObjectStoresInstancesUpdateRequestBody2)
                                     : Request body. (json)

        Returns:
            UserConcreteObjectStoreModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ObjectStoresInstancesUpdateRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserConcreteObjectStoreModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_instances_update_2_2(
        self,
        uuid_: UUID,
        body: ObjectStoresInstancesUpdateRequestBody2,
        run_as: ObjectStoresInstancesUpdateParamRunAs | None = None,
    ) -> UserConcreteObjectStoreModel:
        """
        Update or upgrade user object store instance.

        Args:
            uuid (UUID)              : The UUID used to identify a persisted UserObjectStore
                                       object.
            run-as (Optional[ObjectStoresInstancesUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ObjectStoresInstancesUpdateRequestBody2)
                                     : Request body. (json)

        Returns:
            UserConcreteObjectStoreModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ObjectStoresInstancesUpdateRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserConcreteObjectStoreModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_instances_test_instance_2_2(
        self,
        uuid_: UUID,
        run_as: ObjectStoresInstancesTestInstanceParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Get a persisted user object store instance.

        Args:
            uuid (UUID)              : The UUID used to identify a persisted UserObjectStore
                                       object.
            run-as (Optional[ObjectStoresInstancesTestInstanceParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances/{uuid_}/test"

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

    async def object_stores_instances_test_instance_2_2(
        self,
        uuid_: UUID,
        run_as: ObjectStoresInstancesTestInstanceParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Get a persisted user object store instance.

        Args:
            uuid (UUID)              : The UUID used to identify a persisted UserObjectStore
                                       object.
            run-as (Optional[ObjectStoresInstancesTestInstanceParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances/{uuid_}/test"

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

    async def object_stores_test_instances_update_2_2(
        self,
        uuid_: UUID,
        body: ObjectStoresTestInstancesUpdateRequestBody2,
        run_as: ObjectStoresTestInstancesUpdateParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test updating or upgrading user object source instance.

        Args:
            uuid (UUID)              : The UUID used to identify a persisted UserObjectStore
                                       object.
            run-as (Optional[ObjectStoresTestInstancesUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ObjectStoresTestInstancesUpdateRequestBody2)
                                     : Request body. (json)

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances/{uuid_}/test"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ObjectStoresTestInstancesUpdateRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(PluginStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_test_instances_update_2_2(
        self,
        uuid_: UUID,
        body: ObjectStoresTestInstancesUpdateRequestBody2,
        run_as: ObjectStoresTestInstancesUpdateParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Test updating or upgrading user object source instance.

        Args:
            uuid (UUID)              : The UUID used to identify a persisted UserObjectStore
                                       object.
            run-as (Optional[ObjectStoresTestInstancesUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ObjectStoresTestInstancesUpdateRequestBody2)
                                     : Request body. (json)

        Returns:
            PluginStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_instances/{uuid_}/test"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ObjectStoresTestInstancesUpdateRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(PluginStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_templates_index_2_2(
        self,
        run_as: ObjectStoresTemplatesIndexParamRunAs | None = None,
    ) -> ObjectStoreTemplateSummaries:
        """
        Get a list of object store templates available to build user defined object stores from

        Args:
            run-as (Optional[ObjectStoresTemplatesIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ObjectStoreTemplateSummaries: A list of the configured object store templates.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_templates"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ObjectStoreTemplateSummaries, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_templates_index_2_2(
        self,
        run_as: ObjectStoresTemplatesIndexParamRunAs | None = None,
    ) -> ObjectStoreTemplateSummaries:
        """
        Get a list of object store templates available to build user defined object stores from

        Args:
            run-as (Optional[ObjectStoresTemplatesIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ObjectStoreTemplateSummaries: A list of the configured object store templates.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_store_templates"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ObjectStoreTemplateSummaries, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_index_2_2(
        self,
        selectable: bool | None = False,
        run_as: ObjectStoresIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem216]:
        """
        Get a list of (currently only concrete) object stores configured with this Galaxy
        instance.

        Args:
            selectable (Optional[bool])
                                     : Restrict index query to user selectable object stores,
                                       the current implementation requires this to be true.
            run-as (Optional[ObjectStoresIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem216]: A list of the configured object stores.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_stores"

        params: dict[str, Any] = {
            **({"selectable": selectable} if selectable is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem216], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_index_2_2(
        self,
        selectable: bool | None = False,
        run_as: ObjectStoresIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem216]:
        """
        Get a list of (currently only concrete) object stores configured with this Galaxy
        instance.

        Args:
            selectable (Optional[bool])
                                     : Restrict index query to user selectable object stores,
                                       the current implementation requires this to be true.
            run-as (Optional[ObjectStoresIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem216]: A list of the configured object stores.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_stores"

        params: dict[str, Any] = {
            **({"selectable": selectable} if selectable is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem216], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_show_info_2_2(
        self,
        object_store_id: str,
        run_as: ObjectStoresShowInfoParamRunAs | None = None,
    ) -> ConcreteObjectStoreModel:
        """
        Get information about a concrete object store configured with Galaxy.

        Args:
            object_store_id (str)    : The concrete object store ID.
            run-as (Optional[ObjectStoresShowInfoParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConcreteObjectStoreModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_stores/{object_store_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConcreteObjectStoreModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def object_stores_show_info_2_2(
        self,
        object_store_id: str,
        run_as: ObjectStoresShowInfoParamRunAs | None = None,
    ) -> ConcreteObjectStoreModel:
        """
        Get information about a concrete object store configured with Galaxy.

        Args:
            object_store_id (str)    : The concrete object store ID.
            run-as (Optional[ObjectStoresShowInfoParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConcreteObjectStoreModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/object_stores/{object_store_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConcreteObjectStoreModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
