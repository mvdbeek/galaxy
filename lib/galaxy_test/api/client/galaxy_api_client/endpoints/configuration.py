from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_81 import AnonymousArrayItem81
from ..models.anonymous_array_item_83 import AnonymousArrayItem83
from ..models.configuration_decode_decode_id_200_response import ConfigurationDecodeDecodeId200Response
from ..models.configuration_decode_decode_id_param_run_as import ConfigurationDecodeDecodeIdParamRunAs
from ..models.configuration_dynamic_tool_confs_dynamic_tool_confs_param_run_as import (
    ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs,
)
from ..models.configuration_encode_encode_id_200_response import ConfigurationEncodeEncodeId200Response
from ..models.configuration_encode_encode_id_param_run_as import ConfigurationEncodeEncodeIdParamRunAs
from ..models.configuration_index_200_response import ConfigurationIndex200Response
from ..models.configuration_index_param_keys import ConfigurationIndexParamKeys
from ..models.configuration_index_param_run_as import ConfigurationIndexParamRunAs
from ..models.configuration_index_param_view import ConfigurationIndexParamView
from ..models.configuration_tool_lineages_tool_lineages_param_run_as import (
    ConfigurationToolLineagesToolLineagesParamRunAs,
)
from ..models.configuration_toolbox_reload_toolbox_param_run_as import ConfigurationToolboxReloadToolboxParamRunAs
from ..models.configuration_version_200_response import ConfigurationVersion200Response
from ..models.configuration_whoami_200_response import ConfigurationWhoami200Response
from ..models.configuration_whoami_param_run_as import ConfigurationWhoamiParamRunAs


@runtime_checkable
class ConfigurationClientProtocol(Protocol):
    """Protocol defining the interface of ConfigurationClient for dependency injection."""

    async def configuration_index(
        self,
        view: ConfigurationIndexParamView | None = None,
        keys: ConfigurationIndexParamKeys | None = None,
        run_as: ConfigurationIndexParamRunAs | None = None,
    ) -> ConfigurationIndex200Response: ...

    async def configuration_index(
        self,
        view: ConfigurationIndexParamView | None = None,
        keys: ConfigurationIndexParamKeys | None = None,
        run_as: ConfigurationIndexParamRunAs | None = None,
    ) -> ConfigurationIndex200Response: ...

    async def configuration_decode_decode_id(
        self,
        encoded_id: str,
        run_as: ConfigurationDecodeDecodeIdParamRunAs | None = None,
    ) -> ConfigurationDecodeDecodeId200Response: ...

    async def configuration_decode_decode_id(
        self,
        encoded_id: str,
        run_as: ConfigurationDecodeDecodeIdParamRunAs | None = None,
    ) -> ConfigurationDecodeDecodeId200Response: ...

    async def configuration_dynamic_tool_confs_dynamic_tool_confs(
        self,
        run_as: ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem81]: ...

    async def configuration_dynamic_tool_confs_dynamic_tool_confs(
        self,
        run_as: ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem81]: ...

    async def configuration_encode_encode_id(
        self,
        decoded_id: int,
        run_as: ConfigurationEncodeEncodeIdParamRunAs | None = None,
    ) -> ConfigurationEncodeEncodeId200Response: ...

    async def configuration_encode_encode_id(
        self,
        decoded_id: int,
        run_as: ConfigurationEncodeEncodeIdParamRunAs | None = None,
    ) -> ConfigurationEncodeEncodeId200Response: ...

    async def configuration_tool_lineages_tool_lineages(
        self,
        run_as: ConfigurationToolLineagesToolLineagesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem83]: ...

    async def configuration_tool_lineages_tool_lineages(
        self,
        run_as: ConfigurationToolLineagesToolLineagesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem83]: ...

    async def configuration_toolbox_reload_toolbox(
        self,
        run_as: ConfigurationToolboxReloadToolboxParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def configuration_toolbox_reload_toolbox(
        self,
        run_as: ConfigurationToolboxReloadToolboxParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def configuration_version(
        self,
    ) -> ConfigurationVersion200Response: ...

    async def configuration_version(
        self,
    ) -> ConfigurationVersion200Response: ...

    async def configuration_whoami(
        self,
        run_as: ConfigurationWhoamiParamRunAs | None = None,
    ) -> ConfigurationWhoami200Response | None: ...

    async def configuration_whoami(
        self,
        run_as: ConfigurationWhoamiParamRunAs | None = None,
    ) -> ConfigurationWhoami200Response | None: ...


class ConfigurationClient(ConfigurationClientProtocol):
    """Client for configuration endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def configuration_index(
        self,
        view: ConfigurationIndexParamView | None = None,
        keys: ConfigurationIndexParamKeys | None = None,
        run_as: ConfigurationIndexParamRunAs | None = None,
    ) -> ConfigurationIndex200Response:
        """
        Return an object containing exposable configuration settings

        Return an object containing exposable configuration settings.  A more complete list is
        returned if the user is an admin. Pass in `view` and a comma-seperated list of keys to
        control which configuration settings are returned.

        Args:
            view (ConfigurationIndexParamView | None)
                                     : View to be passed to the serializer
            keys (ConfigurationIndexParamKeys | None)
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (ConfigurationIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationIndex200Response: Object containing exposable configuration settings

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration"

        params: dict[str, Any] = {
            **({"view": DataclassSerializer.serialize(view)} if view is not None else {}),
            **({"keys": DataclassSerializer.serialize(keys)} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ConfigurationIndex200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_index(
        self,
        view: ConfigurationIndexParamView | None = None,
        keys: ConfigurationIndexParamKeys | None = None,
        run_as: ConfigurationIndexParamRunAs | None = None,
    ) -> ConfigurationIndex200Response:
        """
        Return an object containing exposable configuration settings

        Return an object containing exposable configuration settings.  A more complete list is
        returned if the user is an admin. Pass in `view` and a comma-seperated list of keys to
        control which configuration settings are returned.

        Args:
            view (ConfigurationIndexParamView | None)
                                     : View to be passed to the serializer
            keys (ConfigurationIndexParamKeys | None)
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (ConfigurationIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationIndex200Response: Object containing exposable configuration settings

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration"

        params: dict[str, Any] = {
            **({"view": DataclassSerializer.serialize(view)} if view is not None else {}),
            **({"keys": DataclassSerializer.serialize(keys)} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ConfigurationIndex200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_decode_decode_id(
        self,
        encoded_id: str,
        run_as: ConfigurationDecodeDecodeIdParamRunAs | None = None,
    ) -> ConfigurationDecodeDecodeId200Response:
        """
        Decode a given id

        Decode a given id.

        Args:
            encoded_id (str)         : Encoded id to be decoded
            run-as (ConfigurationDecodeDecodeIdParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationDecodeDecodeId200Response: Decoded id

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        encoded_id = DataclassSerializer.serialize(encoded_id)

        url = f"{self.base_url}/api/configuration/decode/{encoded_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ConfigurationDecodeDecodeId200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_decode_decode_id(
        self,
        encoded_id: str,
        run_as: ConfigurationDecodeDecodeIdParamRunAs | None = None,
    ) -> ConfigurationDecodeDecodeId200Response:
        """
        Decode a given id

        Decode a given id.

        Args:
            encoded_id (str)         : Encoded id to be decoded
            run-as (ConfigurationDecodeDecodeIdParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationDecodeDecodeId200Response: Decoded id

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        encoded_id = DataclassSerializer.serialize(encoded_id)

        url = f"{self.base_url}/api/configuration/decode/{encoded_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ConfigurationDecodeDecodeId200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_dynamic_tool_confs_dynamic_tool_confs(
        self,
        run_as: ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem81]:
        """
        Return dynamic tool configuration files

        Return dynamic tool configuration files.

        Args:
            run-as (ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem81]: Dynamic tool configuration files

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/dynamic_tool_confs"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem81])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_dynamic_tool_confs_dynamic_tool_confs(
        self,
        run_as: ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem81]:
        """
        Return dynamic tool configuration files

        Return dynamic tool configuration files.

        Args:
            run-as (ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem81]: Dynamic tool configuration files

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/dynamic_tool_confs"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem81])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_encode_encode_id(
        self,
        decoded_id: int,
        run_as: ConfigurationEncodeEncodeIdParamRunAs | None = None,
    ) -> ConfigurationEncodeEncodeId200Response:
        """
        Encode a given id

        Decode a given id.

        Args:
            decoded_id (int)         : Decoded id to be encoded
            run-as (ConfigurationEncodeEncodeIdParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationEncodeEncodeId200Response: Encoded id

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        decoded_id = DataclassSerializer.serialize(decoded_id)

        url = f"{self.base_url}/api/configuration/encode/{decoded_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ConfigurationEncodeEncodeId200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_encode_encode_id(
        self,
        decoded_id: int,
        run_as: ConfigurationEncodeEncodeIdParamRunAs | None = None,
    ) -> ConfigurationEncodeEncodeId200Response:
        """
        Encode a given id

        Decode a given id.

        Args:
            decoded_id (int)         : Decoded id to be encoded
            run-as (ConfigurationEncodeEncodeIdParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationEncodeEncodeId200Response: Encoded id

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        decoded_id = DataclassSerializer.serialize(decoded_id)

        url = f"{self.base_url}/api/configuration/encode/{decoded_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ConfigurationEncodeEncodeId200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_tool_lineages_tool_lineages(
        self,
        run_as: ConfigurationToolLineagesToolLineagesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem83]:
        """
        Return tool lineages for tools that have them

        Return tool lineages for tools that have them.

        Args:
            run-as (ConfigurationToolLineagesToolLineagesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem83]: Tool lineages for tools that have them

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/tool_lineages"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem83])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_tool_lineages_tool_lineages(
        self,
        run_as: ConfigurationToolLineagesToolLineagesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem83]:
        """
        Return tool lineages for tools that have them

        Return tool lineages for tools that have them.

        Args:
            run-as (ConfigurationToolLineagesToolLineagesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem83]: Tool lineages for tools that have them

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/tool_lineages"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem83])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_toolbox_reload_toolbox(
        self,
        run_as: ConfigurationToolboxReloadToolboxParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Reload the Galaxy toolbox (but not individual tools)

        Reload the Galaxy toolbox (but not individual tools).

        Args:
            run-as (ConfigurationToolboxReloadToolboxParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/toolbox"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_toolbox_reload_toolbox(
        self,
        run_as: ConfigurationToolboxReloadToolboxParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Reload the Galaxy toolbox (but not individual tools)

        Reload the Galaxy toolbox (but not individual tools).

        Args:
            run-as (ConfigurationToolboxReloadToolboxParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/toolbox"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_version(
        self,
    ) -> ConfigurationVersion200Response:
        """
        Return Galaxy version information: major/minor version, optional extra info

        Return Galaxy version information: major/minor version, optional extra info.

        Returns:
            ConfigurationVersion200Response: Galaxy version information: major/minor version,
                                             optional extra info

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/version"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ConfigurationVersion200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_version(
        self,
    ) -> ConfigurationVersion200Response:
        """
        Return Galaxy version information: major/minor version, optional extra info

        Return Galaxy version information: major/minor version, optional extra info.

        Returns:
            ConfigurationVersion200Response: Galaxy version information: major/minor version,
                                             optional extra info

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/version"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ConfigurationVersion200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_whoami(
        self,
        run_as: ConfigurationWhoamiParamRunAs | None = None,
    ) -> ConfigurationWhoami200Response | None:
        """
        Return information about the current authenticated user

        Return information about the current authenticated user.

        Args:
            run-as (ConfigurationWhoamiParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationWhoami200Response | None: Information about the current authenticated
                                                   user

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/whoami"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return (
                    structure_from_dict(response.json(), ConfigurationWhoami200Response)
                    if response.json() is not None
                    else None
                )
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def configuration_whoami(
        self,
        run_as: ConfigurationWhoamiParamRunAs | None = None,
    ) -> ConfigurationWhoami200Response | None:
        """
        Return information about the current authenticated user

        Return information about the current authenticated user.

        Args:
            run-as (ConfigurationWhoamiParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationWhoami200Response | None: Information about the current authenticated
                                                   user

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/whoami"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return (
                    structure_from_dict(response.json(), ConfigurationWhoami200Response)
                    if response.json() is not None
                    else None
                )
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
